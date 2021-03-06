import abc
import sys
from contextlib import redirect_stdout
from io import StringIO
from typing import List, Set, Union, TextIO, Optional, cast

from biolinkml.meta import SchemaDefinition, ClassDefinition, SlotDefinition, ClassDefinitionName, \
    TypeDefinition, Element, SlotDefinitionName, TypeDefinitionName, PrefixPrefixPrefix, ElementName, \
    SubsetDefinition, SubsetDefinitionName
from biolinkml.utils.formatutils import camelcase, underscore
from biolinkml.utils.mergeutils import alias_root
from biolinkml.utils.schemaloader import SchemaLoader
from biolinkml.utils.typereferences import References


class Generator(metaclass=abc.ABCMeta):
    generatorname: str = None                   # Set to os.path.basename(__file__)
    generatorversion: str = None                # Generator version identifier
    valid_formats: List[str] = []               # Allowed formats
    base_dir: str = None                        # Base directory of schema

    visit_all_class_slots: bool = False         # False means only visit own slots, True means visit all slots
    visits_are_sorted: bool = True              # True means visit basic types in alphabetial order, false in entry
    sort_class_slots: bool = False              # True means visit class slots in alphabetical order

    def __init__(self,
                 schema: Union[str, TextIO, SchemaDefinition, "Generator"],
                 fmt: Optional[str] = None,
                 emit_metadata: bool = False) -> None:
        """
        Constructor

        :param schema: metamodel compliant schema.  Can be URI, file name, actual schema, another generator, an
        open file or a pre-parsed schema.
        :param fmt: expected output format
        :param emit_metadata: True means include date, generator, etc. information in source header if appropriate
        """
        if fmt is None:
            fmt = self.valid_formats[0]
        assert fmt in self.valid_formats, f"Unrecognized format: {fmt}"
        self.format = fmt
        self.emit_metadata = emit_metadata
        if isinstance(schema, Generator):
            gen = schema
            self.schema = gen.schema
            self.synopsis = gen.synopsis
            self.namespaces = gen.namespaces
            self.base_dir = gen.base_dir
            self.schema_location = gen.schema_location
        else:
            loader = SchemaLoader(schema, self.base_dir)
            loader.resolve()
            self.schema = loader.schema
            self.synopsis = loader.synopsis
            self.namespaces = loader.namespaces
            self.base_dir = loader.base_dir
            self.schema_location = loader.schema_location

    def serialize(self, **kwargs) -> str:
        """
        Generate output in the required format

        :param kwargs: Generater specific parameters
        :return: Generated outputt
        """
        output = StringIO()
        with redirect_stdout(output):
            self.visit_schema(**kwargs)
            for sn, ss in (sorted(self.schema.subsets.items(), key=lambda s: s[0].lower()) if self.visits_are_sorted
                           else self.schema.subsets.items()):
                self.visit_subset(ss)
            for tn, typ in (sorted(self.schema.types.items(), key=lambda s: s[0].lower()) if self.visits_are_sorted
                            else self.schema.types.items()):
                self.visit_type(typ)
            for sn, slot in (sorted(self.schema.slots.items(), key=lambda c: c[0].lower()) if self.visits_are_sorted
                             else self.schema.slots.items()):
                self.visit_slot(self.aliased_slot_name(slot), slot)
            for cls in (sorted(self.schema.classes.values(), key=lambda c: c.name.lower()) if self.visits_are_sorted
                        else self.schema.classes.values()):
                if self.visit_class(cls):
                    for slot in self.all_slots(cls) if self.visit_all_class_slots else self.own_slots(cls):
                        self.visit_class_slot(cls, self.aliased_slot_name(slot), slot)
                    self.end_class(cls)
            self.end_schema(**kwargs)
        return output.getvalue()

    def visit_schema(self, **kwargs) -> None:
        """ Visited once at the beginning of generation

        @param kwargs: Arguments passed through from CLI -- implementation dependent
        """
        ...

    def end_schema(self, **kwargs) -> None:
        """ Visited once at the end of generation

        @param kwargs: Arguments passed through from CLI -- implementation dependent
        """
        ...

    def visit_class(self, cls: ClassDefinition) -> bool:
        """ Visited once per schema class

        @param cls: class being visited
        @return: Visit slots and end class.  False means skip and go on
        """
        return True

    def end_class(self, cls: ClassDefinition) -> None:
        """ Visited after visit_class_slots (if visit_class returned true)

        @param cls: class being visited
        """
        ...

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        """ Visited for each slot in a class.  If class level visit_all_slots is true, this is visited once
        for any class that is inherited (class itself, is_a, mixin, apply_to).  Otherwise just the own slots.

        @param cls: containing class
        @param aliased_slot_name: Aliased slot name.  May not be unique across all class slots
        @param slot: slot being visited
        """
        ...

    def visit_slot(self, aliased_slot_name: str, slot: SlotDefinition) -> None:
        """ Visited once for every slot definition in the schema.

        @param aliased_slot_name: Aliased name of the slot.  May not be unique
        @param slot: visited slot
        """
        ...

    def visit_type(self, typ: TypeDefinition) -> None:
        """ Visited once for every type definition in the schema

        @param typ: Type definition
        """
        ...

    def visit_subset(self, subset: SubsetDefinition) -> None:
        """ Visited once for every subset definition in the schema

        #param subset: Subset definition
        """
        ...

    # =============================
    # Helper methods
    # =============================
    def own_slots(self, cls: Union[ClassDefinitionName, ClassDefinition]) -> List[SlotDefinition]:
        """ Return the list of slots owned the class definition.  An "own slot" is any ``cls`` slot that does not appear
        in the class is_a parent.  Own_slots include:

            * any slot whose domain is cls
            * slot_usage entries
            * slots from mixins entries
            * slots from apply_to entries


        @param cls: class name or class definition name
        @return: list of owned slots.  List is sorted if sort_class_slots is true, otherwise in class order
        """
        if not isinstance(cls, ClassDefinition):
            cls = self.schema.classes[cls]
        parent = self.schema.classes[cls.is_a] if cls.is_a else None
        seen = set()
        rval = []
        for sname in cls.slots:
            sname_base = alias_root(self.schema, sname)
            if sname_base not in seen and (not parent or sname not in parent.slots):
                slot = self.schema.slots[sname]
                rval.append(slot)
                seen.add(sname_base)
        return sorted(rval, key=lambda s: s.name) if self.sort_class_slots else rval

    def own_slot_names(self, cls: Union[ClassDefinitionName, ClassDefinition]) -> List[SlotDefinitionName]:
        return [slot.name for slot in self.own_slots(cls)]

    def all_slots(self, cls: Union[ClassDefinitionName, ClassDefinition], *, cls_slots_first: bool = False,
                  seen: Optional[Set[ClassDefinitionName]] = None) \
            -> List[SlotDefinition]:
        """ Return all slots that are part of the class definition.  This includes all is_a, mixin and apply_to slots
        but does NOT include slot_usage targets.  If class B has a slot_usage entry for slot "s", only the slot
        definition for the redefined slot will be included, not its base.  Slots are added in the order they appear
        in classes, with recursive is_a's being added first followed by mixins and finally apply_tos

        @param cls: class definition or class definition name
        @param cls_slots_first: True means return own slots at the top of the list
        @param seen: List of slots already recorded. Used for internal recursion
        @return: ordered list of slots in the class with slot usages removed
        """
        if not isinstance(cls, ClassDefinition):
            cls = self.schema.classes[cls]
        if seen is None:
            seen = set()
        rval = []

        parent = self.schema.classes[cls.is_a] if cls.is_a else None
        if cls_slots_first:
            for slot in self.own_slots(cls):
                sname_base = alias_root(self.schema, slot.name)
                if sname_base not in seen:
                    rval.append(slot)
                    seen.add(sname_base)
            return rval + (self.all_slots(parent, cls_slots_first=cls_slots_first, seen=seen) if parent else [])
        else:
            for sname in cls.slots:
                sname_base = alias_root(self.schema, sname)
                if sname_base not in seen:
                    slot = self.schema.slots[sname]
                    rval.append(slot)
                    seen.add(sname_base)
            return sorted(rval, key=lambda s: s.name) if self.sort_class_slots else rval

    def parent(self, element: Union[ClassDefinition, SlotDefinition]) \
            -> Optional[Union[ClassDefinition, SlotDefinition]]:
        """ Return the parent of element, if any """
        return \
            None if element.is_a is None else \
            self.schema.classes[element.is_a] if isinstance(element, ClassDefinition) else \
            self.schema.slots[element.is_a]

    def ancestors(self, element: Union[ClassDefinition, SlotDefinition]) -> List[ElementName]:
        """ Return an ordered list of ancestor names for the supplied slot or class

        @param element: Slot or class name or definition
        @return: Ordered list of of ancestor names
        """
        return [element.name] + ([] if element.is_a is None else self.ancestors(self.parent(element)))

    def neighborhood(self, elements: Union[str, ElementName, List[ElementName]]) \
            -> References:
        """ Return a list of all slots, classes and types that touch any element in elements, including the element
        itself

        @param elements: Element names to do proximity with
        @return: All slots and classes that touch element
        """
        if isinstance(elements, (str, ElementName)):
            elements = [elements]
        touches = References()
        for element in elements:
            if element in self.schema.classes:
                touches.classrefs.add(cast(ClassDefinitionName, element))
                cls = self.schema.classes[cast(ClassDefinitionName, element)]
                if cls.is_a:
                    touches.classrefs.add(cls.is_a)
                # Mixins include apply_to's
                touches.classrefs.update(set(cls.mixins))
                for slotname in cls.slots:
                    slot = self.schema.slots[slotname]
                    if slot.range in self.schema.classes:
                        touches.classrefs.add(cast(ClassDefinitionName, slot.range))
                    elif slot.range in self.schema.types:
                        touches.typerefs.add(cast(TypeDefinitionName, slot.range))
                for cv in self.schema.classes.values():
                    if cv.is_a == element:
                        touches.classrefs.add(cv.name)
                if element in self.synopsis.rangerefs:
                    for slotname in self.synopsis.rangerefs[element]:
                        touches.slotrefs.add(slotname)
                        if self.schema.slots[slotname].domain:
                            touches.classrefs.add(self.schema.slots[slotname].domain)
                if cls.in_subset:
                    touches.subsetrefs.update(cls.in_subset)
            if element in self.schema.slots:
                touches.slotrefs.add(cast(SlotDefinitionName, element))
                slot = self.schema.slots[cast(SlotDefinitionName, element)]
                touches.slotrefs.update(set(slot.mixins))
                if slot.is_a:
                    touches.slotrefs.add(slot.is_a)
                if element in self.synopsis.inverses:
                    touches.slotrefs.update(self.synopsis.inverses[cast(SlotDefinitionName, element)])
                if slot.domain:
                    touches.classrefs.add(slot.domain)
                if slot.range in self.schema.classes:
                    touches.classrefs.add(cast(ClassDefinitionName, slot.range))
                elif slot.range in self.schema.types:
                    touches.typerefs.add(cast(TypeDefinitionName, slot.range))
                if slot.in_subset:
                    touches.subsetrefs.update(slot.in_subset)
                for sv in self.schema.slots.values():
                    if sv.is_a == element:
                        touches.slotrefs.add(sv.name)
            if element in self.schema.types:
                touches.typerefs.add(cast(TypeDefinitionName, element))
                typ = self.schema.types[cast(TypeDefinitionName, element)]
                if element in self.synopsis.rangerefs:
                    touches.slotrefs.update(self.synopsis.rangerefs[element])
                if typ.typeof:
                    touches.typerefs.add(cast(TypeDefinitionName, typ.typeof))
                if typ.in_subset:
                    touches.subsetrefs.update(typ.in_subset)
                for tv in self.schema.types.values():
                    if tv.typeof == element:
                        touches.slotrefs.add(tv.name)
            if element in self.schema.subsets:
                touches.subsetrefs.add(cast(SubsetDefinitionName, element))
                if element in self.synopsis.subsetrefs:
                    touches.update(self.synopsis.subsetrefs[cast(SubsetDefinitionName, element)])
            if not bool(touches):
                print(f"Warning: neighborhood({element}) - {element} is undefined", file=sys.stderr)

        return touches

    def range_type_path(self, typ: TypeDefinition) -> List[str]:
        """
        Return a formatted list of range types from the base up

        :param typ: type definition whose name is to be formatted
        :return: List of possible types with base at the leftmost
        """
        formatted_typ_name = self.class_or_type_name(typ.name)
        if typ.typeof:
            return self.range_type_path(self.schema.types[cast(TypeDefinitionName, typ.typeof)]) + [formatted_typ_name]
        elif typ.repr:
            return [typ.repr, formatted_typ_name]
        else:
            return [formatted_typ_name]

    def class_identifier(self, def_or_name: Union[str, ClassDefinition, TypeDefinition], keys_count: bool=False) \
            -> Optional[SlotDefinitionName]:
        """
        Return the class identifier if any

        :param def_or_name: class name or definition
        :param keys_count: True means treat keys AND identifiers as identifiers
        :return: name of class identifier (or key) if one exists
        """
        if isinstance(def_or_name, ClassDefinition):
            cls = def_or_name
        elif def_or_name in self.schema.classes:
            cls = self.schema.classes[cast(ClassDefinitionName, def_or_name)]
        else:
            return None
        for slotname in cls.slots:
            slot = self.schema.slots[slotname]
            if slot.identifier or (keys_count and slot.key):
                return slotname
        return None

    def class_identifier_path(self, cls_or_clsname: Union[str, ClassDefinition], force_non_key: bool) -> List[str]:
        """
        Return the path closure to a class identifier if the class has a key and force_non_key is false otherwise
        return a dictionary closure.

        :param cls_or_clsname: class definition
        :param force_non_key: True means inlined even if the class has a key
        :return: path
        """
        cls = cls_or_clsname if isinstance(cls_or_clsname, ClassDefinition)\
            else self.schema.classes[cast(ClassDefinitionName, cls_or_clsname)]

        # Determine whether the class has a key
        identifier_slot = None
        if not force_non_key:
            identifier_slot = self.class_identifier(cls, keys_count=True)

        # No key or inlined, its closure is a dictionary
        if identifier_slot is None:
            return ['dict', self.class_or_type_name(cls.name)]

        # We're dealing with a reference
        pathname = camelcase(cls.name + ' ' + self.aliased_slot_name(identifier_slot))
        if cls.is_a:
            parent_identifier_slot = self.class_identifier(cls.is_a, keys_count=True)
            if parent_identifier_slot:
                return self.class_identifier_path(cls.is_a, False) + [pathname]
        return self.slot_type_path(identifier_slot) + [pathname]

    def slot_type_path(self, slot_or_name: Union[str, SlotDefinition]) -> List[str]:
        """
        Return a ordered list of types starting with the base type and ending with the most proximal type

        :param slot_or_name: slot whose range is being typed
        :return: ordered list of types from base type forward
        """
        slot = slot_or_name if isinstance(slot_or_name, SlotDefinition) \
            else self.schema.slots[cast(SlotDefinitionName, slot_or_name)]
        if slot.range in self.schema.types:
            # Type
            return self.range_type_path(self.schema.types[cast(TypeDefinitionName, slot.range)])
        else:
            # Class
            return self.class_identifier_path(slot.range, bool(slot.inlined))

    def aliased_slot_name(self, slot: Union[SlotDefinitionName, SlotDefinition]) -> SlotDefinitionName:
        """ Return the overloaded slot name -- the alias if one exists otherwise the actual name

        @param slot: either a slot name or a definition
        @return: overloaded name
        """
        if isinstance(slot, str):
            slot = self.schema.slots[cast(SlotDefinitionName, slot)]
        return slot.alias if slot.alias else slot.name

    def class_or_type_name(self, name: str) -> str:
        """
        Return the camelcase representation of clsname if it is a valid class or type.  Prepend "Unknown"
        if the name isn't valid
        """
        if name in self.schema.classes:
            return camelcase(name)
        elif name in self.schema.types:
            typ = self.schema.types[cast(TypeDefinitionName, name)]
            if typ.typeof:
                return camelcase(name)
            else:
                return typ.base
        else:
            return "Unknown_" + camelcase(name)

    def slot_name(self, name: SlotDefinitionName) -> str:
        """
        Return the underscored version of the aliased slot name if name is a slot. Prepend "unknown_" if the name
        isn't valid.
        """
        slot = self.schema.slots.get(name)
        return underscore(self.aliased_slot_name(slot) if slot else ("unknown " + name))


    def subset_name(self, name: str) -> str:
        return ('' if name in self.schema.subsets else "Unknown_") + camelcase(name)

    def formatted_element_name(self, el_or_elname: Union[ElementName, Element],
                               is_range_name: bool = False) -> Optional[str]:
        """
        Return the default format for the name or the referenced element.  Slots are under_scored, all others are
        CamelCased. Slot names are the alias, not the actual name

        :param el_or_elname: element or name to map
        :param is_range_name: True means that we're looking for a class or type.  False means Slot or Subset. Only
        applies if el_or_elname is an ElementName (otherwise we know what we've got
        :return: Formatted name if type can be known else None
        """
        if isinstance(el_or_elname, str):
            if is_range_name:
                return self.class_or_type_name(el_or_elname) \
                    if el_or_elname in self.schema.classes or \
                       el_or_elname in self.schema.types or \
                       el_or_elname == self.schema.default_range else None
            elif el_or_elname in self.schema.slots:
                return self.slot_name(cast(SlotDefinitionName, el_or_elname))
            elif el_or_elname in self.schema.subsets:
                return self.subset_name(el_or_elname)
            return None
        elif isinstance(el_or_elname, (ClassDefinition, TypeDefinition)):
            return self.class_or_type_name(el_or_elname.name)
        elif isinstance(el_or_elname, SlotDefinition):
            return self.slot_name(el_or_elname.name)
        elif isinstance(el_or_elname, SubsetDefinition):
            return self.subset_name(el_or_elname.name)
        else:
            return None

    def default_prefix(self) -> Optional[str]:
        """ Return the default prefix for the schema

         @return: URI or NCNAME of default prefix """
        if '://' in self.schema.default_prefix:
            return self.schema.default_prefix
        else:
            # Basic loader tests for valid default prefix
            return self.schema.prefixes[PrefixPrefixPrefix(self.schema.default_prefix)].prefix_reference

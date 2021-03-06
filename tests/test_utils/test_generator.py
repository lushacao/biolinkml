import os
import unittest
from contextlib import redirect_stderr
from io import StringIO
from pprint import pprint
from typing import Union, TextIO

from biolinkml import LOCAL_YAML_PATH
from biolinkml.meta import SchemaDefinition, ClassDefinition, SlotDefinition, TypeDefinition, SubsetDefinition
from biolinkml.utils.generator import Generator
from biolinkml.utils.typereferences import References
from tests.test_utils import datadir


class GeneratorTest(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.1"
    valid_formats = ['txt']

    visit_all_class_slots: bool = True
    visits_are_sorted: bool = False
    sort_class_slots: bool = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str = 'txt', emit_metadata: bool = False) \
            -> None:
        self.visited = []
        self.visit_class_return = True
        self.visit_all_class_slots: bool = True
        self.visits_are_sorted: bool = False
        self.sort_class_slots: bool = False
        super().__init__(schema, fmt, emit_metadata)

    def visit_schema(self, **kwargs) -> None:
        self.visited = ['init']
        self.visited.append(f'schema: {self.schema.name}')

    def end_schema(self, **kwargs) -> None:
        self.visited.append(f'end_schema: {self.schema.name}')
        pprint(self.visited)

    def visit_class(self, cls: ClassDefinition) -> bool:
        self.visited.append(f"class: {cls.name}")
        return self.visit_class_return

    def end_class(self, cls: ClassDefinition) -> None:
        self.visited.append(f"end_class: {cls.name}")

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        self.visited.append(f"  slot: {slot.name}" +
                            (f" ({aliased_slot_name})" if slot.name != aliased_slot_name else ''))

    def visit_slot(self, aliased_slot_name: str, slot: SlotDefinition) -> None:
        self.visited.append(f"slot: {slot.name}" +
                            (f" ({aliased_slot_name})" if slot.name != aliased_slot_name else ''))

    def visit_type(self, typ: TypeDefinition) -> None:
        self.visited.append(f"type: {typ.name}")

    def visit_subset(self, subset: SubsetDefinition) -> None:
        self.visited.append(f"subset: {subset.name}")

# visit_all_class_slots = True, visits_are_sorted = False, sort_class_slots = False
expected1 = [
     'init',
     'schema: generator1',
     'subset: ss2',
     'subset: ss1',
     'type: t2',
     'type: t1',
     'slot: slot1',
     'slot: slot2',
     'slot: mixin slot 1',
     'slot: mixin slot 2',
     'slot: mixin slot 3',
     'slot: applyto slot 1',
     'slot: applyto slot 2',
     'slot: c2_slot1 (slot1)',
     'slot: c3_applyto slot 2 (applyto slot 2)',
     'slot: c3_slot1 (slot1)',
     'class: c1',
     '  slot: slot1',
     '  slot: slot2',
     '  slot: mixin slot 1',
     '  slot: mixin slot 2',
     '  slot: mixin slot 3',
     'end_class: c1',
     'class: c2',
     '  slot: c2_slot1 (slot1)',
     '  slot: slot2',
     '  slot: mixin slot 1',
     '  slot: mixin slot 2',
     '  slot: mixin slot 3',
     '  slot: applyto slot 1',
     '  slot: applyto slot 2',
     'end_class: c2',
     'class: c3',
     '  slot: c3_slot1 (slot1)',
     '  slot: slot2',
     '  slot: mixin slot 1',
     '  slot: mixin slot 2',
     '  slot: mixin slot 3',
     '  slot: applyto slot 1',
     '  slot: c3_applyto slot 2 (applyto slot 2)',
     'end_class: c3',
     'class: c4',
     '  slot: applyto slot 1',
     '  slot: applyto slot 2',
     'end_class: c4',
     'class: mixin1',
     '  slot: mixin slot 1',
     '  slot: mixin slot 2',
     'end_class: mixin1',
     'class: mixin2',
     '  slot: mixin slot 3',
     'end_class: mixin2',
     'class: applyto1',
     '  slot: applyto slot 1',
     '  slot: applyto slot 2',
     'end_class: applyto1',
     'end_schema: generator1']

# visit_all_class_slots = False, visits_are_sorted = False, sort_class_slots = False
expected2 = [
    'init',
    'schema: generator1',
    'subset: ss2',
    'subset: ss1',
    'type: t2',
    'type: t1',
    'slot: slot1',
    'slot: slot2',
    'slot: mixin slot 1',
    'slot: mixin slot 2',
    'slot: mixin slot 3',
    'slot: applyto slot 1',
    'slot: applyto slot 2',
    'slot: c2_slot1 (slot1)',
    'slot: c3_applyto slot 2 (applyto slot 2)',
    'slot: c3_slot1 (slot1)',
    'class: c1',
    '  slot: slot1',
    '  slot: slot2',
    '  slot: mixin slot 1',
    '  slot: mixin slot 2',
    '  slot: mixin slot 3',
    'end_class: c1',
    'class: c2',
    '  slot: c2_slot1 (slot1)',
    '  slot: applyto slot 1',
    '  slot: applyto slot 2',
    'end_class: c2',
    'class: c3',
    '  slot: c3_slot1 (slot1)',
    '  slot: c3_applyto slot 2 (applyto slot 2)',
    'end_class: c3',
    'class: c4',
    '  slot: applyto slot 1',
    '  slot: applyto slot 2',
    'end_class: c4',
    'class: mixin1',
    '  slot: mixin slot 1',
    '  slot: mixin slot 2',
    'end_class: mixin1',
    'class: mixin2',
    '  slot: mixin slot 3',
    'end_class: mixin2',
    'class: applyto1',
    '  slot: applyto slot 1',
    '  slot: applyto slot 2',
    'end_class: applyto1',
    'end_schema: generator1']

# visit_all_class_slots = True, visits_are_sorted = True, sort_class_slots = False
expected3 = [
    'init',
    'schema: generator1',
    'subset: ss1',
    'subset: ss2',
    'type: t1',
    'type: t2',
    'slot: applyto slot 1',
    'slot: applyto slot 2',
    'slot: c2_slot1 (slot1)',
    'slot: c3_applyto slot 2 (applyto slot 2)',
    'slot: c3_slot1 (slot1)',
    'slot: mixin slot 1',
    'slot: mixin slot 2',
    'slot: mixin slot 3',
    'slot: slot1',
    'slot: slot2',
    'class: applyto1',
    '  slot: applyto slot 1',
    '  slot: applyto slot 2',
    'end_class: applyto1',
    'class: c1',
    '  slot: slot1',
    '  slot: slot2',
    '  slot: mixin slot 1',
    '  slot: mixin slot 2',
    '  slot: mixin slot 3',
    'end_class: c1',
    'class: c2',
    '  slot: c2_slot1 (slot1)',
    '  slot: slot2',
    '  slot: mixin slot 1',
    '  slot: mixin slot 2',
    '  slot: mixin slot 3',
    '  slot: applyto slot 1',
    '  slot: applyto slot 2',
    'end_class: c2',
    'class: c3',
    '  slot: c3_slot1 (slot1)',
    '  slot: slot2',
    '  slot: mixin slot 1',
    '  slot: mixin slot 2',
    '  slot: mixin slot 3',
    '  slot: applyto slot 1',
    '  slot: c3_applyto slot 2 (applyto slot 2)',
    'end_class: c3',
    'class: c4',
    '  slot: applyto slot 1',
    '  slot: applyto slot 2',
    'end_class: c4',
    'class: mixin1',
    '  slot: mixin slot 1',
    '  slot: mixin slot 2',
    'end_class: mixin1',
    'class: mixin2',
    '  slot: mixin slot 3',
    'end_class: mixin2',
    'end_schema: generator1']

# visit_all_class_slots = True, visits_are_sorted = False, sort_class_slots = True
expected4 = [
    'init',
    'schema: generator1',
    'subset: ss2',
    'subset: ss1',
    'type: t2',
    'type: t1',
    'slot: slot1',
    'slot: slot2',
    'slot: mixin slot 1',
    'slot: mixin slot 2',
    'slot: mixin slot 3',
    'slot: applyto slot 1',
    'slot: applyto slot 2',
    'slot: c2_slot1 (slot1)',
    'slot: c3_applyto slot 2 (applyto slot 2)',
    'slot: c3_slot1 (slot1)',
    'class: c1',
    '  slot: mixin slot 1',
    '  slot: mixin slot 2',
    '  slot: mixin slot 3',
    '  slot: slot1',
    '  slot: slot2',
    'end_class: c1',
    'class: c2',
    '  slot: applyto slot 1',
    '  slot: applyto slot 2',
    '  slot: c2_slot1 (slot1)',
    '  slot: mixin slot 1',
    '  slot: mixin slot 2',
    '  slot: mixin slot 3',
    '  slot: slot2',
    'end_class: c2',
    'class: c3',
    '  slot: applyto slot 1',
    '  slot: c3_applyto slot 2 (applyto slot 2)',
    '  slot: c3_slot1 (slot1)',
    '  slot: mixin slot 1',
    '  slot: mixin slot 2',
    '  slot: mixin slot 3',
    '  slot: slot2',
    'end_class: c3',
    'class: c4',
    '  slot: applyto slot 1',
    '  slot: applyto slot 2',
    'end_class: c4',
    'class: mixin1',
    '  slot: mixin slot 1',
    '  slot: mixin slot 2',
    'end_class: mixin1',
    'class: mixin2',
    '  slot: mixin slot 3',
    'end_class: mixin2',
    'class: applyto1',
    '  slot: applyto slot 1',
    '  slot: applyto slot 2',
    'end_class: applyto1',
    'end_schema: generator1']

expected5 = [
    'init',
    'schema: generator1',
    'subset: ss2',
    'subset: ss1',
    'type: t2',
    'type: t1',
    'slot: slot1',
    'slot: slot2',
    'slot: mixin slot 1',
    'slot: mixin slot 2',
    'slot: mixin slot 3',
    'slot: applyto slot 1',
    'slot: applyto slot 2',
    'slot: c2_slot1 (slot1)',
    'slot: c3_applyto slot 2 (applyto slot 2)',
    'slot: c3_slot1 (slot1)',
    'class: c1',
    'class: c2',
    'class: c3',
    'class: c4',
    'class: mixin1',
    'class: mixin2',
    'class: applyto1',
    'end_schema: generator1']


class GeneratorTestCase(unittest.TestCase):
    def test_visitors(self):
        """ Test the generator visitor functions """
        gen = GeneratorTest(os.path.join(datadir, 'generator1.yaml'))
        gen.serialize()
        self.assertEqual(expected1, gen.visited)
        gen.visit_all_class_slots = False
        gen.serialize()
        self.assertEqual(expected2, gen.visited)
        gen.visit_all_class_slots = True
        gen.visits_are_sorted = True
        gen.serialize()
        self.assertEqual(expected3, gen.visited)
        gen.visits_are_sorted = False
        gen.sort_class_slots = True
        gen.serialize()
        self.assertEqual(expected4, gen.visited)
        gen.sort_class_slots = False
        gen.visit_class_return = False
        gen.serialize()
        self.assertEqual(expected5, gen.visited)

    def test_default_prefix(self):
        """ Test default prefix utility """
        model = """
id: http://example.org/test/t1
name: t1

default_range: string
types:
    string:
        base: str
        uri: xsd:string

prefixes:
    xsd: http://www.w3.org/2001/XMLSchema#
    AAA: http://example.org/test/aaa/
    BBB: http://example.org/test/bbb/
"""
        gen = GeneratorTest(model + "\n\ndefault_prefix: AAA")
        self.assertEqual("http://example.org/test/aaa/", gen.default_prefix())

        gen = GeneratorTest(model + "\n\ndefault_prefix: http://example.org/test/default/")
        self.assertEqual("http://example.org/test/default/", gen.default_prefix())

        with self.assertRaises(ValueError):
            GeneratorTest(model + "\n\ndefault_prefix: CCCC")

    def test_duplicate_names(self):
        """ Test duplicate name for slot and type detection """
        model = """
id: http://example.org/test/t1
name: t1
default_range: string

types:
    string:
        base: str
        
    dup name:
        base: int
        
    dn2:

        
classes:
    dn2:
    
    dup name:
"""
        errfile = StringIO()
        with self.assertRaises(ValueError):
            gen = GeneratorTest(model)

    def test_element_name(self):
        """ Test formatted_element_name """
        model = """
id: http://example.org/test/t1
name: t1

prefixes:
    xsd: http://www.w3.org/2001/XMLSchema#

subsets:
    dup name:
    subset ss1:

default_range: dup name

types:
    str:
        base: str
        uri: xsd:string
    dup name:
        base: int
        uri: xsd:integer
    type t1:
        base: int
        uri: xsd:integer
    
        
slots:
    dup name:
        domain: class c1
        
classes:
    class c1:
"""
        errfile = StringIO()
        with redirect_stderr(errfile):
            gen = GeneratorTest(model)
        self.assertEqual("""Warning: Shared type and slot names: dup name
Warning: Shared slot and subset names: dup name
Warning: Shared type and subset names: dup name""", errfile.getvalue().strip())

        self.assertEqual('dup_name', gen.formatted_element_name('dup name', False))
        self.assertEqual('int', gen.formatted_element_name('dup name', True))
        self.assertEqual('str', gen.formatted_element_name('str', True))
        self.assertIsNone(gen.formatted_element_name('class c1', False))
        self.assertEqual('ClassC1', gen.formatted_element_name('class c1', True))
        self.assertEqual('SubsetSs1', gen.formatted_element_name('subset ss1', False))
        self.assertEqual("Unknown_ClassC2", gen.class_or_type_name('class c2'))
        self.assertEqual("int", gen.class_or_type_name('dup name'))
        self.assertEqual("int", gen.class_or_type_name('type t1'))
        self.assertEqual("unknown_slot_s2", gen.slot_name('slot s2'))
        self.assertEqual('Unknown_SS', gen.subset_name('s s'))

        self.assertEqual('dup_name', gen.formatted_element_name(gen.schema.slots['dup name']))
        self.assertEqual('int', gen.formatted_element_name(gen.schema.types['dup name']))
        self.assertEqual('DupName', gen.formatted_element_name(gen.schema.subsets['dup name']))
        self.assertEqual('ClassC1', gen.formatted_element_name(gen.schema.classes['class c1']))
        self.assertIsNone(gen.formatted_element_name(gen))

    def test_own_slots(self):
        """ Test the generator own_slots and all_slots helper functions """
        gen = GeneratorTest(os.path.join(datadir, 'ownalltest.yaml'))
        gen.sort_class_slots = True

        self.assertEqual(['s6'], [s.name for s in gen.own_slots('at1')])
        self.assertEqual(['s6'], [s.name for s in gen.all_slots('at1')])
        self.assertEqual(['s6'], [s.name for s in gen.all_slots('at1', cls_slots_first=True)])

        self.assertEqual(['s5', 's6'], [s.name for s in gen.own_slots('m2')])
        self.assertEqual(['s5', 's6'], [s.name for s in gen.all_slots('m2')])
        self.assertEqual(['s5', 's6'], [s.name for s in gen.all_slots('m2', cls_slots_first=True)])

        self.assertEqual(['s4'], [s.name for s in gen.own_slots('m1')])
        self.assertEqual(['s4'], [s.name for s in gen.all_slots('m1')])
        self.assertEqual(['s4'], [s.name for s in gen.all_slots('m1', cls_slots_first=True)])

        self.assertEqual(['s1', 's3'], [s.name for s in gen.own_slots('c1')])
        self.assertEqual(['s1', 's3'], [s.name for s in gen.all_slots('c1')])
        self.assertEqual(['s1', 's3'], [s.name for s in gen.all_slots('c1', cls_slots_first=True)])

        self.assertEqual(['s2', 's4'], [s.name for s in gen.own_slots('c2')])
        self.assertEqual(['s1', 's2', 's3', 's4'], [s.name for s in gen.all_slots('c2')])
        self.assertEqual(['s2', 's4', 's1', 's3'], [s.name for s in gen.all_slots('c2', cls_slots_first=True)])

        self.assertEqual(['s5', 's6'], [s.name for s in gen.own_slots('c3')])
        self.assertEqual(['s1', 's2', 's3', 's4', 's5', 's6'], [s.name for s in gen.all_slots('c3')])
        self.assertEqual(['s5', 's6', 's2', 's4', 's1', 's3'],
                         [s.name for s in gen.all_slots('c3', cls_slots_first=True)])
        
        self.assertEqual(['c4_s1', 'c4_s5', 'c4_s6'], [s.name for s in gen.own_slots('c4')])
        self.assertEqual(['c4_s1', 'c4_s5', 'c4_s6', 's2', 's3', 's4'], [s.name for s in gen.all_slots('c4')])
        self.assertEqual(['c4_s1', 'c4_s5', 'c4_s6', 's2', 's4', 's3'],
                         [s.name for s in gen.all_slots('c4', cls_slots_first=True)])
        
        self.assertEqual(['c5_s1', 'c5_s6'], [s.name for s in gen.own_slots('c5')])
        self.assertEqual(['c4_s5', 'c5_s1', 'c5_s6', 's2', 's3', 's4'], [s.name for s in gen.all_slots('c5')])
        self.assertEqual(['c5_s1', 'c5_s6', 'c4_s5', 's2', 's4', 's3'],
                         [s.name for s in gen.all_slots('c5', cls_slots_first=True)])

    def test_slot_class_paths(self):
        """ Test for aliased slot name, class identifier path and slot type path """
        gen = GeneratorTest(os.path.join(datadir, 'ownalltest.yaml'))
        gen.sort_class_slots = True
        self.assertEqual(['s1', 's5', 's6', 's2', 's3', 's4'],
                         [gen.aliased_slot_name(s.name) for s in gen.all_slots('c4')])
        self.assertEqual(['s5', 's1', 's6', 's2', 's3', 's4'],
                         [gen.aliased_slot_name(s) for s in gen.all_slots('c5')])
        self.assertEqual({
            'c4_s1': ['int'],
            'c4_s5': ['Bool', 'T5'],
            'c4_s6': ['int', 'C1S1', 'C2S1', 'C3S1', 'C4S1'],
            's2': ['int', 'C1S1'],
            's3': ['int', 'T2', 'T3'],
            's4': ['Bool']} , {s.name: gen.slot_type_path(s) for s in gen.all_slots('c4')})
        self.assertEqual({
            'c4_s5': ['Bool', 'T5'],
            'c5_s1': ['int'],
            'c5_s6': ['str'],
            's2': ['int', 'C1S1'],
            's3': ['int', 'T2', 'T3'],
            's4': ['Bool']} , {s.name: gen.slot_type_path(s) for s in gen.all_slots('c5')})
        self.assertEqual({'s1': ['int'], 's3': ['int', 'T2', 'T3']},
                         {s.name: gen.slot_type_path(s) for s in gen.all_slots('c1')})

    def test_ancestors(self):
        """ Test ancestors function and duplicate name detection """
        model = """
id: http://example.org/test/t1
name: t1

prefixes:
  xsd: http://www.w3.org/2001/XMLSchema#

default_range: string

types:
    string:
        base: str
        uri: xsd:string

slots:
    slot s1:
        domain: class c2

    slot s2:
        is_a: slot s1
        
    slot s3:
        is_a: slot s2
        
    slot s4:
        is_a: slot s2
        
classes:
    slot s1:
    
    class c2:
        is_a: slot s1
"""
        errfile = StringIO()
        with redirect_stderr(errfile):
            gen = GeneratorTest(model)
        self.assertEqual("Warning: Shared class and slot names: slot s1", errfile.getvalue().strip())

        self.assertEqual(['slot s1'], gen.ancestors(gen.schema.slots['slot s1']))
        self.assertEqual(['slot s2', 'slot s1'], gen.ancestors(gen.schema.slots['slot s2']))
        self.assertEqual(['slot s3', 'slot s2', 'slot s1'], gen.ancestors(gen.schema.slots['slot s3']))
        self.assertEqual(['slot s4', 'slot s2', 'slot s1'], gen.ancestors(gen.schema.slots['slot s4']))
        self.assertEqual(['slot s1'], gen.ancestors(gen.schema.classes['slot s1']))
        self.assertEqual(['class c2', 'slot s1'], gen.ancestors(gen.schema.classes['class c2']))



    def test_range_type_path(self):
        model = """
id: http://example.org/test/t1
name: t1

prefixes:
  xsd: http://www.w3.org/2001/XMLSchema#

default_range: type 1
types:
    type 1:
        base: int
        uri: xsd:integer
        
    type 2:
        typeof: type 1
        
    type 3:
        typeof: type 2
"""
        gen = GeneratorTest(model)
        self.assertEqual(['int'], gen.range_type_path(gen.schema.types['type 1']))
        self.assertEqual(['int', 'Type2'], gen.range_type_path(gen.schema.types['type 2']))
        self.assertEqual(['int', 'Type2', 'Type3'], gen.range_type_path(gen.schema.types['type 3']))

    def test_identifier_path(self):
        """ Test the case of an implicitly inlined class """
        model = """
id: http://example.org/test/t1
name: t1

prefixes:
    xsd: http://www.w3.org/2001/XMLSchema#
    
types:
    string:
        base: str
        uri: xsd:string
        
slots:
    s1:
        domain: c1
        range: c2
        
    s2:
        domain: c2
        range: string
        
classes:
    c1:
    c2:

"""
        gen = GeneratorTest(model)
        self.assertEqual({'s1': ['dict', 'C2'], 's2': ['str']},
                         {s.name: gen.slot_type_path(s) for s in gen.schema.slots.values()})

    def test_meta_neighborhood(self):
        """ Test the neighborhood function in the metamodel """
        gen = GeneratorTest(LOCAL_YAML_PATH)
        errfile = StringIO()
        with redirect_stderr(errfile):
            gen.neighborhood(['Definition'])
        self.assertEqual("Warning: neighborhood(Definition) - Definition is undefined", errfile.getvalue().strip())
        self.assertEqual(References(
            classrefs={'class_definition', 'local_name', 'schema_definition', 'subset_definition', 'alt_description',
                       'definition', 'example', 'slot_definition', 'element'},
            slotrefs={'is_a', 'apply_to', 'mixins', 'default_range'},
            typerefs={'uriorcurie', 'boolean', 'uri', 'ncname', 'string'},
            subsetrefs=set()), gen.neighborhood('definition'))


if __name__ == '__main__':
    unittest.main()

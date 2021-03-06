# Class: class_definition


the definition of a class or interface

URI: [meta:ClassDefinition](https://w3id.org/biolink/biolinkml/meta/ClassDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SubsetDefinition]<in_subset(i)%200..*-%20\[ClassDefinition|class_uri:uriorcurie%20%3F;subclass_of:uriorcurie%20%3F;abstract(i):boolean%20%3F;mixin(i):boolean%20%3F;values_from(i):uriorcurie%20*;id_prefixes(i):ncname%20*;name(pk)(i):string;aliases(i):string%20*;mappings(i):uriorcurie%20*;description(i):string%20%3F;deprecated(i):string%20%3F;todos(i):string%20*;notes(i):string%20*;comments(i):string%20*;from_schema(i):uri%20%3F;imported_from(i):string%20%3F;see_also(i):uriorcurie%20*],%20\[Example]<examples(i)%200..*-++\[ClassDefinition],%20\[AltDescription]<alt_descriptions(i)%200..*-++\[ClassDefinition],%20\[LocalName]<local_names(i)%200..*-++\[ClassDefinition],%20\[SlotDefinition]<defining_slots%200..*-%20\[ClassDefinition],%20\[SlotDefinition]<slot_usage%200..*-++\[ClassDefinition],%20\[SlotDefinition]<slots%200..*-%20\[ClassDefinition],%20\[ClassDefinition]<apply_to%200..*-%20\[ClassDefinition],%20\[ClassDefinition]<mixins%200..*-%20\[ClassDefinition],%20\[ClassDefinition]<is_a%200..1-%20\[ClassDefinition],%20\[SchemaDefinition]++-%20classes%200..*>\[ClassDefinition],%20\[SlotDefinition]-%20domain%201..1>\[ClassDefinition],%20\[Definition]^-\[ClassDefinition])
## Inheritance

 *  is_a: [Definition](Definition.md) - base class for definitions
## Children

## Used by

 *  **[ClassDefinition](ClassDefinition.md)** *[class_definition.apply_to](class_definition_apply_to.md)*  <sub>0..*</sub>  **[ClassDefinition](ClassDefinition.md)**
 *  **[ClassDefinition](ClassDefinition.md)** *[class_definition.is_a](class_definition_is_a.md)*  <sub>OPT</sub>  **[ClassDefinition](ClassDefinition.md)**
 *  **[ClassDefinition](ClassDefinition.md)** *[class_definition.mixins](class_definition_mixins.md)*  <sub>0..*</sub>  **[ClassDefinition](ClassDefinition.md)**
 *  **[SchemaDefinition](SchemaDefinition.md)** *[classes](classes.md)*  <sub>0..*</sub>  **[ClassDefinition](ClassDefinition.md)**
 *  **[SlotDefinition](SlotDefinition.md)** *[domain](domain.md)*  <sub>REQ</sub>  **[ClassDefinition](ClassDefinition.md)**
## Fields

 * [abstract](abstract.md)  <sub>OPT</sub>
    * Description: an abstract class is a high level class or slot that is typically used to group common slots together and cannot be directly instantiated.
    * range: [Boolean](Boolean.md)
    * inherited from: [Definition](Definition.md)
 * [aliases](aliases.md)  <sub>0..*</sub>
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [alt_descriptions](alt_descriptions.md)  <sub>0..*</sub>
    * range: [AltDescription](AltDescription.md)
    * inherited from: [Element](Element.md)
 * [class_definition.apply_to](class_definition_apply_to.md)  <sub>0..*</sub>
    * range: [ClassDefinition](ClassDefinition.md)
 * [class_definition.is_a](class_definition_is_a.md)  <sub>OPT</sub>
    * range: [ClassDefinition](ClassDefinition.md)
 * [class_definition.mixins](class_definition_mixins.md)  <sub>0..*</sub>
    * range: [ClassDefinition](ClassDefinition.md)
 * [class_uri](class_uri.md)  <sub>OPT</sub>
    * Description: URI of the class in an RDF environment
    * range: [Uriorcurie](Uriorcurie.md)
 * [comments](comments.md)  <sub>0..*</sub>
    * Description: notes and comments about an element intended for external consumption
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [defining_slots](defining_slots.md)  <sub>0..*</sub>
    * Description: The combination of is a plus defining slots form a genus-differentia definition, or the set of necessary and sufficient conditions that can be transformed into an OWL equivalence axiom
    * range: [SlotDefinition](SlotDefinition.md)
 * [deprecated](deprecated.md)  <sub>OPT</sub>
    * Description: Description of why and when this element will no longer be used
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a description of the element's purpose and use
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [examples](examples.md)  <sub>0..*</sub>
    * Description: example usages of an element
    * range: [Example](Example.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [from_schema](from_schema.md)  <sub>OPT</sub>
    * Description: id of the schema that defined the element
    * range: [Uri](Uri.md)
    * inherited from: [Element](Element.md)
 * [id_prefixes](id_prefixes.md)  <sub>0..*</sub>
    * Description: the identifier of this class or slot must begin with one of the URIs referenced by this prefix
    * range: [Ncname](Ncname.md)
    * inherited from: [Element](Element.md)
 * [imported_from](imported_from.md)  <sub>OPT</sub>
    * Description: the imports entry that this element was derived from.  Empty means primary source
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [in_subset](in_subset.md)  <sub>0..*</sub>
    * Description: used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
    * range: [SubsetDefinition](SubsetDefinition.md)
    * inherited from: [Element](Element.md)
 * [local_names](local_names.md)  <sub>0..*</sub>
    * range: [LocalName](LocalName.md)
    * inherited from: [Element](Element.md)
 * [mappings](mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.
    * range: [Uriorcurie](Uriorcurie.md)
    * inherited from: [Element](Element.md)
 * [mixin](mixin.md)  <sub>OPT</sub>
    * Description: this slot or class can only be used as a mixin -- equivalent to abstract
    * range: [Boolean](Boolean.md)
    * inherited from: [Definition](Definition.md)
 * [name](name.md)  <sub>REQ</sub>
    * Description: the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [notes](notes.md)  <sub>0..*</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [see_also](see_also.md)  <sub>0..*</sub>
    * Description: a reference
    * range: [Uriorcurie](Uriorcurie.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [slot_usage](slot_usage.md)  <sub>0..*</sub>
    * Description: the redefinition of a slot in the context of the containing class definition.
    * range: [SlotDefinition](SlotDefinition.md)
 * [slots](slots.md)  <sub>0..*</sub>
    * Description: list of slot names that are applicable to a class
    * range: [SlotDefinition](SlotDefinition.md)
 * [subclass_of](subclass_of.md)  <sub>OPT</sub>
    * Description: rdfs:subClassOf to be emitted in OWL generation
    * range: [Uriorcurie](Uriorcurie.md)
 * [todos](todos.md)  <sub>0..*</sub>
    * Description: Outstanding issue that needs resolution
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [values_from](values_from.md)  <sub>0..*</sub>
    * Description: the identifier of a "value set" -- a set of identifiers that form the possible values for the range of a slot
    * range: [Uriorcurie](Uriorcurie.md)
    * inherited from: [Definition](Definition.md)

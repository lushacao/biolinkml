# Class: prefix


prefix URI tuple

URI: [meta:Prefix](https://w3id.org/biolink/biolinkml/meta/Prefix)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SchemaDefinition]++-%20prefixes%200..*>\[Prefix|prefix_prefix(pk):ncname;prefix_reference:uri])
## Inheritance

## Children

## Used by

 *  **[SchemaDefinition](SchemaDefinition.md)** *[prefixes](prefixes.md)*  <sub>0..*</sub>  **[Prefix](Prefix.md)**
## Fields

 * [prefix_prefix](prefix_prefix.md)  <sub>REQ</sub>
    * Description: the nsname (sans ':' for a given prefix)
    * range: [Ncname](Ncname.md)
 * [prefix_reference](prefix_reference.md)  <sub>REQ</sub>
    * Description: A URI associated with a given prefix
    * range: [Uri](Uri.md)

# Class: cell line to disease or phenotypic feature association


An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype

URI: [https://biolink.github.io/biolink-model/ontology/biolink.ttl/CellLineToDiseaseOrPhenotypicFeatureAssociation](https://biolink.github.io/biolink-model/ontology/biolink.ttl/CellLineToDiseaseOrPhenotypicFeatureAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[CellLineToDiseaseOrPhenotypicFeatureAssociation|id(i):identifier_type;relation(i):iri_type;object(i):iri_type;negated(i):boolean%20%3F;association_slot(i):string%20%3F],%20\[Publication]<publications(i)%200..*-%20\[CellLineToDiseaseOrPhenotypicFeatureAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[CellLineToDiseaseOrPhenotypicFeatureAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[CellLineToDiseaseOrPhenotypicFeatureAssociation],%20\[DiseaseOrPhenotypicFeature]<subject%201..1-%20\[CellLineToDiseaseOrPhenotypicFeatureAssociation],%20\[CellLineToDiseaseOrPhenotypicFeatureAssociation]uses%20-.->\[CellLineToThingAssociation],%20\[CellLineToDiseaseOrPhenotypicFeatureAssociation]uses%20-.->\[ThingToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[CellLineToDiseaseOrPhenotypicFeatureAssociation])
## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
 *  mixin: [CellLineToThingAssociation](CellLineToThingAssociation.md) - An relationship between a cell line and another entity
 *  mixin: [ThingToDiseaseOrPhenotypicFeatureAssociation](ThingToDiseaseOrPhenotypicFeatureAssociation.md)
## Children

## Used by

## Fields

 * [association slot](association_slot.md)  <sub>OPT</sub>
    * Description: any slot that relates an association to another entity
    * range: [String](String.md)
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [association.id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [Association](Association.md)
    * in subsets: (translator_minimal)
 * [cell line to disease or phenotypic feature association.subject](cell_line_to_disease_or_phenotypic_feature_association_subject.md)  <sub>REQ</sub>
    * range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](Boolean.md)
    * inherited from: [Association](Association.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [IriType](IriType.md)
    * inherited from: [Association](Association.md)
 * [provided by](provided_by.md)  <sub>OPT</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [IriType](IriType.md)
    * inherited from: [Association](Association.md)
# Class: gene




URI: [https://biolink.github.io/biolink-model/ontology/biolink.ttl/Gene](https://biolink.github.io/biolink-model/ontology/biolink.ttl/Gene)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing]<interacts%20with(i)%200..*-%20\[Gene|name(i):symbol_type%20%3F;has_biological_sequence(i):biological_sequence%20%3F;id(i):identifier_type;category(i):iri_type%20*;node_property(i):string%20%3F;iri(i):iri_type%20%3F;synonym(i):label_type%20*;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F],%20\[NamedThing]<related%20to(i)%200..*-%20\[Gene],%20\[PhenotypicFeature]<has%20phenotype(i)%200..*-%20\[Gene],%20\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[Gene],%20\[DiseaseOrPhenotypicFeature]<biomarker%20for(i)%200..*-%20\[Gene],%20\[MolecularEntity]<regulates,%20entity%20to%20entity(i)%200..*-%20\[Gene],%20\[MolecularEntity]<decreases%20uptake%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<increases%20uptake%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<affects%20uptake%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<decreases%20secretion%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<increases%20secretion%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<affects%20secretion%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<decreases%20transport%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<increases%20transport%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<affects%20transport%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<decreases%20stability%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<increases%20stability%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<affects%20stability%20of(i)%200..*-%20\[Gene],%20\[Transcript]<decreases%20splicing%20of(i)%200..*-%20\[Gene],%20\[Transcript]<increases%20splicing%20of(i)%200..*-%20\[Gene],%20\[Transcript]<affects%20splicing%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<decreases%20response%20to(i)%200..*-%20\[Gene],%20\[MolecularEntity]<increases%20response%20to(i)%200..*-%20\[Gene],%20\[MolecularEntity]<affects%20response%20to(i)%200..*-%20\[Gene],%20\[GenomicEntity]<decreases%20mutation%20rate%20of(i)%200..*-%20\[Gene],%20\[GenomicEntity]<increases%20mutation%20rate%20of(i)%200..*-%20\[Gene],%20\[GenomicEntity]<affects%20mutation%20rate%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<decreases%20degradation%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<increases%20degradation%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<affects%20degradation%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<decreases%20synthesis%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<increases%20synthesis%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<affects%20synthesis%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<decreases%20molecular%20modification%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<increases%20molecular%20modification%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<affects%20molecular%20modification%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<decreases%20metabolic%20processing%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<increases%20metabolic%20processing%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<affects%20metabolic%20processing%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<decreases%20localization%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<increases%20localization%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<affects%20localization%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<decreases%20folding%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<increases%20folding%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<affects%20folding%20of(i)%200..*-%20\[Gene],%20\[GenomicEntity]<decreases%20expression%20of(i)%200..*-%20\[Gene],%20\[GenomicEntity]<increases%20expression%20of(i)%200..*-%20\[Gene],%20\[GenomicEntity]<affects%20expression%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<decreases%20activity%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<increases%20activity%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<affects%20activity%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<decreases%20abundance%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<increases%20abundance%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<affects%20abundance%20of(i)%200..*-%20\[Gene],%20\[MolecularEntity]<molecularly%20interacts%20with(i)%200..*-%20\[Gene],%20\[AnatomicalEntity]<expressed%20in(i)%200..*-%20\[Gene],%20\[GeneOrGeneProduct]<in%20cell%20population%20with(i)%200..*-%20\[Gene],%20\[GeneOrGeneProduct]<in%20complex%20with(i)%200..*-%20\[Gene],%20\[GeneOrGeneProduct]<in%20pathway%20with(i)%200..*-%20\[Gene],%20\[DiseaseOrPhenotypicFeature]<gene%20associated%20with%20condition%200..*-%20\[Gene],%20\[GeneProduct]<has%20gene%20product%200..*-%20\[Gene],%20\[Gene]<genetically%20interacts%20with%200..*-%20\[Gene],%20\[GeneToGeneProductRelationship]-%20subject%201..1>\[Gene],%20\[GenotypeToGeneAssociation]-%20object%201..1>\[Gene],%20\[SequenceVariant]-%20has%20gene(i)%200..1>\[Gene],%20\[SequenceVariant]-%20has%20gene%200..*>\[Gene],%20\[TranscriptToGeneRelationship]-%20object%201..1>\[Gene],%20\[GeneOrGeneProduct]^-\[Gene])
## Inheritance

 *  is_a: [GeneOrGeneProduct](GeneOrGeneProduct.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
## Children

## Used by

 *  **[GeneToGeneProductRelationship](GeneToGeneProductRelationship.md)** *[gene to gene product relationship.subject](gene_to_gene_product_relationship_subject.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**
 *  **[Gene](Gene.md)** *[genetically interacts with](genetically_interacts_with.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)** *[genotype to gene association.object](genotype_to_gene_association_object.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[has gene](has_gene.md)*  <sub>OPT</sub>  **[Gene](Gene.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[sequence variant.has gene](sequence_variant_has_gene.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[TranscriptToGeneRelationship](TranscriptToGeneRelationship.md)** *[transcript to gene relationship.object](transcript_to_gene_relationship_object.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**
## Fields

 * [affects abundance of](affects_abundance_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects activity of](affects_activity_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects degradation of](affects_degradation_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects expression of](affects_expression_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest
    * range: [GenomicEntity](GenomicEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects folding of](affects_folding_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects localization of](affects_localization_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects metabolic processing of](affects_metabolic_processing_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects molecular modification of](affects_molecular_modification_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects mutation rate of](affects_mutation_rate_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest
    * range: [GenomicEntity](GenomicEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects response to](affects_response_to.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects secretion of](affects_secretion_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects splicing of](affects_splicing_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA
    * range: [Transcript](Transcript.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects stability of](affects_stability_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects synthesis of](affects_synthesis_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects transport of](affects_transport_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects uptake of](affects_uptake_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [biomarker for](biomarker_for.md)  <sub>0..*</sub>
    * Description: holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
    * range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>0..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [decreases abundance of](decreases_abundance_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases activity of](decreases_activity_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases degradation of](decreases_degradation_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases expression of](decreases_expression_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest
    * range: [GenomicEntity](GenomicEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases folding of](decreases_folding_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases localization of](decreases_localization_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases metabolic processing of](decreases_metabolic_processing_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases molecular modification of](decreases_molecular_modification_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases mutation rate of](decreases_mutation_rate_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest
    * range: [GenomicEntity](GenomicEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases response to](decreases_response_to.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases secretion of](decreases_secretion_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases splicing of](decreases_splicing_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA
    * range: [Transcript](Transcript.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases stability of](decreases_stability_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases synthesis of](decreases_synthesis_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases transport of](decreases_transport_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases uptake of](decreases_uptake_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [expressed in](expressed_in.md)  <sub>0..*</sub>
    * Description: holds between a gene or gene product and an anatomical entity in which it is expressed
    * range: [AnatomicalEntity](AnatomicalEntity.md)
    * inherited from: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * in subsets: (translator_minimal)
 * [full name](full_name.md)  <sub>OPT</sub>
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [gene associated with condition](gene_associated_with_condition.md)  <sub>0..*</sub>
    * Description: holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
    * range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
    * in subsets: (translator_minimal)
 * [genetically interacts with](genetically_interacts_with.md)  <sub>0..*</sub>
    * Description: holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
    * range: [Gene](Gene.md)
    * in subsets: (translator_minimal)
 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](BiologicalSequence.md)
    * inherited from: [GenomicEntity](GenomicEntity.md)
 * [has gene product](has_gene_product.md)  <sub>0..*</sub>
    * Description: holds between a gene and a transcribed and/or translated product generated from it
    * range: [GeneProduct](GeneProduct.md)
    * in subsets: (translator_minimal)
 * [has phenotype](has_phenotype.md)  <sub>0..*</sub>
    * Description: holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature).
    * range: [PhenotypicFeature](PhenotypicFeature.md)
    * inherited from: [BiologicalEntity](BiologicalEntity.md)
    * in subsets: (translator_minimal)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [in cell population with](in_cell_population_with.md)  <sub>0..*</sub>
    * Description: holds between two genes or gene products that are expressed in the same cell type or population
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * inherited from: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * in subsets: (translator_minimal)
 * [in complex with](in_complex_with.md)  <sub>0..*</sub>
    * Description: holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * inherited from: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * in subsets: (translator_minimal)
 * [in pathway with](in_pathway_with.md)  <sub>0..*</sub>
    * Description: holds between two genes or gene products that are part of in the same biological pathway
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * inherited from: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * in subsets: (translator_minimal)
 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
    * in subsets: (translator_minimal)
 * [increases abundance of](increases_abundance_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases activity of](increases_activity_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases degradation of](increases_degradation_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases expression of](increases_expression_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest
    * range: [GenomicEntity](GenomicEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases folding of](increases_folding_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases localization of](increases_localization_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases metabolic processing of](increases_metabolic_processing_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases molecular modification of](increases_molecular_modification_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases mutation rate of](increases_mutation_rate_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest
    * range: [GenomicEntity](GenomicEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases response to](increases_response_to.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases secretion of](increases_secretion_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases splicing of](increases_splicing_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA
    * range: [Transcript](Transcript.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases stability of](increases_stability_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases synthesis of](increases_synthesis_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases transport of](increases_transport_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases uptake of](increases_uptake_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [interacts with](interacts_with.md)  <sub>0..*</sub>
    * Description: holds between any two entities that directly or indirectly interact with each other
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [macromolecular machine.name](macromolecular_machine_name.md)  <sub>OPT</sub>
    * range: [SymbolType](SymbolType.md)
    * inherited from: [MacromolecularMachine](MacromolecularMachine.md)
 * [molecularly interacts with](molecularly_interacts_with.md)  <sub>0..*</sub>
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [node property](node_property.md)  <sub>OPT</sub>
    * Description: A grouping for any property that holds between a node and a value
    * range: [String](String.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [regulates, entity to entity](regulates_entity_to_entity.md)  <sub>0..*</sub>
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [related to](related_to.md)  <sub>0..*</sub>
    * Description: A relationship that is asserted between two named things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [synonym](synonym.md)  <sub>0..*</sub>
    * Description: Alternate human-readable names for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [systematic synonym](systematic_synonym.md)  <sub>OPT</sub>
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
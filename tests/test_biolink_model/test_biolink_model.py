import os
import re
import unittest
from types import ModuleType
from typing import List

from pyshex import ShExEvaluator
from pyshex.shex_evaluator import EvaluationResult
from rdflib import Graph, Namespace, URIRef

from biolinkml import METAMODEL_NAMESPACE, LOCAL_SHEX_PATH, LOCAL_CONTEXT_PATH
from biolinkml.generators.csvgen import CsvGenerator
from biolinkml.generators.dotgen import DotGenerator
from biolinkml.generators.golrgen import GolrSchemaGenerator
from biolinkml.generators.graphqlgen import GraphqlGenerator
from biolinkml.generators.jsonldcontextgen import ContextGenerator
from biolinkml.generators.jsonldgen import JSONLDGenerator
from biolinkml.generators.jsonschemagen import JsonSchemaGenerator
from biolinkml.generators.markdowngen import MarkdownGenerator
from biolinkml.generators.owlgen import OwlSchemaGenerator
from biolinkml.generators.protogen import ProtoGenerator
from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.generators.rdfgen import RDFGenerator
from biolinkml.generators.shexgen import ShExGenerator
from tests.test_scripts.clicktestcase import metadata_filter
from tests.utils.generator_utils import GeneratorTestCase

BIOLINK_NS = Namespace("https://w3id.org/biolink/vocab/")

# ShEx validation of the biolink model takes a loooong time, so we only do it on rare occasions
DO_SHEX_VALIDATION = False


class CurrentBiolinkModelTestCase(GeneratorTestCase):
    cwd = os.path.abspath(os.path.dirname(__file__))

    source_path = os.path.join(cwd, 'source')
    target_path = os.path.join(cwd, 'target')
    model_path = os.path.join(cwd, 'yaml')
    model_name = 'biolink-model'

    def test_biolink_python(self):
        """ Test the python generator for the biolink model """
        self.single_file_generator('py', PythonGenerator, {'emit_metadata': True}, filtr=metadata_filter)

        # Make sure the python is valid
        with open(os.path.join(self.source_path, 'biolink-model.py')) as f:
            pydata = f.read()
        spec = compile(pydata, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)

    def test_biolink_markdown(self):
        """ Test the markdown generator for the biolink model """
        self.directory_generator('markdown', MarkdownGenerator)

    def test_biolink_tsv(self):
        """ Test the tsv generator for the biolink model """
        def filtr(s: str) -> str:
            return s.replace('\r\n', '\n')
        self.single_file_generator('tsv', CsvGenerator, {'fmt': 'tsv'}, filtr=filtr)

    def test_biolink_graphviz(self):
        """ Test the dotty generator for the biolink model """
        self.directory_generator('graphviz', DotGenerator)

    def test_biolink_golr(self):
        """ Test the golr schema generator for the biolink model """
        self.directory_generator('golr', GolrSchemaGenerator)

    def test_biolink_graphql(self):
        """ Test the graphql schema generator for the biolink model """
        self.single_file_generator('graphql', GraphqlGenerator)

    def test_biolink_jsonld(self):
        """ Test the jsonld schema generator for the biolink model """
        def filtr(s: str) -> str:
            return re.sub(r'"generation_date": ".*?",', '"generation_date": "2019-01-01 12:00",', s)
        self.single_file_generator('jsonld', JSONLDGenerator, filtr=filtr)

    def test_biolink_context(self):
        """ Test the jsonld context generator for the biolink model """
        def filtr(s: str) -> str:
            return re.sub(r'Generation date: .*?\\n', r'Generation date: \\n',
                          re.sub(r' version: .*?\\n', r' version: \\n', s))
        self.single_file_generator('context.jsonld', ContextGenerator, filtr=filtr)

    def test_biolink_json_schema(self):
        """ Test the jsonld context generator for the biolink model """
        self.single_file_generator('json.schema', JsonSchemaGenerator)

    def test_biolink_owl_schema(self):
        """ Test the owl schema generator for the biolink model """
        self.single_file_generator('owl', OwlSchemaGenerator, comparator=GeneratorTestCase.rdf_comparator)

    def test_biolink_proto(self):
        """ Test the proto schema generator for the biolink model """
        self.single_file_generator('proto', ProtoGenerator)

    @staticmethod
    def _evaluate_shex_results(results: List[EvaluationResult], printit: bool=True) -> bool:
        """
        Check the results of the ShEx evaluation
        :param results: evaluate output
        :return: success indicator
        """
        success = all(r.result for r in results)
        if not success and printit:
            for r in results:
                if not r.result:
                    print(r.reason)
        return success

    def test_biolink_rdf(self):
        """ Test the rdf generator for the biolink model """
        self.single_file_generator('ttl', RDFGenerator, serialize_args={"context": LOCAL_CONTEXT_PATH},
                                   comparator=GeneratorTestCase.rdf_comparator)

        # Validate the RDF against the Biolink ShEx
        if DO_SHEX_VALIDATION:
            g = Graph()
            rdf_file = os.path.join(self.source_path, 'biolink_model.ttl')
            g.load(rdf_file, format='ttl')
            focus = BIOLINK_NS.biolink_model
            start = METAMODEL_NAMESPACE.SchemaDefinition
            results = ShExEvaluator(g, LOCAL_SHEX_PATH, focus, start).evaluate(debug=False)
            self.assertTrue(self._evaluate_shex_results(results))

        else:
            print("*** RDF Model validation step was skipped. See: test_biolink_model.DO_SHEX_VALIDATION to run it")

    def test_biolink_shex_incorrect_rdf(self):
        """ Test some non-conforming RDF  """
        self.single_file_generator('shex', ShExGenerator)
        shex_file = os.path.join(self.source_path, 'biolink-model.shex')
        data_dir = os.path.join(self.cwd, 'data')

        focus = "http://identifiers.org/drugbank:DB00005"
        start = BIOLINK_NS.Drug
        evaluator = ShExEvaluator(None, shex_file, focus, start)

        # incorrect.ttl has 16 error lines (more or less).
        rdf_file = os.path.join(data_dir, 'incorrect.ttl')
        errs_file = os.path.join(data_dir, 'incorrect.errs')
        results = evaluator.evaluate(rdf_file)
        self.assertFalse(self._evaluate_shex_results(results, printit=False))
        self.assertEqual(1, len(results))
        self.assertTrue('Unmatched triples in CLOSED shape' in results[0].reason)
        ntabs = results[0].reason.count('\n\t')
        self.assertEqual(13, ntabs)
        if not os.path.exists(errs_file):
            with open(errs_file, 'w') as f:
                f.write(repr(results))

    @unittest.skipIf(True, "Awaiting fix to PyShEx permutation issue")
    def test_biolink_correct_rdf(self):
        """ Test some conforming RDF  """
        self.single_file_generator('shex', ShExGenerator)
        shex_file = os.path.join(self.source_path, 'biolink-model.shex')
        data_dir = os.path.join(self.cwd, 'data')

        focus = "http://identifiers.org/drugbank:DB00005"
        start = BIOLINK_NS.Drug
        evaluator = ShExEvaluator(None, shex_file, focus, start)

        rdf_file = os.path.join(data_dir, 'correct.ttl')
        results = evaluator.evaluate(rdf_file, debug=False)
        self.assertTrue(self._evaluate_shex_results(results))


    @unittest.skipIf(False, "Evaluation of performance test.")
    def test_probe(self):
        """ Test for determining performance problem """
        shex_file = os.path.join(self.source_path, 'probe.shex')
        data_dir = os.path.join(self.cwd, 'data')

        focus = "http://identifiers.org/drugbank:DB00005"
        start = BIOLINK_NS.Drug
        evaluator = ShExEvaluator(None, shex_file, focus, start)
        rdf_file = os.path.join(data_dir, 'probe.ttl')
        results = evaluator.evaluate(rdf_file, debug=False)
        self.assertTrue(self._evaluate_shex_results(results))


if __name__ == '__main__':
    unittest.main()

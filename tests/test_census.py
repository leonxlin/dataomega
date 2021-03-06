import unittest
import json
from civomega.modules.census_population import SimpleCensusParser, SexAgeCensusParser

class TestSexAgeCensusParser(unittest.TestCase):
    def setUp(self):
        self.parser = SexAgeCensusParser()

    def test_questions(self):
        q = 'how many men in New York?'
        match = self.parser.search(q)
        self.assertIsNotNone(match)

class TestSimpleCensusParser(unittest.TestCase):
    def setUp(self):
        self.parser = SimpleCensusParser()

    def test_a_question(self):
        q = 'how many Dominicans in New York?'
        match = self.parser.search(q)
        self.assertIsNotNone(match)

        self.assertIsNotNone(match.as_json())
        d = json.loads(match.as_json())
        self.assertEquals('04000US36',d['place']['full_geoid'])
        self.assertEquals(695158,d['population'])

        self.assertTrue('New York' in match.as_html())
        self.assertTrue('695158' in match.as_html())
        q = "how many chileans in new york?"
        match = self.parser.search(q)
        self.assertIsNotNone(match)

        self.assertIsNotNone(match.as_json())
        d = json.loads(match.as_json())
        self.assertEquals('04000US36',d['place']['full_geoid'])
        self.assertEquals(16764,d['population'])


    def test_asian_questions(self):
        q = 'how many chinese in New York?'
        match = self.parser.search(q)
        self.assertIsNotNone(match)

        self.assertIsNotNone(match.as_json())
        d = json.loads(match.as_json())
        self.assertEquals('04000US36',d['place']['full_geoid'])
        self.assertEquals(564836,d['population'])
        

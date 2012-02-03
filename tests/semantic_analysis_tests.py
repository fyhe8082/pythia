'''
Created on 1 Feb 2012

@author: george
'''
import unittest
from analysis.semantic import TwitterSemanticAnalyser

tweet1 = "RT @monaeltahawy: RT @Gheblawi Beyond belief: religious history &amp; make-up of #Egypt interesting discussion #Copts http://www.bbc.co.uk/podcasts/series/belief"
tweet2 = "Breaking News - Messi spotted outside the Etihad #transferdeadlineday http://twitpic.com/8dwcum (via @AndrewBloch )"
tweet3 = "This is not a retweet #test"
tweet4 = "RT Beyond belief: religious history &amp; make-up of #Egypt interesting discussion #Copts http://www.bbc.co.uk/podcasts/series/belief"
tweet5 = "This is Egypt. Hello my name is Bob Jones.  I am speaking to you at this very moment.  Are you listening to me, Bob?"
tweet6 = "This is so sad. I am desperate"
tweet7 = "I am so happy!"

class Test(unittest.TestCase):
    
    def test_entity_extraction(self):
        tsa = TwitterSemanticAnalyser()
        calculated = tsa.extract_entities(tweet5)
        expected = [{'status': 'OK', 'count': '3', 'language': 'english', 'url': 'None', 'text': 'Bob Jones', 'entity': '\n            ', 'relevance': '0.919207', 'usage': 'By accessing AlchemyAPI or using information generated by AlchemyAPI, you are agreeing to be bound by the AlchemyAPI Terms of Use: http://www.alchemyapi.com/company/terms.html', 'type': 'Person'}, {'relevance': '0.388583', 'count': '1', 'entity': '\n            ', 'type': 'Person', 'text': 'Bob'}, {'count': '1', 'yago': 'http://mpii.de/yago/resource/Egypt', 'umbel': 'http://umbel.org/umbel/ne/wikipedia/Egypt', 'name': 'Egypt', 'text': 'Egypt', 'opencyc': 'http://sw.opencyc.org/concept/Mx4rvViTg5wpEbGdrcN5Y29ycA', 'entity': '\n            ', 'subType': 'CityTown', 'dbpedia': 'http://dbpedia.org/resource/Egypt', 'freebase': 'http://rdf.freebase.com/ns/guid.9202a8c04000641f80000000000144a4', 'relevance': '0.348978', 'ciaFactbook': 'http://www4.wiwiss.fu-berlin.de/factbook/resource/Egypt', 'type': 'Country', 'disambiguated': '\n                '}]
        self.assertEqual(expected, calculated)
        
    def test_sentiment_extraction(self):
        tsa = TwitterSemanticAnalyser()
        calculated_sad = tsa.extract_sentiment(tweet6)
        calculated_happy = tsa.extract_sentiment(tweet7)
        
        self.assertEqual("negative", calculated_sad[0]['type'])
        self.assertEqual("positive", calculated_happy[0]['type'])
        
    def test_extract_keywords(self):
        tsa = TwitterSemanticAnalyser()
        calculated = tsa.extract_keywords(tweet5)
        expected = [{'status': 'OK', 'keyword': '\n            ', 'language': 'english', 'url': 'None', 'text': 'Bob Jones', 'relevance': '0.996084', 'usage': 'By accessing AlchemyAPI or using information generated by AlchemyAPI, you are agreeing to be bound by the AlchemyAPI Terms of Use: http://www.alchemyapi.com/company/terms.html'}, {'relevance': '0.438146', 'text': 'Egypt', 'keyword': '\n            '}]
        self.assertEqual(expected, calculated) 
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRetweetCounter']
    unittest.main()
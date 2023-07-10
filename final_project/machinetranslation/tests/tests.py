import unittest

from translator import english_to_french, french_to_english

class FrenchToEnglish(unittest.TestCase): 
    def test_equals(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test_not_equals(self):
        self.assertNotEqual(french_to_english('Bon'), 'Hello')

class EnglishToFrench(unittest.TestCase): 
    def test_equals(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_not_equals(self):
        self.assertNotEqual(english_to_french('Greetings'), 'Bonjour')

        
unittest.main()

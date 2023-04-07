# tests.py
import unittest
from .translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        # Test translation of "Hello"
        result = english_to_french("Hello")
        self.assertEqual(result, "Bonjour")

        # Test translation of empty string
        result = english_to_french("")
        self.assertEqual(result, "")

    def test_french_to_english(self):
        # Test translation of "Bonjour"
        result = french_to_english("Bonjour")
        self.assertEqual(result, "Hello")

        # Test translation of empty string
        result = french_to_english("")
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()

import unittest
from translator import englis_to_french,french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_for_null_input(self):
        text = ""
        self.assertEqual(len(text.strip()),0)

    def test_english_to_french(self):
        text = 'Hello'
        expected = "Bonjour"
        self.assertEqual(englis_to_french(text),expected)


class TestFranchToEnglish(unittest.TestCase):
    def test_for_null_input(self):
        text = ""
        self.assertEqual(len(text.strip()),0)

    def test_french_to_english(self):
        text = 'Bonjour'
        expected = 'Hello'
        self.assertEqual(french_to_english(text),expected)

unittest.main()
        
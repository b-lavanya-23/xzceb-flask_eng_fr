import unittest

from translator import englishToFrench,frenchToEnglish

class TestEtoF(unittest.TestCase):
    def test_english_to_french(self):
        self.assertNotEqual(englishToFrench("null"),'')
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

class TestFtoE(unittest.TestCase):
    def test_french_to_english(self):
        self.assertNotEqual(frenchToEnglish(" "), "null")
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

unittest.main()
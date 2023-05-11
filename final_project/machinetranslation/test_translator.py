import unittest
from translator import en_fr, fr_en

class TestTranslator(unittest.TestCase):
    def test_en_to_fr_null_input(self):
        self.assertIsNone(en_fr(None))      
    
    def test_en_to_fr(self):
        self.assertEqual(en_fr('Hello'), 'Bonjour')
    
    def test_fr_to_en_null_input(self):
        self.assertIsNone(fr_en(None))

    def test_fr_to_en(self):
        self.assertEqual(fr_en('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
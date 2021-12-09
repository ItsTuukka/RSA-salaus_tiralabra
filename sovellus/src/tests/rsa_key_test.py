import unittest
from sovelluslogiikka.rsa_key import RSAKey

class TestRsaKey(unittest.TestCase):
    def setUp(self):
        self.test_key = RSAKey(3233, 17)
    
    def test_get_modulus(self):
        self.assertEqual(3233, self.test_key.get_modulus())

    def test_get_exponent(self):
        self.assertEqual(17, self.test_key.get_exponent())
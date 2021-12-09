import unittest
from sovelluslogiikka.generate_keys import KeyGenerator
from sovelluslogiikka.rsa_key import RSAKey
from sovelluslogiikka.smallprimes import SmallPrimes

class TestKeyGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = KeyGenerator(2048, SmallPrimes, RSAKey)
        self.big_prime = 982451653
        self.big_composite = 124251499
    
    def test_is_prime(self):
        self.assertEqual(True, self.generator.is_prime(self.big_prime))
        self.assertEqual(False, self.generator.is_prime(self.big_composite))

    def test_miller_rabin(self):
        self.assertEqual(True, self.generator.miller_rabin(self.big_prime, 40))
        self.assertEqual(False, self.generator.miller_rabin(self.big_composite, 40))
    
    def test_screening(self):
        self.assertEqual(True, self.generator.screening(self.big_prime))
        self.assertEqual(False, self.generator.screening(self.big_composite))
    
    def test_key_generation(self):
        self.generator.generate_keys()
        self.assertEqual(True, self.generator.pub_key != None)
        self.assertEqual(True, self.generator.pvt_key != None)

import unittest
from sovelluslogiikka.encrypt import Encrypt
from sovelluslogiikka.generate_keys import KeyGenerator
from sovelluslogiikka.rsa_key import RSAKey
from sovelluslogiikka.smallprimes import SmallPrimes

class TestEncrypt(unittest.TestCase):
    def setUp(self):
        self.generator = KeyGenerator(2048, SmallPrimes, RSAKey)
        self.generator.generate_keys()
        self.msg = "Tämä on testi viesti."
    
    def test_encryption(self):
        encrypted_msg = Encrypt().encrypt(self.msg, self.generator.pub_key)
        self.assertEqual(encrypted_msg == self.msg, False)
        self.assertEqual(type(encrypted_msg), int)
    
    def test_string_to_bytes(self):
        in_bytes = Encrypt().string_to_bytes(self.msg)
        self.assertEqual(type(in_bytes), bytes)

    def test_bytes_to_int(self):
        in_bytes = Encrypt().string_to_bytes(self.msg)
        in_int = Encrypt().bytes_to_int(in_bytes)
        self.assertEqual(type(in_int), int)



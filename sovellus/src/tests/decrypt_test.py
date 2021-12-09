import unittest
from sovelluslogiikka.decrypt import Decrypt
from sovelluslogiikka.encrypt import Encrypt
from sovelluslogiikka.generate_keys import KeyGenerator
from sovelluslogiikka.rsa_key import RSAKey
from sovelluslogiikka.smallprimes import SmallPrimes

class TestDecrypt(unittest.TestCase):
    def setUp(self):
        self.generator = KeyGenerator(2048, SmallPrimes, RSAKey)
        self.generator.generate_keys()
        self.msg = "Tämä on testi viesti."
        self.size = len(self.msg.encode())
        self.encrypted_msg = Encrypt().encrypt(self.msg, self.generator.pub_key)
        self.decrypted = pow(self.encrypted_msg, self.generator.pvt_key.get_exponent(), self.generator.pvt_key.get_modulus())
    
    def test_decryption(self):
        decrypted_msg = Decrypt().decrypt(self.encrypted_msg, self.size, self.generator.pvt_key)
        self.assertEqual(decrypted_msg, self.msg)
    
    def test_int_to_bytes(self):
        in_bytes = Decrypt().int_to_bytes(self.decrypted, self.size)
        self.assertEqual(type(in_bytes), bytes)

    def test_bytes_to_string(self):
        in_bytes = Decrypt().int_to_bytes(self.decrypted, self.size)
        in_string = Decrypt().bytes_to_string(in_bytes)
        self.assertEqual(type(in_string), str)
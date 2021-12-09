class Encrypt:
    
    """Luokka viestin salaamiseen.
    """

    def encrypt(self, msg, key):
        """Salaa viestin.

        Args:
            msg: Salattava viesti.
            key: Viestin salaava avain.

        Returns:
            Salatun viestin.
        """

        in_bytes = self.string_to_bytes(msg)
        in_int = self.bytes_to_int(in_bytes)
        return pow(in_int, key.get_exponent(), key.get_modulus())

    def string_to_bytes(self, msg):
        """Muuntaa viestin tavuiksi.

        Args: 
            msg: Muutettava viesti.

        Returns:
            Viestin tavuina.
        """

        return msg.encode()

    def bytes_to_int(self, msg):
        """Muuntaa tavut luvuksi.

        Args:
            msg: Muutettavat tavut.

        Returns:
            Viestin lukuna.
        """

        return int.from_bytes(msg, "big")

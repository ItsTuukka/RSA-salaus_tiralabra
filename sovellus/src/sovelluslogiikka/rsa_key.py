class RSAKey:
    """Luokka muodostaa RSA-avain olion.

    Attributes:
        modulus: Avaimen modulus.
        exponent: Avaimen eksponentti.
    """

    def __init__(self, modulus, exponent):
        """Luokan konstruktori.

        Args: 
            modulus: Avaimessa käytettävä modulus.
            exponent: Avaimessa käytettävä eksponentti.
        """

        self.modulus = modulus
        self.exponent = exponent

    def get_modulus(self):
        """Palauttaa avaimen moduluksen.

        Returns:
            Integer, joka on avaimen modulus.
        """

        return self.modulus

    def get_exponent(self):
        """Palauttaa avaimen eksponentin.

        Returns:
            Integer, joka on avaimen eksponentti.
        """

        return self.exponent

class Decrypt:
    
    """Luokka salatun viestin purkamiseen.
    """

    def decrypt(self, msg, size, key):
        """Purkaa salatun viestin.

        Args:
            msg: Salattu viesti.
            key: Purkamiseen käytettävä avain.

        Returns:
            Puretun viestin.
        """

        decrypted = pow(msg, key.get_exponent(), key.get_modulus())
        in_bytes = self.int_to_bytes(decrypted, size)
        in_text = self.bytes_to_string(in_bytes)
        return in_text

    def int_to_bytes(self, msg, size):
        """Muuntaa luvun tavuiksi.

        Args:
            msg: Viesti lukuna.

        Returns:
            Viestin tavuina.
        """

        return msg.to_bytes(size, "big")

    def bytes_to_string(self, msg):
        """Muuntaa tavut tekstiksi.

        Args:
            msg: Viesti tavuina

        Returns:
            Viestin tekstinä.
        """

        return msg.decode()

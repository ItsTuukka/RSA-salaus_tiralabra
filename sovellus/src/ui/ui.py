from tkinter import constants, ttk, Text, END
from sovelluslogiikka.decrypt import Decrypt
from sovelluslogiikka.encrypt import Encrypt
from sovelluslogiikka.generate_keys import KeyGenerator
from sovelluslogiikka.rsa_key import RSAKey
from sovelluslogiikka.smallprimes import SmallPrimes
from tkinter.messagebox import showinfo


class UI:

    """Tämä luokka vastaa ohjelman graafisesta käyttöliittymästä.

    Attributes:
        self._root: Tkinterin juuri.
        self.keys_generated: Boolean, onko avainparia luotu.
    """

    def __init__(self, root):
        """Luokan konstruktori
        
        Args:
            self._root: Tkinterin juuri.
        """

        self._root = root
        self.keys_generated = False

    def start(self):
        """Luo ja näyttää käyttöliittymän.
        """

        head_label = ttk.Label(
            master=self._root, text="RSA-salausohjelma", font="Helvetica 20 bold")
        key_length_label = ttk.Label(
            master=self._root, text="Anna avainten pituus biteissä:", font=("Helvetica 13"))
        self.key_length_entry = ttk.Entry(master=self._root)
        generate_button = ttk.Button(
            master=self._root, text="Luo avainpari", command=self.generate)
        msg1_label = ttk.Label(
            master=self._root, text="Salattava viesti:", font="Helvetica 13")
        self.msg1_entry = Text(self._root, width=27,
                               height=7, font=("Helvetica 11"))
        encrypt_button = ttk.Button(
            master=self._root, text="Salaa viesti", command=self.encrypt)
        msg2_label = ttk.Label(
            master=self._root, text="Salattu viesti:", font="Helvetica 13")
        self.msg2_entry = Text(self._root, width=27,
                               height=7, font=("Helvetica 11"))
        msg3_label = ttk.Label(
            master=self._root, text="Purettava viesti:", font="Helvetica 13")
        self.msg3_entry = Text(self._root, width=27,
                               height=7, font=("Helvetica 11"))
        decrypt_button = ttk.Button(
            master=self._root, text="Pura salattu viesti", command=self.decrypt)
        msg4_label = ttk.Label(
            master=self._root, text="Purettu viesti:", font="Helvetica 13")
        self.msg4_entry = Text(self._root, width=27,
                               height=7, font=("Helvetica 11"))

        head_label.grid(row=0, column=0, columnspan=2,
                        sticky=(constants.W, constants.E))
        key_length_label.grid(row=2, column=0, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        self.key_length_entry.grid(row=2, column=1, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        generate_button.grid(
            row=2, column=2, sticky=constants.W, padx=5, pady=5)
        msg1_label.grid(row=3, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self.msg1_entry.grid(row=4, column=0, sticky=constants.W)
        encrypt_button.grid(row=5, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        msg2_label.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self.msg2_entry.grid(
            row=4, column=1, sticky=(constants.E, constants.W))
        msg3_label.grid(row=6, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self.msg3_entry.grid(row=7, column=0, sticky=constants.W)
        decrypt_button.grid(row=8, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        msg4_label.grid(row=6, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self.msg4_entry.grid(
            row=7, column=1, sticky=(constants.E, constants.W))

        self._root.grid_rowconfigure(0, minsize=50)

    def show_keys_generated(self):
        """Ilmoittaa avainten luomisesta.
        """

        showinfo("RSA salaus", "Avainpari luotu onnistuneesti!")

    def show_key_entry_error(self):
        """Ilmoittaa virhesyötteestä.
        """
        
        showinfo("Error", "Avainten pituus pitää olla luku väliltä 500-5000.")

    def show_key_error(self):
        """Ilmoittaa viestin saalmisesta ilman generoituja avaimia
        """
        
        showinfo("Error", "Ei generoituja avaimia.")

    def show_encrypt_error(self):
        """Ilmoittaa virhesyötteestä.
        """

        showinfo("Error", "Viestin salaus epäonnistui.")

    def show_decrypt_error(self):
        """Ilmoittaa virhesyötteestä.
        """
        
        showinfo("Error", "Viestin purku epäonnistui.")

    def generate(self):
        """Kutsuu tarvittavat metodit avainparin luomiseksi ja ilmoittaa onnistumisesta käyttäjälle.
        """
        
        try:
            length = int(self.key_length_entry.get())
        except:
            self.show_key_entry_error()
            return
        if length < 500 or length > 5000:
            self.show_key_entry_error()
            return
        self.kg = KeyGenerator(int(length), SmallPrimes, RSAKey)
        self.kg.generate_keys()
        self.key_length_entry.delete(0, END)
        self.show_keys_generated()
        self.keys_generated = True

    def encrypt(self):
        """Kutsuu tarvittavat metodit viestin salaamiseksi ja ilmoittaa onnistumisesta käyttäjälle.
        """
        
        if not self.keys_generated:
            self.show_key_error()
            return
        msg = str(self.msg1_entry.get("1.0", "end-1c"))
        self.msg_size = len(msg.encode())
        try:
            encrypted_msg = Encrypt().encrypt(msg, self.kg.pub_key)
        except:
            self.show_encrypt_error()
            return
        self.msg2_entry.insert(END, encrypted_msg)
        self.msg3_entry.insert(END, encrypted_msg)

    def decrypt(self):
        """Kutsuu tarvittavat metodit viestin purkamiseen ja ilmoittaa onnistumisesta käyttäjälle.
        """
        
        encrypted_msg = self.msg3_entry.get("1.0", "end-1c")
        try:
            decrypted_msg = Decrypt().decrypt(
                int(encrypted_msg), self.msg_size, self.kg.pvt_key)
        except:
            self.show_decrypt_error()
            return
        self.msg4_entry.insert(END, decrypted_msg)

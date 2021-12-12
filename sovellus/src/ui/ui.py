from tkinter import Tk, constants, ttk, Text
import tkinter
from sovelluslogiikka import encrypt
from sovelluslogiikka.decrypt import Decrypt
from sovelluslogiikka.encrypt import Encrypt
from sovelluslogiikka.generate_keys import KeyGenerator
from sovelluslogiikka.rsa_key import RSAKey
from sovelluslogiikka.smallprimes import SmallPrimes

class UI:

    def __init__(self, root):
        self._root = root

    def start(self):
        head_label = ttk.Label(master=self._root, text="RSA-salausohjelma", font="Helvetica 20 bold")
        key_length_label = ttk.Label(master=self._root, text="Anna avainten pituus biteissä:", font=("Helvetica 13"))
        self.key_length_entry = ttk.Entry(master=self._root)
        generate_button = ttk.Button(master=self._root, text="Luo avainpari", command=self.generate)
        msg1_label = ttk.Label(master=self._root, text="Salattava viesti:", font="Helvetica 13")
        self.msg1_entry = Text(self._root, width=27, height=7, font=("Helvetica 11"))
        encrypt_button = ttk.Button(master=self._root, text="Salaa viesti", command=self.encrypt)
        msg2_label = ttk.Label(master=self._root, text="Salattu viesti:", font="Helvetica 13")
        self.msg2_entry = Text(self._root, width=27, height=7, font=("Helvetica 11"))
        msg3_label = ttk.Label(master=self._root, text="Purettava viesti:", font="Helvetica 13")
        self.msg3_entry = Text(self._root, width=27, height=7, font=("Helvetica 11"))
        decrypt_button = ttk.Button(master=self._root, text="Pura salattu viesti", command=self.decrypt)
        msg4_label = ttk.Label(master=self._root, text="Purettu viesti:", font="Helvetica 13")
        self.msg4_entry = Text(self._root, width=27, height=7, font=("Helvetica 11"))


        head_label.grid(row=0, column=0, columnspan=2, sticky=(constants.W, constants.E))
        key_length_label.grid(row=2, column=0, sticky=(constants.W, constants.E), padx=5, pady=5)
        self.key_length_entry.grid(row=2, column=1, sticky=(constants.W, constants.E), padx=5, pady=5)
        generate_button.grid(row=2, column=2, sticky=constants.W, padx=5, pady=5)
        msg1_label.grid(row=3, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        self.msg1_entry.grid(row=4, column=0, sticky=constants.W)
        encrypt_button.grid(row=5, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        msg2_label.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        self.msg2_entry.grid(row=4, column=1, sticky=(constants.E, constants.W))
        msg3_label.grid(row=6, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        self.msg3_entry.grid(row=7, column=0, sticky=constants.W)
        decrypt_button.grid(row=8, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        msg4_label.grid(row=6, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        self.msg4_entry.grid(row=7, column=1, sticky=(constants.E, constants.W))

        self._root.grid_rowconfigure(0, minsize=50)
    
    def generate(self):
        length = int(self.key_length_entry.get())
        self.kg = KeyGenerator(int(length), SmallPrimes, RSAKey)
        self.kg.generate_keys()
        self.key_length_entry.delete(tkinter.END)
        keys_generated = ttk.Label(master=self._root, text="Avaimet luotu!")
        keys_generated.grid(row=3, column=2)
    
    def encrypt(self):
        msg = str(self.msg1_entry.get("1.0", "end-1c"))
        self.msg_size = len(msg.encode())
        encrypted_msg = Encrypt().encrypt(msg, self.kg.pub_key)
        self.msg2_entry.insert(tkinter.END, encrypted_msg)
        self.msg3_entry.insert(tkinter.END, encrypted_msg)

    def decrypt(self):
        encrypted_msg = self.msg3_entry.get("1.0", "end-1c")
        decrypted_msg = Decrypt().decrypt(int(encrypted_msg), self.msg_size, self.kg.pvt_key)
        self.msg4_entry.insert(tkinter.END, decrypted_msg)
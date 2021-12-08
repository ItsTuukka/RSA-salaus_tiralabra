from tkinter import Tk, constants, ttk, Text

class UI:

    def __init__(self, root):
        self._root = root
        self._root.geometry("660x400")

    def start(self):
        head_label = ttk.Label(master=self._root, text="RSA-salaus ohjelma", font="Helvetica 20 bold")
        key_length_label = ttk.Label(master=self._root, text="Anna avainten pituus biteissä:", font="italic 13")
        key_length_entry = ttk.Entry(master=self._root)
        generate_button = ttk.Button(master=self._root, text="Luo avainpari")
        msg_label = ttk.Label(master=self._root, text="Salattava viesti:", font="italic 13")
        msg_entry = Text(self._root, width=27, height=7)
        encrypt_button = ttk.Button(master=self._root, text="Salaa viesti")


        head_label.grid(row=0, column=0, columnspan=2)
        key_length_label.grid(row=2, column=0, sticky=constants.W, padx=5, pady=5)
        key_length_entry.grid(row=2, column=1, sticky=constants.W, padx=5, pady=5)
        generate_button.grid(row=2, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        msg_label.grid(row=3, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        msg_entry.grid(row=4, column=0, sticky=(constants.E, constants.W))
        encrypt_button.grid(row=5, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_rowconfigure(0, minsize=50)

        

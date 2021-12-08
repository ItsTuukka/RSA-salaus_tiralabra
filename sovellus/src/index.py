# from sovelluslogiikka.RSAkey import rsa_key
# from sovelluslogiikka.smallprimes import small_primes
# from sovelluslogiikka.generate_keys import key_generator
# from sovelluslogiikka.encrypt import encrypt
# from sovelluslogiikka.decrypt import decrypt

# """Alustava tekstipohjainen käyttöliittymä konseptin toimivuuden tarkistamiseen.
# Tarkoitus tehdä graafinseksi, jos vain mahdollista.
# """

# while True:
#     print("0: lopeta")
#     print("1: generoi RSA-avaimet")
#     choice = int(input())
#     if choice == 1:
#         length = int(input("Anna avainten pituus (suositus 2048): "))
#         kg = key_generator(length, small_primes, rsa_key)
#         kg.generate_keys()
#         print("Avaimet luotu")
#         text = str(input("Anna salattava viesti: "))
#         size_in_bytes = len(text.encode())
#         print(size_in_bytes)
#         encrypted_text = encrypt().encrypt(text, kg.pub_key)
#         print("salattu viesti:")
#         print(encrypted_text)
#         print("Pura viesti? (1 = kyllä)")
#         choice = int(input())
#         if choice == 1:
#             decrypted_text = decrypt().decrypt(encrypted_text, size_in_bytes, kg.pvt_key)
#             print("purettu viesti:")
#             print(decrypted_text)
#             break
#         else:
#             print("ei sitten")
#             break
#     else:
#         break

from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title('RSA salaus')
ui = UI(window)
ui.start()

if __name__ == '__main__':
    window.mainloop()
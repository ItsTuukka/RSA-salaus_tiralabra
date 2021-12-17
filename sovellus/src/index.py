from tkinter import Tk
from ui.ui import UI

"""Tämä tiedosto käynnistää ohjelman greefisen käyttöliittymän.
"""

window = Tk()
window.title('RSA salaus')
ui = UI(window)
ui.start()

if __name__ == '__main__':
    window.mainloop()
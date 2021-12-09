from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title('RSA salaus')
ui = UI(window)
ui.start()

if __name__ == '__main__':
    window.mainloop()
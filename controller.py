"""Modulo controlador del programa, se encarga de crear la ventana principal"""

from tkinter import Tk
from view import Views


if __name__ == "__main__":
    master_tk = Tk()
    obj1 = Views(master_tk)
    master_tk.mainloop()

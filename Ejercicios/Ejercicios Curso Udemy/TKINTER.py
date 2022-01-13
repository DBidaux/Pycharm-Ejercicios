# WIDGETS: TK, Frame, Label, Entry, Text, Button, RadioButton, CheckButton, Menu, Dialogs

import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Message-Box (Pop-Up)
def avisar():
    tkinter.messagebox.showinfo("Título", "Mensaje con la información")

boton = tkinter.Button(raiz, text="Pulsar para aviso", command=avisar)
boton.pack()


raiz.mainloop()
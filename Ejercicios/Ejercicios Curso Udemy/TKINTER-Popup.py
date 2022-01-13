# WIDGETS: TK, Frame, Label, Entry, Text, Button, RadioButton, CheckButton, Menu, Dialogs

import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Message-Box (Pop-Up)
def preguntar():
    resultado = tkinter.messagebox.askquestion("Título de la pregunta", "¿Quieres borrar este fichero?")
    if (resultado == "yes"):
        print("Sí, sí quiero borrar el fichero")
    else:
        print("No, no quiero borrar el fichero")
boton = tkinter.Button(raiz, text="Pulsar para preguntar", command=preguntar)
boton.pack()


raiz.mainloop()
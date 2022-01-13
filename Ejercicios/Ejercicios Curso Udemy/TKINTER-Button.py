# WIDGETS: TK, Frame, Label, Entry, Text, Button, RadioButton, CheckButton, Menu, Dialogs

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")


# Button
# Definimos accion
def accion():
    print("Hola mundo")


boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
boton.config(fg="green")
boton.pack()
raiz.mainloop()

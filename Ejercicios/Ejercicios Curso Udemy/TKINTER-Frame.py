#WIDGETS: TK, Frame, Label, Entry, Text, Button, RadioButton, CheckButton, Menu, Dialogs

import tkinter
raiz = tkinter.Tk()
raiz.title("Mi programa")

#Label
texto = "Hola mundo"
etiqueta = tkinter.Label(raiz, text=texto)
etiqueta.config(fg="green", bg="lightgrey", font="Cortana, 30")
etiqueta.pack()
raiz.mainloop()

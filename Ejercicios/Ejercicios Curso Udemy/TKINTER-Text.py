#WIDGETS: TK, Frame, Label, Entry, Text, Button, RadioButton, CheckButton, Menu, Dialogs

import tkinter
raiz = tkinter.Tk()
raiz.title("Mi programa")

#Text
entrada = tkinter.Text(raiz)
entrada.config(width=20, height=10, font=("Verdana", 15), padx=10, pady=10, fg="green", selectbackground="Lightgrey")
entrada.pack()
raiz.mainloop()

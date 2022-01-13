matricula = input("Introduce una matrícula: ")
if len(matricula) == 6 and \
        "A" <= matricula[0] <= "Z" and \
        "A" <= matricula[1] <= "Z" and \
        "A" <= matricula[2] <= "Z" and \
        "0" <= matricula[3] <= "9" and \
        "0" <= matricula[4] <= "9" and \
        "0" <= matricula[5] <= "9":
    print("Es una matrícula antigua válida")
elif len(matricula) == 7 and \
        "A" <= matricula[0] <= "Z" and \
        "A" <= matricula[1] <= "Z" and \
        "A" <= matricula[2] <= "Z" and \
        "0" <= matricula[3] <= "9" and \
        "0" <= matricula[4] <= "9" and \
        "0" <= matricula[5] <= "9" and \
        "0" <= matricula[6] <= "9":
    print("Es una matrícula nueva válida")
else:
    print("No es una matrícula válida")

contador = 0
print("Este programa calcula tu media introduciendo notas como a+, a, a-, b+, b, b-, c+, c, c-, d+, d, f")
number = int(input("Cuantas notas vas a introducir?: "))
mediatotal = 0

while contador < number:
    nota = input("Introduzca tu nota: ")
    if nota == "A" or nota == "A+":
        mediatotal += 4.0
    elif nota == "a_minus" or nota == "A-":
        mediatotal += 3.7
    elif nota == "b_plus" or nota == "B+":
        mediatotal += 3.3
    elif nota == "B":
        mediatotal += 3
    elif nota == "b_minus" or nota == "B-":
        mediatotal += 2.7
    elif nota == "c_plus" or nota == "C+":
        mediatotal += 2.3
    elif nota == "C":
        mediatotal += 2.0
    elif nota == "c_minus" or nota == "C-":
        mediatotal += 1.7
    elif nota == "d_plus" or nota == "D+":
        mediatotal += 1.3
    elif nota == "D":
        mediatotal += 1.0
    elif nota == "F":
        mediatotal += 0
    contador = contador + 1

notafinal = mediatotal / number
print("La nota media es de ", notafinal)

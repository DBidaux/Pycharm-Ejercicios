# Calificaciones alfabéticas a numéricas
a = 4.0
a_minus = 3.7
b_plus = 3.3
b = 3.0
b_minus = 2.7
c_plus = 2.3
c = 2.0
c_minus = 1.7
d_plus = 1.3
d = 1.0
f = 0
no_valido = -1

letra = input("Introduce una calificación alfabética: ")
letra = letra.upper()
if letra == "A+" or letra == "A":
    notanum = a
elif letra == "A-":
    notanum = a_minus
elif letra == "B+":
    notanum = b_plus
elif letra == "B":
    notanum = b
elif letra == "B-":
    notanum = b_minus
elif letra == "C+":
    notanum = c_plus
elif letra == "C":
    notanum = c
elif letra == "C-":
    notanum = c_minus
elif letra == "D+":
    notanum = d_plus
elif letra == "D":
    notanum = d
elif letra == "F":
    notanum = f
else:
    notanum = no_valido

if notanum == no_valido:
    print("No es una calificación académica.")
else:
    print("Es un " + str(notanum))

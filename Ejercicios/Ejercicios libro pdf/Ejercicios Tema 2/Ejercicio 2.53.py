rating = float(input("Introduzca una puntuación: "))
unacc = 0.0
acc = 0.4
meri = 0.6
raising = 2400 * rating
if rating == unacc:
    print("Su desempeño ha sido inaceptable. Su aumento es de", str(raising))
elif rating == acc:
    print("Su desempeño ha sido aceptable. Su aumento es de", str(raising))
elif rating == meri:
    print("Su desempeño ha sido meritorio. Su aumento es de", str(raising))
else:
    print("No existe esa calificación.")

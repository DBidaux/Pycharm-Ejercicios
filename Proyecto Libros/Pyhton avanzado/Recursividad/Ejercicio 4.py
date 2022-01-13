def SumarVector(vector, elemento):
    if elemento == 0:
        return vector[elemento]
    else:
        return SumarVector(vector, elemento - 1) + vector[elemento]


vectorenteros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Vector de enteros: ", vectorenteros)
elementoasumar = int(input("¿Cuantos elementos quieres sumar?: "))
if (elementoasumar > 0) & (elementoasumar <= len(vectorenteros)):
    print("Resultado: ", SumarVector(vectorenteros, elementoasumar-1))
else:
    print("ERRROR: El número de elementos a sumar es erróneo.")

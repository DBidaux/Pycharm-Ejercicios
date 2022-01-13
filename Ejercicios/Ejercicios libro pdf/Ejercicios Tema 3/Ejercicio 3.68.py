linea = input("Introduzca un conjunto de 8 bits (en blanco para finalizar): ")

while linea != "":
    if linea.count("0") + linea.count("1") != 8 or len(linea) != 8:
        print("No son 8 bits. Prueba de nuevo.")
    else:
        unos = linea.count("1")
        if unos % 2 == 0:
            print("El bit de paridad debería ser 0")
        else:
            print("El bit de paridad debería ser 1")
    linea = input("Introduzca un conjunto de 8 bits (en blanco para finalizar): ")

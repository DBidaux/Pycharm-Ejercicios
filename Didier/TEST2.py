fin = False
print("""************
Calculadora
************
    Menú
    1)Suma
    2)Resta
    3)Multiplicación
    4)División
    5)Salir""")
 
while not fin:
    opc = int(input('Opción:'))

    if opc == 1:
        sum1 = int(input("Introduce el primer sumando: "))
        sum2 = int(input("Introduce el segundo sumando: "))
        print("El resultado es: ", sum1 + sum2)

    elif opc == 2:
        minuendo = int(input("Minuendo: "))
        sustraendo = int(input("Sustraendo: "))
        print("El resultado es: ", minuendo - sustraendo)

    elif opc == 3:
        multiplicando = int(input("Multiplicando: "))
        multiplicador = int(input("Multiplicador: "))
        print("El resultado es: ", multiplicador * multiplicando)

    elif opc == 4:
        dividendo = int(input("Dividendo: "))
        divisor = int(input("Divisor: "))
        print("El resultado es:", dividendo / divisor)

    elif opc == 5:
        fin = True

def Sumar():
    sumando1 = int(input("Sumando uno:"))
    sumando2 = int(input("Sumando dos:"))
    print("El resultado de la suma es:", sumando1 + sumando2)


def Restar():
    rest1 = int(input("Minuendo:"))
    rest2 = int(input("Sustraendo:"))
    print("El resultado de la resta es:", rest1 - rest2)


def Multiplicar():
    mult1 = int(input("Multiplicando:"))
    mult2 = int(input("Multiplicador:"))
    print("El resultado de la multiplicación es:", mult1 * mult2)


def Dividir():
    dividendo = int(input("Dividendo:"))
    divisor = int(input("Divisor:"))
    print("El resultado de la división es:", dividendo / divisor)


def Calculadora():
    fin = False
    while not fin:
        opc = int(input("OPCIÓN:"))
        if opc == 1:
            Sumar()
        elif opc == 2:
            Restar()
        elif opc == 3:
            Multiplicar()
        elif opc == 4:
            Dividir()
        elif opc == 5:
            fin = True


print("""************
CALCULADORA
************
MENU
1)SUMA
2)RESTA
3)MULTIPLICACIÓN
4)DIVISIÓN
5)SALIR""")
Calculadora()


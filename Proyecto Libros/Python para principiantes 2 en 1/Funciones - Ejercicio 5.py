def di_hola(nombre):
    print(f"Hola, {nombre}!")
    print("Bienvenido a mi retransmisión en vivo!")


usuario = input("Introduce tu nombre, por favor: ")
di_hola(usuario)


def saludo(nombre, apellido):
    print(f"Hola, {nombre} {apellido}")
    print("Espero que disfrutes de mi transmisión!")


nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
saludo(nombre, apellido)


def cubo(numero):
    return numero * numero * numero


alcubo = float(input("Introduce el numero que quieres elevar al cubo:"))
print(cubo(alcubo))

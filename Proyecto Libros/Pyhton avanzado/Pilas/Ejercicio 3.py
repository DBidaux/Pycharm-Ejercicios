class Pila:
    def __init__(self):
        self.__items = []

    def EstaVacia(self):
        if len(self.__items) == 0:
            return True
        else:
            return False

    def Apilar(self, item):
        self.__items.append(item)

    def Retirar(self):
        return self.__items.pop()

    def LeerCima(self):
        return self.__items[len(self.__items) - 1]

    def LeerFondo(self):
        pilaauxiliar = Pila()
        while not (self.EstaVacia()):
            pilaauxiliar.Apilar(self.Retirar())
        valorfondo = pilaauxiliar.LeerCima()
        while not(pilaauxiliar.EstaVacia()):
            self.Apilar(pilaauxiliar.Retirar())
        return valorfondo

    def NumeroElementos(self):
        pilaauxiliar = Pila()
        while not (self.EstaVacia()):
            pilaauxiliar.Apilar(self.Retirar())
        numeroelementos = 0
        while not (pilaauxiliar.EstaVacia()):
            self.Apilar(pilaauxiliar.Retirar())
            numeroelementos = numeroelementos + 1
        return numeroelementos

    def MostrarPila(self):
        print("Pila: ", self.__items, "<---Cima")


def SimuladorPila():
    fin = False
    pila = Pila()
    while not fin:
        opc = input("Opción:")
        if opc == '1':
            item = input("Introduzca elemento a apilar: ")
            pila.Apilar(item)
            print("Elemento apilado: ", item)
        elif opc == '2':
            if pila.EstaVacia():
                print("La pila está vacía, no puede retirarse ningún elemento")
            else:
                item = pila.LeerCima()
                pila.Retirar()
                print("Elemento retirado: ", item)
        elif opc == '3':
            if pila.EstaVacia():
                print("La pila está vacía, no puede leerse la cima")
            else:
                print("La cima es: ", pila.LeerCima())
        elif opc == '4':
            if pila.EstaVacia():
                print("La pila está vacía, no puede leerse la cima")
            else:
                print("El fondo es: ", pila.LeerFondo())
        elif opc == '5':
            if pila.EstaVacia():
                print("La pila está vacía")
            else:
                print("La pila no está vacía")
        elif opc == '6':
            pila.MostrarPila()
        elif opc == '7':
            print("Número de elementos en la pila: ", pila.NumeroElementos())
        elif opc == '8':
            fin = True


print("""***********
Simulador de pila
***********
Menú:
1) Apilar
2) Retirar
3) Leer cima
4) Leer fondo
5) ¿Está vacía?
6) Número de elementos
7) Mostrar pila
8) Fin""")
SimuladorPila()

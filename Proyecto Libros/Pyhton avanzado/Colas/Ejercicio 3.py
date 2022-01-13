class Cola:
    def __init__(self):
        self.__items = []

    def EstaVacia(self):
        if len(self.__items) == 0:
            return True
        else:
            return False

    def Encolar(self, item):
        self.__items.insert(0, item)

    def Desencolar(self):
        return self.__items.pop()

    def LeerPrimerElemento(self):
        colaauxiliar = Cola()
        while not (self.EstaVacia()):
            ultimoelemento = self.Desencolar()
            colaauxiliar.Encolar(ultimoelemento)
        while not (colaauxiliar.EstaVacia()):
            self.Encolar(colaauxiliar.Desencolar())
        return ultimoelemento

    def NumeroElementos(self):
        colaauxiliar = Cola()
        numeroelementos = 0
        while not (self.EstaVacia()):
            numeroelementos = numeroelementos + 1
            colaauxiliar.Encolar(self.Desencolar())
        while not (colaauxiliar.Desencolar()):
            return numeroelementos

    def MostrarCola(self):
        print("Cola: ", self.__items, "<--Primer elemento")


def SimuladorCola():
    fin = False
    cola = Cola()
    while not fin:
        opc = input("Opción:")
        if opc == "1":
            item = input("Introduzca elemento a encolar: ")
            cola.Encolar(item)
            print("Elemento encolado: ", item)
        elif opc == "2":
            if cola.EstaVacia():
                print("La cola está vacía, no se puede desencolar ningún elemento.")
            else:
                item = cola.LeerPrimerElemento()
                cola.Desencolar()
                print("Elemento desencolado: ", item)
        elif opc == "3":
            if cola.EstaVacia():
                print("La cola está vacía, no se puede leer ningún elemento.")
            else:
                print("El primer elemento es: ", cola.LeerPrimerElemento())
        elif opc == "4":
            if cola.EstaVacia():
                print("La cola está vacía, no se puede leer ningún elemento.")
            else:
                print("El último elemento es: ", cola.NumeroElementos())
        elif opc == "5":
            if cola.EstaVacia():
                print("La cola está vacía.")
            else:
                print("La cola no está vacía.")
        elif opc == "6":
            print("Número de elementos: ", cola.NumeroElementos())
        elif opc == "7":
            cola.MostrarCola()
        elif opc == "8":
            fin = True

print("""**********
Simulador de Cola
***********
Menú:
1)Encolar
2)Desencolar
3)Leer primer elemento
4)Leer último elemento
5)¿Está vacía?
6)Número de elementos
7)Mostar cola
8)Salir""")
SimuladorCola()
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
    def MostrarPila(self):
        print("Pila: ", self.__items, "<---Cima")


pila = Pila()
for i in range(10):
    pila.Apilar(i)
pila.MostrarPila()
pilareves = Pila()
while not(pila.EstaVacia()):
    pilareves.Apilar(pila.Retirar())
pilareves.MostrarPila()
class PuntoPublico:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PuntoPrivado:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def GetX(self):
        return self.__x

    def GetY(self):
        return self.__y

    def SetX(self, x):
        self.__x = x

    def Sety(self, y):
        self.__y = y


publico = PuntoPublico(4, 6)
privado = PuntoPrivado(7, 3)
print("Valores de punto publico:", publico.x, ",", publico.y)
print("Valores de punto privado:", privado.GetX(), ",", privado.GetY())
publico.x = 2
privado.SetX(9)
print("Valores de punto publico:", publico.x, ",", publico.y)
print("Valores de punto privado:", privado.GetX(), ",", privado.GetY())

class OperarValores:
    def __init__(self, v1, v2):
        self.__V1 = v1
        self.__V2 = v2

    def __Sumar(self):
        return self.__V1 + self.__V2

    def __Restar(self):
        return self.__V1 - self.__V2

    def Operar(self):
        print("El resultado de la suma es:", self.__Sumar())
        print("El resultado de la resta es:", self.__Restar())

operarvalores = OperarValores(7,3)
operarvalores.Operar()



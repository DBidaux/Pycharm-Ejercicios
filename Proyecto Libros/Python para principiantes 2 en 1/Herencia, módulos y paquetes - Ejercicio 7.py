class Transporte:
    def Velocidad(self):
        print("Es muy rápido.")

    def Ruedas(self, numero):
        print(f"Tiene {numero} ruedas.")

    def Motor(self, tipo):
        print(f"Tiene un gran {tipo}.")


class Coche(Transporte):
    def Constructor(self, nombre):
        print(f"El diseñador es {nombre}")



class Moto(Transporte):
    def Caballito(self):
        print("Se pueden hacer caballitos")

ferrari = Coche()
ferrari.Constructor("Ferrari")
ferrari.Motor("V12")
ferrari.Ruedas(4)
ferrari.Velocidad()
yamaha = Moto()
yamaha.Motor("Twin-V")
yamaha.Velocidad()
yamaha.Ruedas(2)
yamaha.Caballito()

class Coche:
    def __init__(self, marca, modelo, color, combustible, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def Caracteristicas(self):
        print(
            "Este coche es de la marca {}, modelo {}, de color {}, usa {}, y su cilindrada es {}.".format(self.marca,
                                                                                                          self.modelo,
                                                                                                          self.color,
                                                                                                          self.combustible,
                                                                                                          self.cilindrada))

media = lambda nota1, nota2, nota3: (nota1 + nota2 + nota3) / 3

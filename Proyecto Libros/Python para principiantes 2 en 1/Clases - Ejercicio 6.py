class Heroes:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def Presentar(self):
        print("Mi nombre es " + self.nombre + ".")
        print(f"Tengo {self.edad} años.")
        print("El color de mi traje es " + self.color + ".")


heroe_1 = Heroes("Tony Stark", 38, "rojo")
heroe_2 = Heroes("Steve Rogers", 80, "azul")

heroe_1.Presentar()
print("----------")
heroe_2.Presentar()
print("----------")

try:
    name = "Bruce Wayne"
    edad = 40
    print(name + edad)
except TypeError:
    print("Usa una cadena formateada")

try:
    edad1 = 45
    edad2 = 0
    div = edad1/edad2
    print(div)
except ZeroDivisionError:
    print("No se puede dividir por 0")

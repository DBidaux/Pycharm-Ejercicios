def saludar(nombre):
    """
    Esto será un comentario de la función saludar.
    Esto función recibirá como parámetro una cadena con el nombre e
    imprimirá por pantalla un saludo con el nombre concatenado.
    """
    print("Buenos días " + nombre)

saludar("Didier")

class Saludos:
    """
    Esta clase tendrá dos funciones, buenos_dias y adios
    Ambas funciones recibirán como parámetro un nombre.
    """
    def buenos_dias(self, nombre):
        """
        Esta función sirve para decir buenos días
        :param nombre:
        :return:
        """
        print("Buenos días {}".format(nombre))
    def adios(self, nombre):
        """
        Esta función dice adiós a la persona.
        :param nombre:
        :return:
        """
        print("Adiós {}".format(nombre))
help(Saludos)
saludo = Saludos()
saludo.buenos_dias("Didier")
saludo.adios("Didier")
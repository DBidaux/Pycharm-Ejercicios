class Autor:
    def __init__(self, nombre, apellidos):
        self.Nombre = nombre
        self.Apellidos = apellidos

    def MostrarAutor(self):
        print("Autor: ", self.Nombre, " ", self.Apellidos)


class Libro:
    def __init__(self, titulo, isbn):
        self.Titulo = titulo
        self.ISBN = isbn

    def AnadirAutor(self, autor):
        self.Autor = autor

    def MostrarLibro(self):
        print("------ Libro ------ ")
        print("Titulo: ", self.Titulo)
        print("ISBN: ", self.ISBN)
        self.Autor.MostrarAutor()
        print("--------------------")

    def ObtenerTitulo(self):
        return self.Titulo


class Biblioteca:
    def __init__(self):
        self.ListaLibros = []

    def NumeroLibros(self):
        return len(self.ListaLibros)

    def AnadirLibro(self, libro):
        self.ListaLibros = self.ListaLibros + [libro]

    def MostrarBiblioteca(self):
        print("############################")
        for item in self.ListaLibros:
            item.MostrarLibro()
        print("############################")

    def BorrarLibro(self, titulo):
        encontrado = False
        posicionaborrar = -1
        for item in self.ListaLibros:
            posicionaborrar += 1
            if item.ObtenerTitulo() == titulo:
                encontrado = True
                break
        if encontrado:
            del self.ListaLibros[posicionaborrar]
            print("Libro borrado correctamente!")
        else:
            print("Libro no encontrado!")


def MostrarMenu():
    print("""MENU
        1)Añadir libro a la biblioteca
        2)Mostar Biblioteca
        3)Borrar libro
        4)Numero de libros?
        5)Salir""")


def AnadirLibroABiblioteca():
    titulo = input("Introduzca el título del libro:")
    isbn = input("Introduzca el ISBN del libro:")
    autornombre = input("Introduzca el nombre del autor:")
    autorapellidos = input("Introduzca los apellidos del autor:")
    autor = Autor(autornombre, autorapellidos)
    libro = Libro(titulo, isbn)
    libro.AnadirAutor(autor)
    biblioteca.AnadirLibro(libro)
    return biblioteca


def MostrarBiblioteca():
    biblioteca.MostrarBiblioteca()


def BorrarLibro():
    titulo = input("Introduzca el título del libro que quiere borrar:")
    biblioteca.BorrarLibro(titulo)


def NumeroLibros():
    print("El número de libros en la biblioteca es:", biblioteca.NumeroLibros())


fin = False
biblioteca = Biblioteca()

while not fin:
    MostrarMenu()
    opcion = int(input("Selecciones opción:"))
    if opcion == 1:
        biblioteca = AnadirLibroABiblioteca()
    elif opcion == 2:
        MostrarBiblioteca()
    elif opcion == 3:
        BorrarLibro()
    elif opcion == 4:
        NumeroLibros()
    elif opcion == 5:
        fin = True

print("Adiós!")

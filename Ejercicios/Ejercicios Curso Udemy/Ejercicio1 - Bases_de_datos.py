import sqlite3

# Crea o se conecta a una base de datos

conexion = sqlite3.connect("basededatosejercicio.db")

# Mediante el cursor hacemos consultas

cursor = conexion.cursor()

# Con el método execute creamos tabla

cursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER, Nombre TEXT, Precio INTEGER)")

# Hacemos una lista para introducir de una sola vez todos los artículos

lista_productos = [(1, 'Impresora', 300), (2, 'Ratón', 20),
                   (3, 'Ordenador', 600)]

# Con executemany se introducen

cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", lista_productos)

# Seleccionamos todos lo que hay en la tabla

cursor.execute("SELECT * FROM PRODUCTOS")

# Con fetchall recoge todos los campos

lista_productos = cursor.fetchall()

# Los hacemos iterar con un bucle for

for producto in lista_productos:
    print(producto)

# Con commit ejecutas las sentencias anteriores

conexion.commit()

# Con close cierras la base de datos

conexion.close()

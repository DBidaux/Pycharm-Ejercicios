import sqlite3

conexion = sqlite3.connect("basededatos1.db")
conexion.close()

# Creación tabla

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE PERSONAS (Nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")
conexion.commit()
conexion.close()

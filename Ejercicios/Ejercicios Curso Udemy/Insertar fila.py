import sqlite3
# Insertar datos en una fila

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()
cursor.execute("INSERT INTO PERSONAS VALUES ('Antonio', 'Perez', 'Gomez', '35')")
conexion.commit()
conexion.close()
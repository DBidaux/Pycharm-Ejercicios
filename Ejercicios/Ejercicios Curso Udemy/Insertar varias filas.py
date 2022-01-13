import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()
lista_personas = [('Pedro', 'Rodriguez', 'Perez', 26), ('Ana', 'Blanco', 'Iglesias', 45),
                  ('Estefanía', 'Fernandez', 'Gomez', 45)]
cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)", lista_personas)
conexion.commit()
conexion.close()
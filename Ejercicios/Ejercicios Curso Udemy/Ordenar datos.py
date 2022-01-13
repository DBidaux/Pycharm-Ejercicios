import sqlite3
conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")
lista_personas_ordenada = cursor.fetchall()
for persona in lista_personas_ordenada:
    print(persona)
conexion.close()
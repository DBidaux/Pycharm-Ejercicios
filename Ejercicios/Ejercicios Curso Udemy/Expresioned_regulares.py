#search
import re

texto1 = "Hola, mi nombre es Didier"
re.search("nombre", texto1)
resultado = re.search("nombre", texto1)
if resultado:
    print("Cadena encontrada")
else:
    print("Cadena no encontrada")

#findall
texto2 = """
EL coche de Luis es rojo, 
el coche de Ana es verde, 
y el coche de Miguel es rojo."""
prueba = re.findall("coche.*rojo", texto2)
print(prueba)

#split
texto3 = "La silla es blanca y vale 80"
prueba1 = re.split("\s", texto3)
print(prueba1)

#sub
texto4 = "La silla es blanca y vale 80"
prueba2 = re.sub("blanca", "roja", texto4)
print(prueba2)
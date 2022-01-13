# Módulo OS:
# getcwd: directorio actual de trabajo.
# chdir: cambia directorio de trabajo por una pasada por un parámetro.
# getpid: devuelve el identificador del proceso del aplicativo.
# getuid: devuelve el identificador del usuario del proceso aplicativo.
# listdir: lista el contenido del directorio de trabajo actual.
# mkdir: crea un directorio nuevo dentro del directorio actual.
# rename: renombra un fichero.
#
# Módulo shutil:
# copy: copia el fichero parametrizado en uno nuevo con el nombre especificado.
# move: mueve el fichero a la ruta especificada.


import os
import shutil

print("----------Ejercicio 1:----------")
print("Directorio de trabajo actual: ", os.getcwd())
print("Nuevo directorio de trabajo: ", os.getcwd())
print("ID proceso: ", os.getpid())
print("ID usuario: ", os.getuid())

print("----------Ejercicio 2:----------")
print("Directorio de trabajo: ", os.getcwd())
print("Contenido: ", os.listdir())
print("¡Copiando el fichero de ejemoplo.txt!")
shutil.copy
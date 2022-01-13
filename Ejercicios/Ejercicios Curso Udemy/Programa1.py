import modulofichero
nombre_fichero = "fichero1.txt"
fichero = modulofichero.Fichero(nombre_fichero)

texto = "Esta es la primera línea del fichero.\nEsta es la segunda línea del fichero."
fichero.grabar_fichero(texto)

texto = "\nEsta es la tercera línea del fichero."
fichero.incluir_fichero(texto)

texto_leido = fichero.leer_fichero()
print(texto_leido)

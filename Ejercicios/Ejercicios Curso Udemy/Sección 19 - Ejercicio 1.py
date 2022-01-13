import re


def buscar(palabra, texto):
    resultado = re.search(palabra, texto)
    return resultado


texto = "Esto es una frase para hacer búsquedas"
palabra = "frase"
resultado = buscar(palabra, texto)
if resultado:
    print("Palabra {} encontrada".format(palabra))
    inicial = resultado.start()
    final = resultado.end()
    print("Empieza en la posición {} y finaliza en la posición {}".format(inicial, final))
else:
    print("Palabra {} no encontrada".format(palabra))

print(resultado)

# Módulo random: elecciones de forma aleatoria
# Funciones:
# randrange: devuelve nº aleatorio en rango especificado
# sample: devuelve lista de nº en un rango especificado. 2 parámetros: rango de los numeros, y numero de elementos.
# random: devuelve un número decimal
# choice: selecciona elemento al azar de una lista.

import random
print("Número aleatorio(1-100): ", random.randrange(100))
print("Lista aleatoria de números(1-50): ", random.sample(range(50), 6))
print("Número decimal aleatorio: ", random.random())
print("Eleccion aleatoria [Rojo, Verde, Amarillo, Azul, Rosa]: ", random.choice(['Rojo', 'Verde', 'Amarillo', 'Azul', 'Rosa']))
# Módulo statistics:
# mean: media de una lista de números.
# median: mediana de una lista de números.
# median low: mediana inferior de una lista de números.
# median high: mediana superior de una lista de números.
# mode: moda de una lista de números.
# variance: varianza de un listado de números.

import statistics
import random

print("----------Ejercicio 1:----------")
valores = random.sample(range(10), 8)
print("Números aleatorios generados: ", valores)
print("Media: ", statistics.mean(valores))
print("Mediana: ", statistics.median(valores))
print("Mediana inferior: ", statistics.median_low(valores))
print("Mediana superior: ", statistics.median_high(valores))
print("Moda: ", statistics.mode(valores))
print("Varianza: ", statistics.variance(valores))
# JSON
# Datos de un diccionario a estructura JSON --> DUMPS

producto1 = {"nombre": "silla", "color": "blanco", "precio": 80}
import json
estructura_json = json.dumps(producto1)
print(estructura_json)

print(estructura_json[0])
print(producto1["nombre"])

# Convertir estructura JSON a diccionario --> LOADS
producto2 = json.loads(estructura_json)
print(producto2)
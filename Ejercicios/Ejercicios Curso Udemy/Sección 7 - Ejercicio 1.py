frutas = {"manzana": "apple", "naranja": "orange", "platano": "banana", "limon": "lemon"}
for fruta in frutas:
    print(fruta)
frutas["piña"] = "pineapple"
print(frutas)
for clave, valor in frutas.items():
    print("{} en inglés es {}".format(clave, valor))

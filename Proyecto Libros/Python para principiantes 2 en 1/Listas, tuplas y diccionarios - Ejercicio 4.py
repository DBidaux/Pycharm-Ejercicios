# Listas

friends = ["Joey", "Chandler", "Ross", "Phoebe", "Rachel", "Monica"]
print(friends)
print(len(friends))
for item in friends:
    print(f"Hola, {item}")
    print(f"Adiós, {item}")
print("----------")

print(friends[-6])
print(friends[-5])
print(friends[-4])
print(friends[-3])
print(friends[-2])
print(friends[-1])
print("----------")

print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print(friends[5])
print("----------")

print(friends[3:])
print(friends[2:5])
print("----------")

friends = ["Joey", "Chandler", "Ross", "Phoebe", "Rachel", "Monica"]
friends[0] = "Joey Tribbiani"
friends[1] = "Chandler Bing"
friends[2] = "Ross Geller"
friends[3] = "Phoebe Buffay"
friends[4] = "Rachel Green"
friends[5] = "Monica Geller"
print(friends)
print("----------")

numbers = [99, 123, 2313, 1, 1231411, 343, 435345]
print(numbers)
numbers.insert(2, 999)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print("----------")

amigo = {
    "nombre": "Didier",
    "edad": 27,
    "Correo electrónico": "Bidaux3@hotmail.es",
    "Coche": "BMW serie1"
}
print(amigo["Correo electrónico"])
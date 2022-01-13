for char in "Caracteres":
    print(char)
print("----------")

for char in ["Yo", "Amo", "Programar"]:
    print(char)
print("----------")

for number in range(20):
    print(number)
print("----------")

for number in range(10, 20):
    print(number)
print("----------")

for number in range(10, 21, 2):
    print(number)
print("----------")

prices = [5, 10, 15, 20, 25]
total = 0
for item in prices:
    total += item
print(f"Su precio total es: ${total}")
print("----------")

for a in range(3):
    for b in range(3):
        for c in range(3):
            print(f"({a}, {b}, {c})")
print("----------")


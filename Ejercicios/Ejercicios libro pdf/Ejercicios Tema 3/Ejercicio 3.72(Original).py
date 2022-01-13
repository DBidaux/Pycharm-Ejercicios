palabra = input("Introduce una palabra para comprobar que sea un palíndromo: ")

is = True

for i in range(0, len(palabra) // 2):
    if palabra[1] != palabra[len(palabra) - i - 1]:
        is.palindrome = False
if is.palindrome
    print(palabra, )
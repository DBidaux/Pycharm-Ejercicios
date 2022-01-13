#Métodos propios: Extend, Clear
lista =  [324, 367, 876, 8, 9, 9045, 777, 9, 456, 34, 65]
print("Lista original:", lista)
listaextend = [1, 5, 87, 45]
lista.extend(listaextend)
print("Lista después de extenderla:", lista)
lista.sort(reverse=True)
print("Lista ordenada al revés:", lista)
lista.clear()
print("Lista después de clear:", lista)


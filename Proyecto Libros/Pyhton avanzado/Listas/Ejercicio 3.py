#Métodos propios: Append, Insert, Remove, Pop
lista =  [324, 367, 876, 8, 9, 9045, 777, 9, 456, 34, 65]
print("Lista original:", lista)
lista.append(54)
lista.append(876)
print("Lista después de usar append:", lista)
lista.insert(4, 111)
lista.insert(8, 683)
print("Lista después de usar insert:", lista)
lista.sort()
print("Lista ordenada:", lista)
lista.remove(9)
print("Lista después de remove:", lista)
numerodevuelto = lista.pop()
print("Valor devuelto por pop:", numerodevuelto)
print("Lista después de pop sin parámetro:", lista)
numerodevuelto = lista.pop(3)
print("Valor devuelto por pop:", numerodevuelto)
print("Lista después de pop del 34:", lista)
mensaje = input("Introduce el mensaje: ")
cambio = int(input("Introduce el valor de cambio: "))

nuevo_mensaje = ""
for ch in mensaje:
    if "a" <= ch <= "z":
        pos = ord(ch) - ord("a")
        pos = (pos + cambio) % 26
        nuevo_caracter = chr(pos + ord("a"))
        nuevo_mensaje = nuevo_mensaje + nuevo_caracter
    elif "A" <= ch <= "Z":
        pos = ord(ch) - ord("A")
        pos = (pos + cambio) % 26
        nuevo_caracter = chr(pos + ord("A"))
        nuevo_mensaje = nuevo_mensaje + nuevo_caracter
    else:
        nuevo_mensaje = nuevo_mensaje + ch

print("El mensaje encriptado es", nuevo_mensaje)
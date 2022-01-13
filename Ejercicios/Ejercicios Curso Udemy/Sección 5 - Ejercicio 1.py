nota1 = int(input("Introduce la primera nota: "))
nota2 = int(input("Introduce la segunda nota: "))
nota3 = int(input("Introduce la tercer nota: "))
notamedia = (nota1 + nota2 + nota3)/3
if notamedia >= 5:
    print("Aprobado")
else:
    print("Suspenso")
year = int(input("Introduzca un año:"))

if year % 12 == 8:
    animal = "Dragón"
elif year % 12 == 9:
    animal = "Serpiente"
elif year % 12 == 10:
    animal = "Caballo"
elif year % 12 == 11:
    animal = "Oveja"
elif year % 12 == 0:
    animal = "Mono"
elif year % 12 == 1:
    animal = "Gallo"
elif year % 12 == 2:
    animal = "Perro"
elif year % 12 == 3:
    animal = "Cerdo"
elif year % 12 == 4:
    animal = "Rata"
elif year % 12 == 5:
    animal = "Buey"
elif year % 12 == 6:
    animal = "Tigre"
else:
    animal = "Conejo"

print("%d es el año del %s." % (year, animal))

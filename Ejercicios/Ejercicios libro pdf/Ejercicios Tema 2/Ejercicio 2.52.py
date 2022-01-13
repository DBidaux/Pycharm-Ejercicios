notanum = float(input("Introduzca una nota numérica: "))

if -1 < notanum < 0.99:
    print("La nota alfabética es F")
elif 1.0 <= notanum < 1.29:
    print("La nota alfabética es D")
elif 1.3 <= notanum < 1.69:
    print("La nota alfabética es D+")
elif 1.7 <= notanum < 1.99:
    print("La nota alfabética es C-")
elif 2.0 <= notanum < 2.29:
    print("La nota alfabética es C")
elif 2.3 <= notanum < 2.69:
    print("La nota alfabética es C+")
elif 2.7 <= notanum < 2.99:
    print("La nota alfabética es B-")
elif 3.0 <= notanum < 3.29:
    print("La nota alfabética es B")
elif 3.3 <= notanum < 3.69:
    print("La nota alfabética es B+")
elif 3.7 <= notanum < 3.99:
    print("La nota alfabética es A-")
elif notanum == 4.0:
    print("La nota alfabética es A")
elif notanum > 4.0:
    print("La nota alfabética es A+")

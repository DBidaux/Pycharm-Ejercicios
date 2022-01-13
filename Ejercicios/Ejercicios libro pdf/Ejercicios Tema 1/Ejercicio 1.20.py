presion = float(input("Introduce la presión en Pascales del sistema: "))
volumen = float(input("Introduce el volumen en litros del sistema: "))
temp = float(input("Introduce la temperatura en grados centigrados del sistema: "))
R = 8.314
temp_k = temp + 273.15
n = (presion * volumen) / R * temp_k
print("El nº de moles presentes en un tanque SCUBA es de " + str(n) + " moles.")

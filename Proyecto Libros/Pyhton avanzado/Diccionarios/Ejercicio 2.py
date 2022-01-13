#Métodos propios: Get, Update, SetDefault
numerosingles = {"Uno":"One", "Dos":"Two", "Tres":"Three", "Cuatro":"Four", "Cinco":"Five"}
print("Diccionario original", numerosingles)
print("Valor del Tres (get):", numerosingles.get("Tres"))
print("Valor del Seis (get) (no existe):", numerosingles.get("Seis"))
print("Valor del Seis (get) (no existe):", numerosingles.get("Seis", "No existe"))
numerosingles.update({"Seis":"Six", "Tres":"ThreeNUEVO"})
print("Diccionario después del update:", numerosingles)
print("setdefault del Siete:", numerosingles.setdefault("Siete", "Seven"))
print("Diccionario después del setdefault (nuevo elemento):", numerosingles)
print("setdefault del Cinco:", numerosingles.setdefault("Cinco", "FiveNUEVO"))
print("Diccionario después del setdefault (elemento existente):", numerosingles)
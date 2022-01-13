import threading


def MostrarInformacion():
    print("Hilo:", threading.currentThread().getName(), "con identificador:", threading.currentThread().ident)


print("# Ejecución sin hilos #")
MostrarInformacion()
MostrarInformacion()
MostrarInformacion()

print("# Ejecución con hilos #")
hilo1 = threading.Thread(target=MostrarInformacion())
hilo2 = threading.Thread(target=MostrarInformacion())
hilo3 = threading.Thread(target=MostrarInformacion())
hilo1.start()
hilo2.start()
hilo3.start()
hilo1.join()
hilo2.join()
hilo3.join()

import os
import time
import threading
import multiprocessing


def MostrarInformacion():
    print("PID: %s, Nombre proceso: %s" % (os.getpid(), multiprocessing.current_process().name))


if __name__ == "__main__":
    MostrarInformacion()
    proceso1 = multiprocessing.Process(target=MostrarInformacion())
    proceso2 = multiprocessing.Process(target=MostrarInformacion())
    proceso3 = multiprocessing.Process(target=MostrarInformacion())
    proceso1.start()
    proceso2.start()
    proceso3.start()
    proceso1.join()
    proceso2.join()
    proceso3.join()

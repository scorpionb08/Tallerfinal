import time
import random

class Vehiculo:
    def __init__(self, velocidad, posicion):
        self.velocidad = velocidad
        self.posicion = posicion

    def mover(self):
        self.posicion += self.velocidad

    def __str__(self):
        return f"Vehiculo en la posición {self.posicion} con velocidad {self.velocidad}"

class Semáforo:
    def __init__(self, estado):
        self.estado = estado

    def cambiar_estado(self):
        self.estado = not self.estado

    def __str__(self):
        return f"Semáforo en estado {'verde' if self.estado else 'rojo'}"


class Cruce:
    def __init__(self, semaforo1, semaforo2):
        self.semaforo1 = semaforo1
        self.semaforo2 = semaforo2

    def __str__(self):
        return f"Cruce con semáforos {self.semaforo1} y {self.semaforo2}"

class SimuladorDeTráfico:
    def __init__(self, vehiculos, cruces):
        self.vehiculos = vehiculos
        self.cruces = cruces

    def simular(self, tiempo):
        for i in range(tiempo):
            print(f"Tiempo {i}")
            for vehiculo in self.vehiculos:
                vehiculo.mover()
                print(vehiculo)
            for cruce in self.cruces:
                if cruce.semaforo1.estado:
                    print(f"{cruce.semaforo1} en {cruce}")
                else:
                    print(f"{cruce.semaforo2} en {cruce}")
                    for vehiculo in self.vehiculos:
                        if vehiculo.posicion >= 0 and vehiculo.posicion <= 10:
                            vehiculo.velocidad = 0
                        else:
                            vehiculo.velocidad = random.randint(1, 5)
            time.sleep(2)


vehiculo1 = Vehiculo(2, 0)
vehiculo2 = Vehiculo(3, 5)
vehiculo3 = Vehiculo(4, 10)

semaforo1 = Semáforo(True)
semaforo2 = Semáforo(False)

cruce1 = Cruce(semaforo1, semaforo2)

simulador = SimuladorDeTráfico([vehiculo1, vehiculo2, vehiculo3], [cruce1])

simulador.simular(6)
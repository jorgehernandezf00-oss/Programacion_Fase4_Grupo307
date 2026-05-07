from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass


class ReservaSala(Servicio):
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        total = 100000 * duracion
        total -= total * descuento
        total += total * impuesto
        return total


class AlquilerEquipo(Servicio):
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        if 1 <= duracion <= 2:
            total = 250000
        elif 4 <= duracion <= 6:
            total = 500000
        else:
            total = 250000 * duracion

        total -= total * descuento
        total += total * impuesto
        return total


class Asesoria(Servicio):
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        total = 280000 * duracion
        total -= total * descuento
        total += total * impuesto
        return total
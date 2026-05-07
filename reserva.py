from excepciones import ReservaError
from logger import log_info

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        try:
            if not (1 <= duracion <= 24):
                raise ValueError("Duración fuera de rango")

            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "Pendiente"
            self.costo = servicio.calcular_costo(duracion)

        except Exception as e:
            raise ReservaError("Error al crear reserva") from e

    def confirmar(self):
        self.estado = "Confirmada"
        log_info(f"Reserva confirmada: {self.cliente.nombre}")

    def cancelar(self):
        self.estado = "Cancelada"
        log_info(f"Reserva cancelada: {self.cliente.nombre}")
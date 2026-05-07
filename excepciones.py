class ClienteError(Exception):
    """Excepción para errores en los datos del cliente"""
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ServicioError(Exception):
    """Excepción para errores en el cálculo de servicios"""
    pass

class ReservaError(Exception):
    """Excepción para errores en la lógica de reservas"""
    pass
class SoftwareFJError(Exception):
    """Clase base para excepciones de la empresa Software FJ"""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Se lanza cuando los datos de la reserva no son correctos"""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza cuando el servicio solicitado no está disponible"""
    pass

class ClienteNoValidoError(SoftwareFJError):
    """Se lanza cuando los datos del cliente son erróneos"""
    pass

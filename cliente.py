from abc import ABC, abstractmethod
from excepciones import ClienteError

class Entidad(ABC):
    def __init__(self, id_entidad):
        self._id = id_entidad

    @abstractmethod
    def mostrar_info(self):
        pass


class Cliente(Entidad):
    def __init__(self, id_entidad, nombre, correo):
        super().__init__(id_entidad)

        if not nombre.strip():
            raise ClienteError("Nombre vacío")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        self._nombre = nombre
        self._correo = correo

    @property
    def nombre(self):
        return self._nombre

    def mostrar_info(self):
        return f"{self._nombre} ({self._correo})"
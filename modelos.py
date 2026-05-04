from abc import ABC, abstractmethod
from errores import ClienteNoValidoError

# 1. Clase Abstracta Base (Requisito: Abstracción)
class EntidadBase(ABC):
    def __init__(self, id_entidad):
        self.id_entidad = id_entidad

# 2. Clase Cliente (Requisito: Encapsulación y Validaciones)
class Cliente(EntidadBase):
    def __init__(self, id_cliente, nombre, correo):
        super().__init__(id_cliente)
        # Validación estricta
        if not nombre or "@" not in correo:
            raise ClienteNoValidoError("Datos de cliente incompletos o correo inválido.")
        
        self.__nombre = nombre  # Atributo privado (Encapsulación)
        self.__correo = correo

    def obtener_info(self):
        return f"Cliente: {self.__nombre} | Email: {self.__correo}"

# 3. Clase Abstracta Servicio (Requisito: Polimorfismo)
class Servicio(EntidadBase, ABC):
    def __init__(self, id_servicio, nombre, precio_base):
        super().__init__(id_servicio)
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        """Cada servicio calculará su costo de forma diferente"""
        pass

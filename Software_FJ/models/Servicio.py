from abc import ABC, abstractmethod

from Software_FJ.utils.GeneradorId import GeneradorId


class Servicio(ABC):
    def __init__(self, nombre, descripcion, precioBase, disponible=True):
        self.__idServicio = f"SER-{GeneradorId.generarId()}"
        self.nombre = nombre
        self.descripcion = descripcion
        self.precioBase = precioBase
        self.disponible = disponible

    @property
    def idServicio(self):
        return self.__idServicio

    @abstractmethod
    def calcularCosto(self, cantidad, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describirServicio(self):
        pass

    @abstractmethod
    def validarParametros(self):
        pass

    def calcularCostoConAjustes(self, cantidad, descuento=0, impuesto=0):
        """Variante común: aplica descuento porcentual y luego impuesto porcentual."""
        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise ValueError("Descuento e impuesto deben estar entre 0 y 100")
        base = self.calcularCosto(cantidad)
        return round(base * (1 - descuento / 100) * (1 + impuesto / 100), 2)

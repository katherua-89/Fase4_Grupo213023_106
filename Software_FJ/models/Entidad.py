from abc import ABC, abstractmethod
from datetime import date

from Software_FJ.utils.GeneradorId import GeneradorId


class Entidad(ABC):
    def __init__(self):
        self._id = f"ENT-{GeneradorId.generarId()}"
        self._fechaCreacion = date.today()

    @property
    def id(self) -> str:
        return self._id

    @property
    def fechaCreacion(self) -> date:
        return self._fechaCreacion

    @abstractmethod
    def validarDatos(self):
        pass

    @abstractmethod
    def obtenerInformacion(self):
        pass

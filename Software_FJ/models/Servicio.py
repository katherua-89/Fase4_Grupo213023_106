from abc import ABC, abstractmethod
from utils.GeneradorId import GeneradorId as gen
class Servicio(ABC):
    #Se establece una entidad padre, de la que se heredaran id y fecha de creacion
    __idServicio:str
    nombre:str
    descripcion:str
    precioBase:float
    disponible:bool
    
    #Se construye un constructor para el id y la fecha
   
    def __init__(self, nombre, descripcion, precioBase, disponible):
        self.__idServicio=f"SER-{gen.generarId()}"
        self.nombre=nombre
        self.descripcion=descripcion
        self.precioBase=precioBase
        self.disponible=disponible

    @abstractmethod
    def calcularCosto():
        pass
    @abstractmethod
    def describirServicio():
        pass
    @abstractmethod
    def validarParametros():
        pass
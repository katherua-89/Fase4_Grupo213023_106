from datetime import date
from utils.GeneradorId import GeneradorId as gen
from abc import ABC, abstractmethod
class Entidad(ABC):
    #Se establece una entidad padre, de la que se heredaran id y fecha de creacion
    __id:int
    __fechaCreacion:date
    #Se construye un constructor para el id y la fecha
   
    def __init__(self):
        self.__id=f"ENT-{gen.generarId()}"
        self.fechaCreacion=date.today()
        
    @abstractmethod
    def validarDatos():
        pass
    @abstractmethod
    def obtenerInformacion():
        pass
    
        
    
from datetime import date
from utils.GeneradorId import GeneradorId as gen
class Entidad():
    #Se establece una entidad padre, de la que se heredaran id y fecha de creacion
    id:int
    fechaCreacion:date
    #Se construye un constructor para el id y la fecha
    def __init__(self, id):
        self.id=f"ENT-{gen.generarId()}"
        self.fechaCreacion=date.today()
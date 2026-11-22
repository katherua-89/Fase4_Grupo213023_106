from Software_FJ.models.Cliente import Cliente
from Software_FJ.models.Servicio import Servicio
from utils.GeneradorId import GeneradorId as gen
class Reserva():
    #Atributos de la clase
    idReserva:str
    cliente:Cliente
    servicio:Servicio
    duracion:int
    estado:str
    costoTotal:float
    #Se construye un constructor para la reserva
    def __init__(self, cliente, servicio, duracion,estado):
        self.idReserva=f"RES-{gen.generarId()}"
        self.cliente=cliente
        self.servicio=servicio
        self.duracion=duracion
        self.estado=estado
        self.costoTotal=self.servicio.calcularCosto(self.duracion)
    def confirmarReserva(self):
        #Se confirma la reserva
        self.estado="Confirmada"
        return f"Reserva confirmada para el cliente {self.cliente.nombre} con el servicio {self.servicio.nombre}"
    def cancelarReserva(self):
        #Se cancela la reserva
        self.estado="Cancelada"
        return f"Reserva cancelada para el cliente {self.cliente.nombre} con el servicio {self.servicio.nombre}"
    def describirReserva(self):
        #Se describe la reserva
        return f"Reserva ID: {self.idReserva}, Cliente: {self.cliente.nombre}, Servicio: {self.servicio.nombre}, Duración: {self.duracion} horas, Estado: {self.estado}, Costo Total: {self.costoTotal}"
    def procesarReserva(self):
        #Se procesa la reserva
        if self.cliente is None or self.servicio is None:
            raise ValueError("El cliente y el servicio no pueden ser nulos")
        if self.duracion <= 0:
            raise ValueError("La duración debe ser mayor a 0")
        if not isinstance(self.duracion, int):
            raise ValueError("La duración debe ser un número entero")
        if not isinstance(self.estado, str):
            raise ValueError("El estado debe ser un valor de tipo string")
        if not isinstance(self.costoTotal, (int, float)):
            raise ValueError("El costo total debe ser un número")
        if self.costoTotal < 0:
            raise ValueError("El costo total no puede ser negativo")
        if self.estado == "Confirmada":
            return f"Reserva procesada para el cliente {self.cliente.nombre} con el servicio {self.servicio.nombre}. Costo total: {self.costoTotal}"
        else:
            return f"No se puede procesar la reserva ya que no está confirmada."
    def calcularCostoTotal(self):
        #Se calcula el costo total de la reserva
        self.costoTotal=self.servicio.calcularCosto(self.duracion)
        return self.costoTotal
    def cambiarEstado(self, nuevoEstado:str):
        #Se cambia el estado de la reserva
        if not isinstance(nuevoEstado, str):
            raise ValueError("El nuevo estado debe ser un valor de tipo string")
        self.estado=nuevoEstado
        return f"El estado de la reserva {self.idReserva} ha sido cambiado a {self.estado}"
    
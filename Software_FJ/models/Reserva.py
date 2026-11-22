from Software_FJ.models.Cliente import Cliente
from Software_FJ.models.Servicio import Servicio
from Software_FJ.utils.GeneradorId import GeneradorId


class Reserva:
    ESTADOS = {"PENDIENTE", "CONFIRMADA", "CANCELADA"}

    def __init__(self, cliente: Cliente, servicio: Servicio, duracion: int):
        self.idReserva = f"RES-{GeneradorId.generarId()}"
        self.cliente, self.servicio, self.duracion = cliente, servicio, duracion
        self.estado = "PENDIENTE"
        self.costoTotal = 0

    def confirmarReserva(self):
        self.procesarReserva()
        self.estado = "CONFIRMADA"
        self.costoTotal = self.servicio.calcularCosto(self.duracion)
        return self

    def cancelarReserva(self):
        if self.estado == "CONFIRMADA":
            raise ValueError("No se puede cancelar una reserva confirmada")
        self.estado = "CANCELADA"
        return self

    def procesarReserva(self):
        if not isinstance(self.cliente, Cliente) or not isinstance(self.servicio, Servicio):
            raise ValueError("Cliente y servicio son obligatorios")
        if not isinstance(self.duracion, int) or self.duracion <= 0:
            raise ValueError("La duración debe ser un entero mayor a 0")
        if not self.servicio.disponible:
            raise ValueError("El servicio no está disponible")
        self.costoTotal = self.servicio.calcularCosto(self.duracion)
        return True

    def calcularCostoTotal(self, descuento=0, impuesto=0):
        self.costoTotal = self.servicio.calcularCosto(self.duracion, descuento, impuesto)
        return self.costoTotal

    def describirReserva(self):
        return f"{self.idReserva} | cliente={self.cliente.nombre} | servicio={self.servicio.nombre} | duración={self.duracion} | estado={self.estado} | total={self.costoTotal}"

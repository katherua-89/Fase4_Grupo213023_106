from __future__ import annotations

from Software_FJ.exceptions.ExcepcionesPersonalizadas import (
    DatosInvalidosError,
    OperacionNoPermitidaError,
    RecursoNoEncontradoError,
    ReservaInvalidaError,
    ServicioNoDisponibleError,
)
from Software_FJ.models.Reserva import Reserva
from Software_FJ.utils.GestorLogs import GestorLogs


class ReservaService:
    """Crea y procesa reservas asociando clientes con servicios."""

    # Aporte de Edwin Arley Duarte Escobar: las reservas se mantienen en una
    # colección en memoria, sin acoplar la aplicación a una base de datos.

    def __init__(self, cliente_service, servicio_service, logger: GestorLogs | None = None):
        self.cliente_service = cliente_service
        self.servicio_service = servicio_service
        self.reservas: dict[str, Reserva] = {}
        self.logger = logger or GestorLogs()

    def crear(self, id_cliente: str, id_servicio: str, duracion: int) -> Reserva:
        try:
            cliente = self.cliente_service.obtener(id_cliente)
            servicio = self.servicio_service.obtener(id_servicio)
            if not servicio.disponible:
                raise ServicioNoDisponibleError(f"El servicio {id_servicio} no está disponible")
            reserva = Reserva(cliente, servicio, duracion)
            reserva.procesarReserva()
            self.reservas[reserva.idReserva] = reserva
            self.logger.registrarEvento("CREAR_RESERVA", reserva.idReserva)
            return reserva
        except Exception as exc:
            self.logger.registrarError("CREAR_RESERVA", str(exc), type(exc).__name__)
            if isinstance(exc, (ServicioNoDisponibleError, RecursoNoEncontradoError, ReservaInvalidaError)):
                raise
            raise ReservaInvalidaError(f"No fue posible crear la reserva: {exc}") from exc

    def obtener(self, id_reserva: str) -> Reserva:
        try:
            return self.reservas[id_reserva]
        except KeyError as exc:
            raise RecursoNoEncontradoError(f"No existe la reserva {id_reserva}") from exc

    def confirmar(self, id_reserva: str) -> Reserva:
        reserva = self.obtener(id_reserva)
        try:
            reserva.confirmarReserva()
            self.logger.registrarEvento("CONFIRMAR_RESERVA", id_reserva)
            return reserva
        except Exception as exc:
            self.logger.registrarError("CONFIRMAR_RESERVA", str(exc), type(exc).__name__)
            raise OperacionNoPermitidaError(str(exc)) from exc

    def cancelar(self, id_reserva: str) -> Reserva:
        reserva = self.obtener(id_reserva)
        try:
            reserva.cancelarReserva()
            self.logger.registrarEvento("CANCELAR_RESERVA", id_reserva)
            return reserva
        except Exception as exc:
            self.logger.registrarError("CANCELAR_RESERVA", str(exc), type(exc).__name__)
            raise OperacionNoPermitidaError(str(exc)) from exc

    def listar(self) -> list[Reserva]:
        return list(self.reservas.values())

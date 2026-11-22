from __future__ import annotations

from Software_FJ.exceptions.ExcepcionesPersonalizadas import (
    DatosInvalidosError,
    RecursoNoEncontradoError,
)
from Software_FJ.models.Servicio import Servicio
from Software_FJ.utils.GestorLogs import GestorLogs


class ServicioService:
    """Administra servicios especializados sin usar base de datos."""

    # Aporte de Katerin Marcela Rua Sanchez: el catálogo trabaja con la clase
    # abstracta Servicio, permitiendo registrar cualquier implementación concreta.

    def __init__(self, logger: GestorLogs | None = None):
        self.servicios: dict[str, Servicio] = {}
        self.logger = logger or GestorLogs()

    def registrar(self, servicio: Servicio) -> Servicio:
        try:
            if not isinstance(servicio, Servicio):
                raise DatosInvalidosError("El objeto recibido no es un Servicio válido")
            servicio.validarParametros()
            self.servicios[servicio.idServicio] = servicio
            self.logger.registrarEvento("REGISTRAR_SERVICIO", servicio.idServicio)
            return servicio
        except Exception as exc:
            self.logger.registrarError("REGISTRAR_SERVICIO", str(exc), type(exc).__name__)
            if isinstance(exc, DatosInvalidosError):
                raise
            raise DatosInvalidosError(f"No fue posible registrar el servicio: {exc}") from exc

    def listar(self, solo_disponibles: bool = False) -> list[Servicio]:
        servicios = list(self.servicios.values())
        return [s for s in servicios if s.disponible] if solo_disponibles else servicios

    def obtener(self, id_servicio: str) -> Servicio:
        try:
            return self.servicios[id_servicio]
        except KeyError as exc:
            self.logger.registrarError("OBTENER_SERVICIO", id_servicio, "RecursoNoEncontrado")
            raise RecursoNoEncontradoError(f"No existe el servicio {id_servicio}") from exc

    def cambiar_disponibilidad(self, id_servicio: str, disponible: bool) -> Servicio:
        servicio = self.obtener(id_servicio)
        if not isinstance(disponible, bool):
            raise DatosInvalidosError("La disponibilidad debe ser booleana")
        servicio.disponible = disponible
        self.logger.registrarEvento("CAMBIAR_DISPONIBILIDAD", id_servicio)
        return servicio

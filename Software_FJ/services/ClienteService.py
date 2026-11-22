from __future__ import annotations

from Software_FJ.exceptions.ExcepcionesPersonalizadas import (
    DatosInvalidosError,
    RecursoNoEncontradoError,
)
from Software_FJ.models.Cliente import Cliente
from Software_FJ.utils.GestorLogs import GestorLogs


class ClienteService:
    """Casos de uso para registrar, consultar y actualizar clientes."""

    def __init__(self, logger: GestorLogs | None = None):
        self.clientes: dict[str, Cliente] = {}
        self.logger = logger or GestorLogs()

    def registrar(self, nombre, documento, correo, telefono) -> Cliente:
        try:
            cliente = Cliente(nombre, documento, correo, telefono)
            cliente.validarDatos()
            if any(c.obtenerInformacion()["documento"] == cliente.documento for c in self.clientes.values()):
                raise DatosInvalidosError("Ya existe un cliente con ese documento")
            self.clientes[cliente.idCliente] = cliente
            self.logger.registrarEvento("REGISTRAR_CLIENTE", cliente.idCliente)
            return cliente
        except Exception as exc:
            self.logger.registrarError("REGISTRAR_CLIENTE", str(exc), type(exc).__name__)
            if isinstance(exc, DatosInvalidosError):
                raise
            raise DatosInvalidosError(f"No fue posible registrar el cliente: {exc}") from exc

    def listar(self) -> list[Cliente]:
        return list(self.clientes.values())

    def obtener(self, id_cliente: str) -> Cliente:
        try:
            return self.clientes[id_cliente]
        except KeyError as exc:
            self.logger.registrarError("OBTENER_CLIENTE", id_cliente, "RecursoNoEncontrado")
            raise RecursoNoEncontradoError(f"No existe el cliente {id_cliente}") from exc

    def actualizar_correo(self, id_cliente: str, correo: str) -> Cliente:
        cliente = self.obtener(id_cliente)
        try:
            cliente.actualizarCorreo(correo)
            self.logger.registrarEvento("ACTUALIZAR_CORREO", id_cliente)
            return cliente
        except Exception as exc:
            self.logger.registrarError("ACTUALIZAR_CORREO", str(exc), type(exc).__name__)
            raise DatosInvalidosError(str(exc)) from exc

    def actualizar_telefono(self, id_cliente: str, telefono: str) -> Cliente:
        cliente = self.obtener(id_cliente)
        try:
            cliente.actualizarTelefono(telefono)
            self.logger.registrarEvento("ACTUALIZAR_TELEFONO", id_cliente)
            return cliente
        except Exception as exc:
            self.logger.registrarError("ACTUALIZAR_TELEFONO", str(exc), type(exc).__name__)
            raise DatosInvalidosError(str(exc)) from exc

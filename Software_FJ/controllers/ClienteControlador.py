from Software_FJ.exceptions.ExcepcionesPersonalizadas import ErrorDominio


class ClienteControlador:
    def __init__(self, cliente_service):
        self.service = cliente_service

    def registrar(self, nombre, documento, correo, telefono):
        try:
            cliente = self.service.registrar(nombre, documento, correo, telefono)
            return {"exito": True, "datos": cliente.obtenerInformacion()}
        except ErrorDominio as exc:
            return {"exito": False, "error": str(exc)}

    def listar(self):
        return {"exito": True, "datos": [c.obtenerInformacion() for c in self.service.listar()]}

    def actualizar_correo(self, id_cliente, correo):
        try:
            cliente = self.service.actualizar_correo(id_cliente, correo)
            return {"exito": True, "datos": cliente.obtenerInformacion()}
        except ErrorDominio as exc:
            return {"exito": False, "error": str(exc)}

from Software_FJ.exceptions.ExcepcionesPersonalizadas import ErrorDominio


class ServicioControlador:
    def __init__(self, servicio_service):
        self.service = servicio_service

    def registrar(self, servicio):
        try:
            registrado = self.service.registrar(servicio)
            return {"exito": True, "datos": registrado.describirServicio()}
        except ErrorDominio as exc:
            return {"exito": False, "error": str(exc)}

    def listar(self, solo_disponibles=False):
        return {"exito": True, "datos": [s.describirServicio() for s in self.service.listar(solo_disponibles)]}

    def cambiar_disponibilidad(self, id_servicio, disponible):
        try:
            servicio = self.service.cambiar_disponibilidad(id_servicio, disponible)
            return {"exito": True, "datos": servicio.describirServicio()}
        except ErrorDominio as exc:
            return {"exito": False, "error": str(exc)}

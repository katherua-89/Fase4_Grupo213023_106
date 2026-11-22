from Software_FJ.exceptions.ExcepcionesPersonalizadas import ErrorDominio


class ReservaControlador:
    def __init__(self, reserva_service):
        self.service = reserva_service

    def crear(self, id_cliente, id_servicio, duracion):
        try:
            reserva = self.service.crear(id_cliente, id_servicio, duracion)
            return {"exito": True, "datos": reserva.describirReserva()}
        except ErrorDominio as exc:
            return {"exito": False, "error": str(exc)}

    def confirmar(self, id_reserva):
        try:
            reserva = self.service.confirmar(id_reserva)
            return {"exito": True, "datos": reserva.describirReserva()}
        except ErrorDominio as exc:
            return {"exito": False, "error": str(exc)}

    def cancelar(self, id_reserva):
        try:
            reserva = self.service.cancelar(id_reserva)
            return {"exito": True, "datos": reserva.describirReserva()}
        except ErrorDominio as exc:
            return {"exito": False, "error": str(exc)}

    def listar(self):
        return {"exito": True, "datos": [r.describirReserva() for r in self.service.listar()]}

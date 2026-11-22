from Software_FJ.models.Servicio import Servicio


class AsesoriaEspecializada(Servicio):
    def __init__(self, nombre, descripcion, precioBase, disponible, especialidad, costoHora, cantidadHoras):
        super().__init__(nombre, descripcion, precioBase, disponible)
        self.especialidad, self.costoHora, self.cantidadHoras = especialidad, costoHora, cantidadHoras

    def calcularCosto(self, horas=None, descuento=0, impuesto=0):
        horas = self.cantidadHoras if horas is None else horas
        return self.calcularCostoConAjustes(horas, descuento, impuesto) if descuento or impuesto else self.precioBase + self.costoHora * horas

    def describirServicio(self):
        return f"{self.nombre}: {self.especialidad}, {self.costoHora}/hora, {self.cantidadHoras} horas"

    def validarParametros(self):
        if not isinstance(self.especialidad, str) or not self.especialidad.strip() or not isinstance(self.costoHora, (int, float)) or self.costoHora <= 0 or not isinstance(self.cantidadHoras, int) or self.cantidadHoras <= 0:
            raise ValueError("Los parámetros de asesoría no son válidos")
        if not isinstance(self.precioBase, (int, float)) or self.precioBase < 0 or not isinstance(self.disponible, bool):
            raise ValueError("Los costos o disponibilidad no son válidos")
        return True

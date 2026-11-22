from Software_FJ.models.Servicio import Servicio


class ReservarSala(Servicio):
    TIPOS_VALIDOS = {"Pequeña", "Mediana", "Grande"}

    def __init__(self, nombre, descripcion, precioBase, disponible, capacidad, tipoSala, costoHora):
        super().__init__(nombre, descripcion, precioBase, disponible)
        self.capacidad, self.tipoSala, self.costoHora = capacidad, tipoSala, costoHora

    def calcularCosto(self, horas, descuento=0, impuesto=0):
        return self.calcularCostoConAjustes(horas, descuento, impuesto) if descuento or impuesto else self.precioBase + self.costoHora * horas

    def describirServicio(self):
        return f"{self.nombre}: sala {self.tipoSala}, capacidad {self.capacidad}, {self.costoHora}/hora"

    def validarParametros(self):
        if not isinstance(self.capacidad, int) or self.capacidad <= 0 or self.tipoSala not in self.TIPOS_VALIDOS:
            raise ValueError("Los parámetros de sala no son válidos")
        if not isinstance(self.costoHora, (int, float)) or self.costoHora <= 0 or not isinstance(self.precioBase, (int, float)) or self.precioBase < 0 or not isinstance(self.disponible, bool):
            raise ValueError("Los costos o disponibilidad no son válidos")
        return True

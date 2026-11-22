from Software_FJ.models.Servicio import Servicio


class AlquilerEquipo(Servicio):
    TIPOS_VALIDOS = {"Cámara", "Proyector", "Micrófono"}

    def __init__(self, nombre, descripcion, precioBase, disponible, tipoEquipo, costoDia, cantidad):
        super().__init__(nombre, descripcion, precioBase, disponible)
        self.tipoEquipo, self.costoDia, self.cantidad = tipoEquipo, costoDia, cantidad

    def calcularCosto(self, dias, descuento=0, impuesto=0):
        return self.calcularCostoConAjustes(dias, descuento, impuesto) if descuento or impuesto else self.precioBase + self.costoDia * dias

    def describirServicio(self):
        return f"{self.nombre}: {self.tipoEquipo}, {self.costoDia}/día, cantidad {self.cantidad}"

    def validarParametros(self):
        if not isinstance(self.nombre, str) or not self.nombre.strip() or not isinstance(self.descripcion, str) or not self.descripcion.strip():
            raise ValueError("Nombre y descripción son obligatorios")
        if not isinstance(self.precioBase, (int, float)) or self.precioBase < 0 or not isinstance(self.costoDia, (int, float)) or self.costoDia <= 0:
            raise ValueError("Los costos no son válidos")
        if not isinstance(self.disponible, bool) or self.tipoEquipo not in self.TIPOS_VALIDOS or not isinstance(self.cantidad, int) or self.cantidad <= 0:
            raise ValueError("Los parámetros del equipo no son válidos")
        return True

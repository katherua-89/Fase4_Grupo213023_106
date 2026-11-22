from Software_FJ.models.Servicio import Servicio

class AlquilerEquipo(Servicio):
    
    def __init__(self, nombre, descripcion, precioBase, disponible, tipoEquipo, costoDia, cantidad):
        super().__init__(nombre, descripcion, precioBase, disponible)
        self.tipoEquipo = tipoEquipo
        self.costoDia = costoDia
        self.cantidad = cantidad
        
    
    def calcularCosto(self, dias):
        #Se calcula el costo del servicio de alquiler de equipo
        return self.precioBase + (self.costoDia * dias)
    
    
    def describirServicio(self):
        #Se describe el servicio de alquiler de equipo
        return f"Servicio: {self.nombre}, Descripción: {self.descripcion}, Precio Base: {self.precioBase}, Disponible: {self.disponible}, Tipo de Equipo: {self.tipoEquipo}, Costo por Día: {self.costoDia}"
    
    def validarParametros(self):
        #Se validan los parametros del servicio de alquiler de equipo
        if self.costoDia <= 0:
            raise ValueError("El costo por día debe ser mayor a 0")
        if self.tipoEquipo not in ["Cámara", "Proyector", "Micrófono"]:
            raise ValueError("El tipo de equipo debe ser 'Cámara', 'Proyector' o 'Micrófono'")
        if self.precioBase < 0:
            raise ValueError("El precio base no puede ser negativo")
        if not self.nombre or not self.descripcion:
            raise ValueError("El nombre y la descripción no pueden estar vacíos")
        if not isinstance(self.disponible, bool):
            raise ValueError("El valor de disponible debe ser un booleano")
        if not isinstance(self.costoDia, (int, float)):
            raise ValueError("El costo por día debe ser un número")
        if not isinstance(self.tipoEquipo, str):
            raise ValueError("El tipo de equipo debe ser una cadena de texto")
        if not isinstance(self.cantidad, int) or self.cantidad <= 0:
            raise ValueError("La cantidad debe ser un número entero mayor a 0")
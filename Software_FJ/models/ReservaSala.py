from Software_FJ.models.Servicio import Servicio

class ReservarSala(Servicio):
    
    def __init__(self, nombre, descripcion, precioBase, disponible, capacidad, tipoSala, costoHora ):
        super().__init__(nombre, descripcion, precioBase, disponible)
        self.capacidad = capacidad
        self.tipoSala = tipoSala
        self.costoHora = costoHora
        
    
    def calcularCosto(self, horas):
        #Se calcula el costo del servicio de reservar sala
        return self.precioBase + (self.costoHora * horas)
    
    
    def describirServicio(self):
        #Se describe el servicio de reservar sala
        return f"Servicio: {self.nombre}, Descripción: {self.descripcion}, Precio Base: {self.precioBase}, Disponible: {self.disponible}, Tipo de Sala: {self.tipoSala}, Capacidad: {self.capacidad}, Costo por Hora: {self.costoHora}"
    
    def validarParametros(self):
        #Se validan los parametros del servicio de reservar sala
        if self.capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        if self.costoHora <= 0:
            raise ValueError("El costo por hora debe ser mayor a 0")
        if self.tipoSala not in ["Pequeña", "Mediana", "Grande"]:
            raise ValueError("El tipo de sala debe ser 'Pequeña', 'Mediana' o 'Grande'")
        if self.precioBase < 0:
            raise ValueError("El precio base no puede ser negativo")
        if not self.nombre or not self.descripcion:
            raise ValueError("El nombre y la descripción no pueden estar vacíos")
        if not isinstance(self.disponible, bool):
            raise ValueError("El valor de disponible debe ser un booleano")
        if not isinstance(self.capacidad, int):
            raise ValueError("La capacidad debe ser un número entero")
        if not isinstance(self.costoHora, (int, float)):
            raise ValueError("El costo por hora debe ser un número")
        if not isinstance(self.tipoSala, str):
            raise ValueError("El tipo de sala debe ser una cadena de texto")
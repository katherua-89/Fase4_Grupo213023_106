from Software_FJ.models.Servicio import Servicio
class AsesoriaEspecializada(Servicio):
    
    def __init__(self, nombre, descripcion, precioBase, disponible, especialidad, costoHora, cantidadHoras):
        self.__idServicio = f"ASESP-{super()._Servicio__idServicio }"
        super().__init__(nombre, descripcion, precioBase, disponible)
        self.especialidad = especialidad
        self.costoHora = costoHora
        self.cantidadHoras = cantidadHoras
    
    def calcularCosto(self):
        #Se calcula el costo del servicio de asesoria especializada
        return self.precioBase + (self.costoHora * self.cantidadHoras)
    def describirServicio(self):
        #Se describe el servicio de asesoria especializada
        return f"Servicio: {self.nombre}, Descripción: {self.descripcion}, Precio Base: {self.precioBase}, Disponible: {self.disponible}, Especialidad: {self.especialidad}, Costo por Hora: {self.costoHora}, Cantidad de Horas: {self.cantidadHoras}"
    
    def validarParametros(self):
        #Se validan los parametros del servicio de asesoria especializada
        if self.costoHora <= 0:
            raise ValueError("El costo por hora debe ser mayor a 0")
        if self.cantidadHoras <= 0:
            raise ValueError("La cantidad de horas debe ser mayor a 0")
        if not self.especialidad:
            raise ValueError("La especialidad no puede estar vacía")
        if self.precioBase < 0:
            raise ValueError("El precio base no puede ser negativo")
        if not self.nombre or not self.descripcion:
            raise ValueError("El nombre y la descripción no pueden estar vacíos")
        if not isinstance(self.disponible, bool):
            raise ValueError("El valor de disponible debe ser un booleano")
        if not isinstance(self.costoHora, (int, float)):
            raise ValueError("El costo por hora debe ser un número")
        if not isinstance(self.cantidadHoras, int):
            raise ValueError("La cantidad de horas debe ser un número entero")
        
from Software_FJ.models.Entidad import Entidad
class Cliente(Entidad):
    #Se establecen los atributos que se generaran
    
    
    def __init__(self, nombre, documento, correo, telefono):
        self.__idCliente = f"CLI-{super()._Entidad__id }"                   
        self.__fechaCreacion = super()._Entidad__fechaCreacion
        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo
        self.__telefono = telefono

    def validarDatos(self):
        #Se valida que los datos del cliente sean correctos
        if len(self.__nombre) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")
        if len(self.__documento) < 10:
            raise ValueError("El documento debe tener al menos 10 caracteres")
        if len(self.__correo) < 5 or "@" not in self.__correo:
            raise ValueError("El correo debe contener un '@', y se mayor a 5 caracteres")
        if len(self.__telefono) < 10:
            raise ValueError("El teléfono debe tener al menos 10 caracteres")
    def obtenerInformacion(self):
        #Se obtiene la informacion del cliente
        return {
            "idCliente": self.__idCliente,
            "fechaCreacion": self.__fechaCreacion,
            "nombre": self.__nombre,
            "documento": self.__documento,
            "correo": self.__correo,
            "telefono": self.__telefono
        }
    def actualizarCorreo(self, nuevoCorreo):
        #Se actualiza el correo del cliente
        if len(nuevoCorreo) < 5 or "@" not in nuevoCorreo:
            raise ValueError("El correo debe contener un '@', y se mayor a 5 caracteres")
        self.__correo = nuevoCorreo
        return f"El correo del cliente {self.__nombre} ha sido actualizado a {self.__correo}"
    
    def actualizarTelefono(self, nuevoTelefono):
        #Se actualiza el telefono del cliente
        if len(nuevoTelefono) < 10:
            raise ValueError("El teléfono debe tener al menos 10 caracteres")
        self.__telefono = nuevoTelefono
        return f"El teléfono del cliente {self.__nombre} ha sido actualizado a {self.__telefono}"
    
    
    
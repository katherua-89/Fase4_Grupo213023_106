from Software_FJ.models.Entidad import Entidad


class Cliente(Entidad):
    def __init__(self, nombre, documento, correo, telefono):
        super().__init__()
        self.__idCliente = f"CLI-{self.id}"
        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo
        self.__telefono = telefono

    @property
    def idCliente(self):
        return self.__idCliente

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def validarDatos(self):
        if not all(isinstance(v, str) for v in (self.__nombre, self.__documento, self.__correo, self.__telefono)):
            raise ValueError("Los datos del cliente deben ser texto")
        if len(self.__nombre.strip()) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")
        if len(self.__documento.strip()) < 6:
            raise ValueError("El documento debe tener al menos 6 caracteres")
        if len(self.__correo.strip()) < 5 or "@" not in self.__correo:
            raise ValueError("El correo debe contener un '@'")
        if len(self.__telefono.strip()) < 7:
            raise ValueError("El teléfono debe tener al menos 7 caracteres")
        return True

    def obtenerInformacion(self):
        return {"idCliente": self.idCliente, "fechaCreacion": self.fechaCreacion.isoformat(), "nombre": self.nombre,
                "documento": self.documento, "correo": self.correo, "telefono": self.telefono}

    def actualizarCorreo(self, nuevoCorreo):
        if not isinstance(nuevoCorreo, str) or len(nuevoCorreo.strip()) < 5 or "@" not in nuevoCorreo:
            raise ValueError("El correo debe contener un '@'")
        self.__correo = nuevoCorreo
        return self.__correo

    def actualizarTelefono(self, nuevoTelefono):
        if not isinstance(nuevoTelefono, str) or len(nuevoTelefono.strip()) < 7:
            raise ValueError("El teléfono debe tener al menos 7 caracteres")
        self.__telefono = nuevoTelefono
        return self.__telefono

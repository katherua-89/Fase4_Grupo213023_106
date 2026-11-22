from utils.GeneradorId import GeneradorId as gen
class GestorLogs():
    #Atributos de la clase
    __idLog:str
    accion:str
    fecha:str
    descripcionLog:str
    tipoLog:str
    #Se construye un constructor para el log
    def __init__(self, accion, descripcion, tipoLog):
        self.__idLog=f"LOG-{gen.generarId()}"
        self.accion=accion
        self.fecha=str(gen.obtenerFechaActual())
        self.descripcionLog=descripcion
        self.tipoLog=tipoLog
    def describirLog(self):
        #Se describe el log
        return f"Log ID: {self.__idLog}, Acción: {self.accion}, Fecha: {self.fecha}, Descripción: {self.descripcionLog}, Tipo: {self.tipoLog}"
    def registrarLog(self):
        #Se registra el log
        return f"Log registrado: {self.describirLog()}" 
    def registrarEvento(self, evento, descripcion, tipoEvento):
        #Se registra un evento en el log
        self.accion=evento
        self.descripcionLog=descripcion
        self.tipoLog=tipoEvento
        return f"Evento registrado: {self.describirLog()}"
    def registrarError(self, accion, descripcion, tipoError):
        #Se registra un error en el log
        self.accion=accion
        self.descripcionLog=descripcion
        self.tipoLog=tipoError
        return f"Error registrado: {self.describirLog()}"
        
    def consultarLogs(self):
        #Se consultan los logs
        return f"Consultando logs: {self.describirLog()}"
    
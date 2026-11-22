from datetime import datetime
from uuid import uuid4


class GeneradorId:
    @staticmethod
    def generarId() -> str:
        return str(uuid4())

    @staticmethod
    def obtenerFechaActual() -> str:
        return datetime.now().isoformat(timespec="seconds")

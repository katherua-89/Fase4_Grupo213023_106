from __future__ import annotations

import logging
from pathlib import Path


class GestorLogs:
    def __init__(self, ruta: str | Path | None = None):
        self.ruta = Path(ruta or Path(__file__).resolve().parents[2] / "logs" / "software_fj.log")
        self.ruta.parent.mkdir(parents=True, exist_ok=True)
        self._logger = logging.getLogger(f"Software_FJ.{self.ruta}")
        self._logger.setLevel(logging.INFO)
        self._logger.propagate = False
        if not self._logger.handlers:
            handler = logging.FileHandler(self.ruta, encoding="utf-8")
            handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
            self._logger.addHandler(handler)

    def registrarEvento(self, evento: str, descripcion: str, tipoEvento: str = "EVENTO") -> None:
        self._logger.info("%s | %s | %s", tipoEvento, evento, descripcion)

    def registrarError(self, accion: str, descripcion: str, tipoError: str = "ERROR") -> None:
        self._logger.error("%s | %s | %s", tipoError, accion, descripcion)

    def registrarLog(self, accion: str, descripcion: str, tipoLog: str = "INFO") -> None:
        self._logger.info("%s | %s | %s", tipoLog, accion, descripcion)

    def consultarLogs(self) -> str:
        return self.ruta.read_text(encoding="utf-8") if self.ruta.exists() else ""

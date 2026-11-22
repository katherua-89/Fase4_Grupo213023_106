class ErrorDominio(Exception):
    """Error base controlado por la aplicación."""


class DatosInvalidosError(ErrorDominio):
    pass


class RecursoNoEncontradoError(ErrorDominio):
    pass


class OperacionNoPermitidaError(ErrorDominio):
    pass


class ServicioNoDisponibleError(ErrorDominio):
    pass


class ReservaInvalidaError(ErrorDominio):
    pass

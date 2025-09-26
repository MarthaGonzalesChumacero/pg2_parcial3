import re


class ValidadorBase:
    """Valida patrones básicos: números, letras, alfanumérico."""

    _re_numeros = re.compile(r"^[0-9]+$")
    _re_letras = re.compile(r"^[A-Za-zÁÉÍÓÚÑáéíóúñ ]+$")
    _re_alfanumerico = re.compile(r"^[A-Za-z0-9ÁÉÍÓÚÑáéíóúñ _-]+$")

    def validar_solo_numeros(self, valor) -> bool:
        return isinstance(valor, (str, int)) and self._re_numeros.match(str(valor)) is not None

    def validar_solo_letras(self, valor) -> bool:
        return isinstance(valor, str) and self._re_letras.match(valor) is not None

    def validar_alfanumerico(self, valor) -> bool:
        return isinstance(valor, str) and self._re_alfanumerico.match(valor) is not None


class ValidadorDatosPersonales(ValidadorBase):
    """Validaciones de edad, nombre y documento de identidad."""

    def validar_edad(self, edad) -> bool:
        try:
            e = int(edad)
        except Exception:
            return False
        return 0 <= e <= 120

    def validar_nombre(self, nombre) -> bool:
        return self.validar_solo_letras(nombre) and 1 <= len(nombre.strip()) <= 100

    def validar_documento_identidad(self, doc) -> bool:
        doc = str(doc)
        return self.validar_alfanumerico(doc) and 5 <= len(doc) <= 15


class ValidadorDatosContacto(ValidadorBase):
    """Validaciones de email, celular y dirección."""

    _re_email = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    _re_cel = re.compile(r"^(?:\+?\d{7,15}|\d{7,15})$")

    def validar_email(self, email) -> bool:
        return isinstance(email, str) and self._re_email.match(email) is not None

    def validar_celular(self, celular) -> bool:
        return isinstance(celular, (str, int)) and self._re_cel.match(str(celular)) is not None

    def validar_direccion(self, direccion) -> bool:
        return isinstance(direccion, str) and self.validar_alfanumerico(direccion) and 3 <= len(direccion) <= 200

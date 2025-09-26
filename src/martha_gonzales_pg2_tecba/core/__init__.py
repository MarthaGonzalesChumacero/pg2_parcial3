from dataclasses import dataclass
from ..validators import ValidadorDatosContacto, ValidadorDatosPersonales


@dataclass(frozen=True)
class Persona:
    nombre: str
    edad: int
    documento: str
    email: str
    celular: str
    direccion: str

    @staticmethod
    def builder():
        return _PersonaBuilder()


class _PersonaBuilder:
    def __init__(self):
        self._vper = ValidadorDatosPersonales()
        self._vcon = ValidadorDatosContacto()
        self._nombre = None
        self._edad = None
        self._documento = None
        self._email = None
        self._celular = None
        self._direccion = None

    # ---- Datos personales
    def con_nombre(self, nombre: str):
        if not self._vper.validar_nombre(nombre):
            raise ValueError("Nombre inválido")
        self._nombre = nombre.strip()
        return self

    def con_edad(self, edad: int):
        if not self._vper.validar_edad(edad):
            raise ValueError("Edad inválida")
        self._edad = int(edad)
        return self

    def con_documento(self, documento: str):
        if not self._vper.validar_documento_identidad(documento):
            raise ValueError("Documento inválido")
        self._documento = str(documento)
        return self

    # ---- Datos de contacto
    def con_email(self, email: str):
        if not self._vcon.validar_email(email):
            raise ValueError("Email inválido")
        self._email = email.strip()
        return self

    def con_celular(self, celular: str):
        if not self._vcon.validar_celular(celular):
            raise ValueError("Celular inválido")
        self._celular = str(celular)
        return self

    def con_direccion(self, direccion: str):
        if not self._vcon.validar_direccion(direccion):
            raise ValueError("Dirección inválida")
        self._direccion = direccion.strip()
        return self

    def build(self) -> Persona:
        faltan = [k for k, v in {
            "nombre": self._nombre, "edad": self._edad, "documento": self._documento,
            "email": self._email, "celular": self._celular, "direccion": self._direccion
        }.items() if v is None]
        if faltan:
            raise ValueError(f"Campos faltantes: {', '.join(faltan)}")
        return Persona(
            nombre=self._nombre, edad=self._edad, documento=self._documento,
            email=self._email, celular=self._celular, direccion=self._direccion
        )

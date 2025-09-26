import pytest
from martha_gonzales_pg2_tecba.core import Persona


def test_persona_builder_valido():
    p = (Persona.builder()
         .con_nombre("Martha Gonzales")
         .con_edad(25)
         .con_documento("1234567")
         .con_email("martha@example.com")
         .con_celular("+59170000000")
         .con_direccion("Av Siempre Viva 123")
         .build())
    assert p.nombre == "Martha Gonzales"
    assert p.edad == 25


def test_persona_builder_invalido():
    builder = Persona.builder()
    try:
        builder.con_email("no-es-email")
        assert False, "Debió fallar con un email inválido"
    except ValueError:
        assert True

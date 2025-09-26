
# **PG2_PARCIALL3**

## **martha_gonzales_pg2_tecba (v0.0.1)**

Librería de Python para la validación de datos personales y de contacto, y la gestión de objetos `Persona` mediante el patrón **Builder**. Este proyecto fue desarrollado como parte de una tarea académica para el curso PG2 (TECBA).

---

### **1. Instalación**

Para instalar la librería desde el entorno de prueba de **TestPyPI**, utiliza el siguiente comando:

```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps martha-gonzales-pg2-tecba==0.0.1
```

**Nota**: Si necesitas otras dependencias que no estén en **TestPyPI**, puedes agregarlas con `--extra-index-url https://pypi.org/simple`.

---

### **2. Uso básico**

Aquí te mostramos cómo usar la librería para construir un objeto **`Persona`** con el patrón **Builder**:

```python
from martha_gonzales_pg2_tecba.core import Persona

try:
    # Crear una persona válida
    persona = (Persona.builder()
               .con_nombre("Martha Gonzales")
               .con_edad(25)
               .con_documento("1234567")
               .con_email("martha@example.com")
               .con_celular("+59170000000")
               .con_direccion("Av Siempre Viva 123")
               .build())

    print("¡Persona creada con éxito!")
    print(persona)

    # Intento con datos inválidos
    print("\nIntentando crear persona con datos inválidos...")
    Persona.builder() \
        .con_nombre("Martha") \
        .con_edad(150) \
        .con_documento("abc") \
        .build()

except ValueError as e:
    print(f"Error de validación: {e}")

```

**Salida esperada:**
```python
Persona(nombre='Martha Gonzales', edad=25, documento='1234567', 
        email='martha@example.com', celular='+59170000000', 
        direccion='Av Siempre Viva 123')
```

---

### **3. Módulos incluidos**

#### **`core`**
- **`Persona`**: Clase principal implementada con el patrón **Builder** para la construcción segura de objetos `Persona`.

#### **`validators`**
- **`ValidadorBase`**: Valida datos alfanuméricos, números y letras.
- **`ValidadorDatosPersonales`**: Valida campos como nombre, documento de identidad y edad.
- **`ValidadorDatosContacto`**: Valida los datos de contacto como email, celular y dirección.

---

### **4. Ejemplo de uso y validación**

Este es un ejemplo completo de cómo la librería valida y crea un objeto `Persona`:

```python
from martha_gonzales_pg2_tecba.validators import ValidadorDatosPersonales, ValidadorDatosContacto

# Validación de datos personales
validar_persona = ValidadorDatosPersonales("Martha Gonzales", 25, "1234567")
validar_persona.validar()

# Validación de datos de contacto
validar_contacto = ValidadorDatosContacto("martha@example.com", "+59170000000", "Av Siempre Viva 123")
validar_contacto.validar()
```

**Nota**: Los métodos `validar()` lanzarán una excepción `ValueError` si los datos no son válidos.

---

### **5. Pruebas**

Este proyecto incluye pruebas automáticas utilizando **pytest**. Para ejecutarlas en la raíz del proyecto, usa:

```bash
pytest
```

---

### **6. Estructura del proyecto**

La estructura del proyecto es la siguiente:

```
pg2_parcial3/
│
├── src/
│   └── martha_gonzales_pg2_tecba/
│       ├── core/
│       │   └── __init__.py
│       └── validators/
│           └── __init__.py
│
├── tests/
│   └── test_persona.py
│
├── setup.cfg
├── pyproject.toml
├── README.md
└── requirements.txt

```

### **7. Licencia**

Este proyecto se distribuye bajo la licencia **MIT**.


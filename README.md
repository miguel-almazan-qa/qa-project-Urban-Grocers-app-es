# Proyecto de Automatización API - Urban Grocers

## Descripción
Este proyecto automatiza la suite de pruebas para validar el comportamiento del campo `name` en el endpoint de creación de kits de productos (`POST /api/v1/kits`) de la aplicación Urban Grocers.

## Fuente de Documentación
- API Documentation: Urban Grocers API Docs (`/docs/`)

## Tecnologías y Técnicas Utilizadas
- **Python 3.10+**: Lenguaje principal de programación.
- **Pytest**: Framework para ejecución y aserciones de pruebas automatizadas.
- **Requests**: Librería HTTP para interacción con la API REST.
- **Git y GitHub**: Control de versiones y repositorio remoto.

## Estructura del Proyecto
- `configuration.py`: Almacena la URL base y rutas de la API.
- `data.py`: Contiene los cuerpos de solicitud JSON y encabezados HTTP base.
- `sender_stand_request.py`: Módulos y funciones para el envío de peticiones HTTP.
- `create_kit_name_kit_test.py`: Casos de prueba automatizados con Pytest.
- `README.md`: Documentación del proyecto.
- `.gitignore`: Archivo de configuración para exclusión de archivos no deseados en Git.

## Instrucciones de Ejecución
1. Instala las dependencias:
   `pip install pytest requests`
2. Inicia el servidor de Urban Grocers y actualiza `URL_SERVICE` en `configuration.py`.
3. Ejecuta la suite de pruebas en la terminal:
   `pytest create_kit_name_kit_test.py`
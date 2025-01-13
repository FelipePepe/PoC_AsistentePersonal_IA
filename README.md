# Asistente Personal basado en IA

Este proyecto implementa un **asistente personal** que procesa correos electrónicos y realiza tareas como la gestión de correos, agendamiento de eventos y organización de tareas utilizando modelos de lenguaje a través de **Ollama** y **LangChain**.

## Descripción

El asistente personal es capaz de:

- Leer correos electrónicos.
- Procesar los correos para extraer información relevante.
- Responder correos electrónicos de manera automatizada.
- Agendar eventos o recordatorios.
- Organizar tareas y hacer recomendaciones.

### Flujo general del sistema:

1. **Conexión a un servidor de correo**: Utiliza IMAP para acceder a los correos electrónicos desde una cuenta configurada.
2. **Procesamiento de correos con Ollama**: Los correos se procesan utilizando un modelo de lenguaje (por ejemplo, `llama-3.2`) para extraer información relevante o sugerir acciones.
3. **Generación de respuestas**: Basado en el análisis del correo, el modelo sugiere acciones como responder el correo o agendar eventos.

## Requisitos

- **Python 3.12** o superior.
- **Ollama**: Un servidor de modelos de lenguaje. Asegúrate de tenerlo instalado y en funcionamiento.
- **LangChain**: Usado para crear flujos de trabajo con el modelo de lenguaje.
- **IMAP**: Para acceder a la bandeja de entrada de tu correo electrónico.
- **Dependencias**:
    - `requests`
    - `langchain`
    - `decouple`
    - `email`
    - `imaplib`

### Instalación de dependencias

```bash
pip install requests langchain decouple
```

## Configuración

1. Ollama:
* Instala y ejecuta Ollama en tu máquina. Debe estar accesible en http://localhost:11434.
* Asegúrate de que el modelo (por ejemplo, llama-3.2) esté disponible en tu instancia de Ollama.

2. Variables de entorno:
* Configura tu correo electrónico y contraseña en variables de entorno para acceder a tu cuenta de correo de manera segura.
* Crea un archivo .env con las siguientes líneas:

```env
EMAIL=tu_correo@example.com
EMAIL_PASSWORD=tu_contraseña
```

## Estructura del Proyecto
El código está dividido en tres archivos principales:
1. main.py
Este archivo es el punto de entrada para el asistente personal. Se encarga de:

* Conectar al servidor de correo utilizando IMAP.
* Leer los correos electrónicos.
* Pasar cada correo a través de un modelo de lenguaje para su procesamiento.

2. ollama_utils.py
Este archivo se encarga de interactuar con el servidor Ollama, que ejecuta el modelo de lenguaje y procesa el contenido de los correos.

3. email_utils.py
Este archivo se encarga de conectar con el servidor smtp y descargar los correos.

## Cómo usar
1. Ejecutar el servidor de Ollama:

* Asegúrate de tener Ollama corriendo en tu máquina, escuchando en http://localhost:11434.

2. Configura tu correo:

* Asegúrate de tener las variables de entorno EMAIL y EMAIL_PASSWORD configuradas correctamente.

3. Ejecuta el Asistente Personal:

* Corre el archivo main.py

4. Ver resultados.

* El asistente procesará los correos electrónicos y mostrará en la consola las respuestas generadas por el modelo del lenguaje.

## Notas
Este proyecto está diseñado como una prueba de concepto. Puedes extenderlo para agregar más funcionalidades como integración con calendarios o tareas.
Si estás ejecutando Ollama en un entorno diferente, asegúrate de ajustar la configuración de base_url para apuntar a la URL correcta del servidor.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

from email_utils import iniciar_sesion_imap, leer_correos
from ollama_utils import consultar_ollama
from decouple import config

def procesar_correos_con_ia(correos):
    """
    Procesa los correos utilizando IA para analizarlos.
    """
    for correo in correos:
        print(f"De: {correo['remitente']}")
        print(f"Asunto: {correo['asunto']}")
        
        # Resumir y analizar el correo con Ollama
        prompt = (
            f"Este es un correo electrónico. Ayúdame a identificar lo importante:\n\n"
            f"Asunto: {correo['asunto']}\n"
            f"Cuerpo: {correo['cuerpo']}\n\n"
            f"1. ¿Cuál es el propósito del correo?\n"
            f"2. Resume el contenido en una oración.\n"
            f"3. ¿Debería responder a este correo? Si es así, sugiere una respuesta breve."
        )
        respuesta_ia = consultar_ollama(prompt)
        print(f"IA dice:\n{respuesta_ia}")

if __name__ == "__main__":
    # Usar variables de entorno para la seguridad
    usuario = config("EMAIL")
    password = config("EMAIL_PASSWORD")
    
    if not usuario or not password:
        print("Configura las variables de entorno EMAIL y EMAIL_PASSWORD.")
        exit(1)
    
    # Conectar al servidor de correo
    servidor = iniciar_sesion_imap(usuario, password)
    correos = leer_correos(servidor)

    # Cerrar la sesión
    servidor.logout()

    # Procesar correos con IA
    procesar_correos_con_ia(correos)
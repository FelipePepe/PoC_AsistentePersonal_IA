import imaplib
import email

def iniciar_sesion_imap(usuario, password):
    """
    Inicia sesión en el servidor IMAP.
    """
    servidor = imaplib.IMAP4_SSL("imap.gmail.com")
    servidor.login(usuario, password)
    return servidor

def leer_correos(servidor, carpeta="INBOX"):
    """
    Lee los correos electrónicos de una carpeta específica.
    """
    servidor.select(carpeta)
    _, mensajes = servidor.search(None, "ALL")
    ids = mensajes[0].split()
    correos = []
    
    for id_ in ids[-10:]:  # Leer los últimos 10 correos
        _, datos = servidor.fetch(id_, "(RFC822)")
        raw_email = datos[0][1]
        mensaje = email.message_from_bytes(raw_email)
        remitente = mensaje["From"]
        asunto = mensaje["Subject"]
        
        # Procesar el contenido del mensaje
        cuerpo = ""
        if mensaje.is_multipart():
            for parte in mensaje.walk():
                if parte.get_content_type() == "text/plain":
                    charset = parte.get_content_charset() or "utf-8"
                    cuerpo = parte.get_payload(decode=True).decode(charset, errors="replace")
                    break
        else:
            charset = mensaje.get_content_charset() or "utf-8"
            cuerpo = mensaje.get_payload(decode=True).decode(charset, errors="replace")
        
        correos.append({"remitente": remitente, "asunto": asunto, "cuerpo": cuerpo})
    return correos

from langchain.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM

def consultar_ollama(prompt_input, modelo="llama2", base_url="http://localhost:11434"):
    # Define el PromptTemplate para un asistente personal
    po_prompt = PromptTemplate(
        template=(
            "Eres un asistente personal muy eficiente. Puedes ayudarme con tareas como gestionar correos electrónicos, "
            "organizar mi calendario, recordarme cosas importantes y ayudarme con mis tareas diarias.\n\n"
            "Aquí están las instrucciones específicas que debes seguir para cada tarea:\n"
            "1. Si el correo que recibiste es importante, responde con una breve descripción de su contenido.\n"
            "2. Si necesitas agendar algo, escribe el evento con formato: 'Evento: Título | Fecha | Hora'.\n"
            "3. Si hay tareas pendientes, organiza y agrégalas a una lista de tareas, separadas por comas.\n"
            "4. Si se requiere una acción o respuesta, proporciona una sugerencia clara y breve.\n\n"
            "Tarea/Correo a procesar: {input}"
        ),
        input_variables=["input"]
    )
    
    # Prepara el prompt con el input del usuario
    prompt = po_prompt.format(input=prompt_input)
    
    # Usar OllamaLLM con el modelo y base_url
    po_llm = OllamaLLM(model=modelo, base_url=base_url)
    
    # Procesar la cadena y obtener la respuesta
    try:
        response = po_llm.invoke(prompt)
        return response
    except Exception as e:
        print(f"Error en la solicitud a Ollama: {e}")
    return None

from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# ===============================================
# MENSAJES DE RESPALDO
# ===============================================

MENSAJES = {

    "es": "¡Bienvenido a POP Turismo! Hemos encontrado varias recomendaciones para tu viaje. Explora las opciones disponibles a continuación.",

    "en": "Welcome to POP Turismo! We have found several recommendations for your trip. Explore the available options below.",

    "fr": "Bienvenue sur POP Turismo ! Nous avons trouvé plusieurs recommandations pour votre voyage. Découvrez-les ci-dessous.",

    "pt": "Bem-vindo ao POP Turismo! Encontramos várias recomendações para sua viagem. Explore as opções abaixo.",

    "de": "Willkommen bei POP Turismo! Wir haben mehrere Empfehlungen für Ihre Reise gefunden. Entdecken Sie die folgenden Optionen.",

    "it": "Benvenuto su POP Turismo! Abbiamo trovato diversi suggerimenti per il tuo viaggio. Scopri le opzioni qui sotto."

}


# ===============================================
# GENERAR MENSAJE
# ===============================================

def generar_mensaje(

    codigo_idioma,

    idioma,

    ciudad,

    tipo,

    presupuesto,

    dias,

    viajeros,

    transporte,

    intereses,

    hoteles,

    restaurantes,

    actividades

):

    prompt = f"""
You are an expert tourism assistant for an airport digital kiosk.

The traveler selected the language:

{idioma}

IMPORTANT RULES

Respond ONLY in {idioma}.

Write naturally.

Be friendly.

Maximum 120 words.

Do NOT use bullet points.

Do NOT create lists.

Do NOT mention hotel names.

Do NOT mention restaurant names.

Do NOT mention activity names.

The recommendations will be displayed visually below your message.

Traveler information

Destination: {ciudad}

Travel type: {tipo}

Budget: {presupuesto}

Travel duration: {dias} days

Travelers: {viajeros}

Transportation: {transporte}

Main interest: {intereses}

The system found:

{len(hoteles)} hotels

{len(restaurantes)} restaurants

{len(actividades)} tourist activities.

Generate only one welcoming paragraph inviting the traveler to explore the recommendations shown below.
"""

    try:

        respuesta = client.responses.create(

            model="gpt-5",

            input=prompt

        )

        return respuesta.output_text.strip()

    except Exception as e:

        print(f"Error OpenAI: {e}")

        return MENSAJES.get(
            codigo_idioma,
            MENSAJES["es"]
        )

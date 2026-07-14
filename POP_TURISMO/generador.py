from openai import OpenAI
import os


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generar_mensaje(
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
Eres un asesor turístico profesional.

El usuario viajará con las siguientes características:

Ciudad: {ciudad}
Idioma: {idioma}
Tipo de viaje: {tipo}
Presupuesto: {presupuesto}
Duración: {dias} días
Viajeros: {viajeros}
Transporte: {transporte}
Intereses: {intereses}

Encontré:

- {len(hoteles)} hoteles
- {len(restaurantes)} restaurantes
- {len(actividades)} actividades

Genera únicamente un mensaje de bienvenida.

NO enumeres hoteles.

NO enumeres restaurantes.

NO enumeres actividades.

NO hagas listas.

Solo escribe un párrafo amigable (máximo 120 palabras) invitando al usuario a revisar las recomendaciones que aparecerán a continuación.

Respeta el idioma seleccionado.
"""

    try:

        respuesta = client.responses.create(

            model="gpt-5",

            input=prompt

        )

        return respuesta.output_text

    except Exception:

        # Respaldo cuando la IA no esté disponible

        idiomas = {

            "Español":
                f"¡Bienvenido! Encontré varias recomendaciones para tu viaje a {ciudad}. A continuación podrás explorar hoteles, restaurantes y actividades seleccionadas según tus preferencias.",

            "English":
                f"Welcome! I found several recommendations for your trip to {ciudad}. Below you can explore hotels, restaurants and activities tailored to your preferences.",

            "Français":
                f"Bienvenue ! J'ai trouvé plusieurs recommandations pour votre voyage à {ciudad}. Vous pouvez découvrir ci-dessous des hôtels, restaurants et activités adaptés à vos préférences.",

            "Português":
                f"Bem-vindo! Encontrei várias recomendações para sua viagem a {ciudad}. A seguir você poderá explorar hotéis, restaurantes e atividades de acordo com suas preferências."

        }

        return idiomas.get(
            idioma,
            idiomas["Español"]
        )

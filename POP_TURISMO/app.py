from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# ==========================
# CONFIGURACIÓN OPENAI
# ==========================

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# ==========================
# PÁGINA PRINCIPAL
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# RECOMENDADOR
# ==========================

@app.route("/recommend", methods=["POST"])
def recommend():

    try:

        data = request.get_json()

        ciudad = data.get("ciudad", "")
        idioma = data.get("idioma", "Español")
        presupuesto = data.get("presupuesto", "")
        intereses = data.get("intereses", "")
        tipo = data.get("tipo", "")
        dias = data.get("dias", "")
        viajeros = data.get("viajeros", "")
        transporte = data.get("transporte", "")

        prompt = f"""
Eres POP Turismo, un guía turístico profesional, experto en turismo nacional e internacional.

El usuario viajará a:

Destino: {ciudad}

Idioma: {idioma}

Tipo de viaje: {tipo}

Presupuesto: {presupuesto}

Intereses: {intereses}

Duración: {dias} días

Viajeros: {viajeros}

Transporte: {transporte}

Tu misión es conversar con el viajero como si fueras un asesor turístico de lujo.

NO escribas listas enormes.

NO respondas como un robot.

La respuesta debe sentirse natural.

Utiliza pequeños párrafos.

Utiliza emojis únicamente para separar secciones.

La estructura será:

👋 Bienvenida

Explica por qué el destino es una excelente elección.

🏨 Alojamiento

Recomienda tres hoteles.

Describe cada uno.

Incluye un rango aproximado de precios.

🍽 Gastronomía

Habla de cinco restaurantes.

Explica qué comer en cada uno.

Recomienda platos típicos.

🎯 Actividades

Describe cinco actividades imperdibles.

Explica cuánto tiempo toma cada una.

Menciona el mejor horario para realizarlas.

🚖 Transporte

Explica cómo desplazarse.

Da costos aproximados.

🌤 Clima

Explica cómo estará el clima.

Recomienda qué ropa llevar.

💡 Consejos

Da recomendaciones de seguridad.

Consejos culturales.

Lugares que vale la pena visitar.

Lugares que debería evitar.

🎉 Despedida

Finaliza deseándole un excelente viaje.

Toda la respuesta debe estar escrita completamente en {idioma}.

Escribe de forma elegante y conversacional.
"""

        response = client.responses.create(
            model="gpt-5",
            input=prompt,
            temperature=0.9,
            max_output_tokens=1800
        )

        return jsonify({
            "respuesta": response.output_text
        })

    except Exception as e:

        return jsonify({
            "respuesta": f"""
⚠ Ocurrió un error.

Detalle:

{str(e)}

Verifica:

• API Key

• Conexión

• Cuota disponible
"""
        }), 500


# ==========================
# HEALTH CHECK
# ==========================

@app.route("/health")
def health():

    return jsonify({
        "status": "ok"
    })


# ==========================
# MAIN
# ==========================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )
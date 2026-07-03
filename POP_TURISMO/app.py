from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Cliente de OpenAI usando la variable de entorno de Render
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    data = request.get_json()

    idioma = data.get("idioma")
    ciudad = data.get("ciudad")
    presupuesto = data.get("presupuesto")
    intereses = data.get("intereses")
    tipo = data.get("tipo")
    dias = data.get("dias")
    viajeros = data.get("viajeros")
    transporte = data.get("transporte")

    prompt = f"""
Eres un experto en turismo del destino {ciudad}.

Acabas de recibir un turista en el aeropuerto.

Información del viajero:

• Ciudad destino: {ciudad}
• Idioma: {idioma}
• Tipo de viaje: {tipo}
• Presupuesto: {presupuesto}
• Intereses: {intereses}
• Duración: {dias} días
• Número de viajeros: {viajeros}
• Transporte: {transporte}

Genera recomendaciones personalizadas.

Organiza la respuesta exactamente así:

🏨 ALOJAMIENTO
- 3 hoteles recomendados
- Precio aproximado por noche
- Zona donde se ubican
- Explica por qué son adecuados

🍽 GASTRONOMÍA
- 5 restaurantes
- Tipo de comida
- Precio aproximado
- Plato recomendado

🎯 ACTIVIDADES
- 5 actividades
- Tiempo estimado
- Costo aproximado
- Horario recomendado

🚖 TRANSPORTE
- Cómo desplazarse
- Costos aproximados

💡 CONSEJOS
- Seguridad
- Clima
- Recomendaciones útiles

Responde completamente en {idioma}.
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return jsonify({
        "respuesta": response.output_text
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
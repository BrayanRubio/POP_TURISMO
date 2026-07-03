from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Cliente de OpenAI (la API Key debe estar configurada en Render)
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
Eres un asesor turístico profesional especializado en la ciudad de {ciudad}.

El viajero tiene la siguiente información:

- Idioma: {idioma}
- Ciudad destino: {ciudad}
- Tipo de viaje: {tipo}
- Presupuesto: {presupuesto}
- Intereses: {intereses}
- Duración: {dias} días
- Número de viajeros: {viajeros}
- Transporte preferido: {transporte}

Genera una guía turística completa y organizada.

Utiliza formato Markdown.

La respuesta debe contener exactamente estas secciones:

# 🏨 Hoteles recomendados

Para cada hotel indica:

- Nombre
- Categoría (⭐⭐⭐⭐⭐)
- Precio aproximado por noche
- Zona
- ¿Por qué lo recomiendas?

# 🍽 Restaurantes

Para cada restaurante indica:

- Nombre
- Tipo de comida
- Plato recomendado
- Precio aproximado

# 🎯 Actividades

Para cada actividad indica:

- Nombre
- Duración
- Costo aproximado
- Horario recomendado

# 🚖 Transporte

Explica:

- Cómo movilizarse
- Costos aproximados
- Recomendaciones

# 🌤 Clima

Describe el clima habitual para esos días.

# 💵 Presupuesto estimado

Haz una estimación del costo total del viaje.

# 💡 Consejos útiles

Incluye recomendaciones de seguridad, horarios, clima y cultura.

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
    app.run(host="0.0.0.0", port=5000, debug=True)
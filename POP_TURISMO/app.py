from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Cargar bases de datos
with open("data/hoteles.json", encoding="utf-8") as f:
    hoteles = json.load(f)

with open("data/restaurantes.json", encoding="utf-8") as f:
    restaurantes = json.load(f)

with open("data/actividades.json", encoding="utf-8") as f:
    actividades = json.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    data = request.get_json()

    ciudad = data.get("ciudad", "").lower()
    presupuesto = data.get("presupuesto", "").lower()
    intereses = data.get("intereses", "").lower()

    # FILTRAR DATOS
    hoteles_filtrados = [
        h for h in hoteles
        if h["ciudad"].lower() == ciudad
    ]

    restaurantes_filtrados = [
        r for r in restaurantes
        if r["ciudad"].lower() == ciudad
    ]

    actividades_filtradas = [
        a for a in actividades
        if a["ciudad"].lower() == ciudad
    ]

    # RESPUESTA
    return jsonify({
        "hoteles": hoteles_filtrados[:5],
        "restaurantes": restaurantes_filtrados[:5],
        "actividades": actividades_filtradas[:5]
    })


if __name__ == "__main__":
    app.run(debug=True)
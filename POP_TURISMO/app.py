from flask import Flask, render_template, request, jsonify

from motor import generar_recomendacion

app = Flask(__name__)


# ==========================================
# PÁGINA PRINCIPAL
# ==========================================

@app.route("/")
def index():
    return render_template("index.html")


# ==========================================
# RECOMENDADOR
# ==========================================

@app.route("/recommend", methods=["POST"])
def recommend():

    try:

        datos = request.get_json()

        respuesta = generar_recomendacion(datos)

        return jsonify({
            "success": True,
            "respuesta": respuesta
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "respuesta": "Ha ocurrido un error.",
            "error": str(e)
        }), 500


# ==========================================
# HEALTH CHECK
# ==========================================

@app.route("/health")
def health():

    return jsonify({

        "status": "ok",

        "app": "POP Turismo",

        "version": "2.0"

    })


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )
from flask import Flask, render_template, request, jsonify

from motor import generar_recomendacion

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    try:

        datos = request.get_json()

        resultado = generar_recomendacion(datos)

        return jsonify({

            "success": True,

            "mensaje": resultado["mensaje"],

            "hoteles": resultado["hoteles"],

            "restaurantes": resultado["restaurantes"],

            "actividades": resultado["actividades"]

        })

    except Exception as e:

        return jsonify({

            "success": False,

            "error": str(e)

        }),500


if __name__=="__main__":

    app.run(debug=True)

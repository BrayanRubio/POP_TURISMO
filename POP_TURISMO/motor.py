from buscador import obtener_recomendaciones, ciudad_disponible
from generador import generar_guia


def generar_recomendacion(datos):

    # ===============================
    # DATOS DEL USUARIO
    # ===============================

    ciudad = datos.get("ciudad", "").strip()

    idioma = datos.get("idioma", "Español")

    presupuesto = datos.get("presupuesto", "")

    intereses = datos.get("intereses", "")

    tipo = datos.get("tipo", "")

    dias = datos.get("dias", "")

    viajeros = datos.get("viajeros", "")

    transporte = datos.get("transporte", "")

    # ===============================
    # VALIDACIONES
    # ===============================

    if ciudad == "":

        return "⚠ Debes seleccionar una ciudad."

    if not ciudad_disponible(ciudad):

        return f"No encontré información turística disponible para {ciudad}."

    # ===============================
    # CONSULTAR BASE LOCAL
    # ===============================

    recomendaciones = obtener_recomendaciones(

        ciudad,

        presupuesto

    )

    hoteles = recomendaciones["hoteles"]

    restaurantes = recomendaciones["restaurantes"]

    actividades = recomendaciones["actividades"]

    # ===============================
    # GENERAR RESPUESTA
    # ===============================

    respuesta = generar_guia(

        ciudad=ciudad,

        idioma=idioma,

        presupuesto=presupuesto,

        intereses=intereses,

        tipo=tipo,

        dias=dias,

        viajeros=viajeros,

        transporte=transporte,

        hoteles=hoteles,

        restaurantes=restaurantes,

        actividades=actividades

    )

    return respuesta
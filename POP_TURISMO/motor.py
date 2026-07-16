import json
import os

from buscador import (
    buscar_hoteles,
    buscar_restaurantes,
    buscar_actividades
)

from generador import generar_mensaje


# ======================================================
# RUTAS
# ======================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RUTA_HOTELES = os.path.join(BASE_DIR, "data", "hoteles.json")
RUTA_RESTAURANTES = os.path.join(BASE_DIR, "data", "restaurantes.json")
RUTA_ACTIVIDADES = os.path.join(BASE_DIR, "data", "actividades.json")


# ======================================================
# CARGAR JSON
# ======================================================

def cargar_json(ruta):

    with open(ruta, encoding="utf-8") as archivo:
        return json.load(archivo)


# ======================================================
# GENERAR RECOMENDACIÓN
# ======================================================

def generar_recomendacion(datos):

    # ------------------------------------------
    # Código del idioma recibido desde el HTML
    # ------------------------------------------

    codigo_idioma = datos.get("idioma", "es")

    idiomas = {
        "es": "Spanish",
        "en": "English",
        "fr": "French",
        "pt": "Portuguese",
        "de": "German",
        "it": "Italian"
    }

    idioma = idiomas.get(codigo_idioma, "Spanish")

    # ------------------------------------------
    # Datos del formulario
    # ------------------------------------------

    ciudad = datos.get("ciudad", "")

    presupuesto = datos.get("presupuesto", "Medio")

    tipo = datos.get("tipo", "")

    intereses = datos.get("intereses", "")

    dias = int(datos.get("dias") or 1)

    viajeros = int(datos.get("viajeros") or 1)

    transporte = datos.get("transporte", "")

    fecha_inicio = datos.get("fecha_inicio", "")

    fecha_fin = datos.get("fecha_fin", "")

    # ------------------------------------------
    # Cargar bases
    # ------------------------------------------

    hoteles_bd = cargar_json(RUTA_HOTELES)

    restaurantes_bd = cargar_json(RUTA_RESTAURANTES)

    actividades_bd = cargar_json(RUTA_ACTIVIDADES)

    # ------------------------------------------
    # Buscar recomendaciones
    # ------------------------------------------

    hoteles = buscar_hoteles(
        hoteles_bd,
        ciudad,
        presupuesto,
        fecha_inicio,
        fecha_fin
    )

    restaurantes = buscar_restaurantes(
        restaurantes_bd,
        ciudad,
        presupuesto
    )

    actividades = buscar_actividades(
        actividades_bd,
        ciudad,
        intereses
    )

    # ------------------------------------------
    # Generar mensaje con IA
    # ------------------------------------------

    mensaje = generar_mensaje(

        codigo_idioma=codigo_idioma,

        idioma=idioma,

        ciudad=ciudad,

        tipo=tipo,

        presupuesto=presupuesto,

        dias=dias,

        viajeros=viajeros,

        transporte=transporte,

        intereses=intereses,

        hoteles=hoteles,

        restaurantes=restaurantes,

        actividades=actividades

    )

    # ------------------------------------------
    # Respuesta
    # ------------------------------------------

    return {

        "mensaje": mensaje,

        "hoteles": hoteles,

        "restaurantes": restaurantes,

        "actividades": actividades

    }

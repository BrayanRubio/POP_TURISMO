from datetime import datetime


IDIOMAS = ["es", "en", "fr", "pt", "de", "it"]

PRESUPUESTOS = ["Económico", "Medio", "Alto"]

TIPOS_VIAJE = [
    "Vacaciones",
    "Negocios",
    "Familia",
    "Mochilero",
    "Romántico",
    "Aventura"
]


def validar_idioma(idioma):

    return idioma in IDIOMAS


def validar_presupuesto(presupuesto):

    return presupuesto in PRESUPUESTOS


def validar_tipo(tipo):

    return tipo in TIPOS_VIAJE


def validar_viajeros(viajeros):

    try:

        viajeros = int(viajeros)

        return viajeros > 0

    except:

        return False


def validar_dias(dias):

    try:

        dias = int(dias)

        return dias > 0

    except:

        return False


def validar_fechas(inicio, fin):

    if not inicio or not fin:

        return False

    try:

        fecha1 = datetime.strptime(inicio,"%Y-%m-%d")

        fecha2 = datetime.strptime(fin,"%Y-%m-%d")

        return fecha2 >= fecha1

    except:

        return False


def validar_ciudad(ciudad):

    return len(ciudad.strip()) > 0

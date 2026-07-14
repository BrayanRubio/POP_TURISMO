from datetime import datetime
from urllib.parse import quote


# ===============================================
# PRECIOS
# ===============================================

def formatear_precio(valor):
    """
    Convierte:
    350000

    en

    $350.000 COP
    """

    try:
        return f"${valor:,.0f} COP".replace(",", ".")
    except:
        return "$0 COP"


# ===============================================
# FECHAS
# ===============================================

def validar_fechas(fecha_inicio, fecha_fin):

    if not fecha_inicio or not fecha_fin:
        return False

    try:

        inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")

        fin = datetime.strptime(fecha_fin, "%Y-%m-%d")

        return fin >= inicio

    except:

        return False


def calcular_dias(fecha_inicio, fecha_fin):

    try:

        inicio = datetime.strptime(fecha_inicio,"%Y-%m-%d")

        fin = datetime.strptime(fecha_fin,"%Y-%m-%d")

        return (fin-inicio).days

    except:

        return 0


# ===============================================
# GOOGLE MAPS
# ===============================================

def url_google_maps(latitud,longitud):

    return f"https://www.google.com/maps?q={latitud},{longitud}"


# ===============================================
# WHATSAPP
# ===============================================

def url_whatsapp(numero,nombre):

    mensaje = quote(

        f"Hola, estoy interesado en obtener información sobre {nombre}."

    )

    return f"https://wa.me/{numero}?text={mensaje}"


# ===============================================
# TELÉFONOS
# ===============================================

def formatear_telefono(numero):

    numero = str(numero)

    if len(numero)==10:

        return f"({numero[:3]}) {numero[3:6]}-{numero[6:]}"

    return numero


# ===============================================
# CALIFICACIÓN
# ===============================================

def estrellas(calificacion):

    estrellas_llenas = int(round(calificacion))

    return "⭐"*estrellas_llenas


# ===============================================
# DISPONIBILIDAD
# ===============================================

def disponible(item,fecha_inicio,fecha_fin):

    if not fecha_inicio:

        return True

    if "disponibilidad" not in item:

        return True

    return (

        fecha_inicio in item["disponibilidad"]

        and

        fecha_fin in item["disponibilidad"]

    )

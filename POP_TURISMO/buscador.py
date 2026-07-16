import unicodedata
from datetime import datetime

# ==========================================================
# FUNCIONES AUXILIARES
# ==========================================================

def normalizar(texto):
    """Quita tildes y pasa a minúsculas para comparar sin errores de acentos/mayúsculas."""
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return texto


def precio_valido(precio, presupuesto):
    presupuesto = presupuesto.lower()
    if presupuesto == "económico":
        return precio <= 200000
    elif presupuesto == "medio":
        return 200000 < precio <= 500000
    elif presupuesto == "alto":
        return precio > 500000
    return True


def disponible(item, fecha_inicio, fecha_fin):
    if not fecha_inicio or not fecha_fin:
        return True

    disponibilidad = item.get("disponibilidad")

    # Si el hotel no tiene datos de disponibilidad, no lo descartamos
    if not disponibilidad:
        return True

    return (
        fecha_inicio in disponibilidad and
        fecha_fin in disponibilidad
    )


# ==========================================================
# HOTELES
# ==========================================================

def buscar_hoteles(
        hoteles,
        ciudad,
        presupuesto,
        fecha_inicio,
        fecha_fin):

    resultados = []
    ciudad = normalizar(ciudad)

    for hotel in hoteles:
        if normalizar(hotel["ciudad"]) != ciudad:
            continue

        if not precio_valido(
                hotel["precio"],
                presupuesto):
            continue

        if not disponible(
                hotel,
                fecha_inicio,
                fecha_fin):
            continue

        resultados.append(hotel)

    resultados.sort(
        key=lambda x: (
            x.get("calificacion", 0),
            -x.get("precio", 0)
        ),
        reverse=True
    )

    return resultados[:3]


# ==========================================================
# RESTAURANTES
# ==========================================================

def buscar_restaurantes(
        restaurantes,
        ciudad,
        presupuesto):

    ciudad = normalizar(ciudad)
    resultados = []

    for restaurante in restaurantes:
        if normalizar(restaurante["ciudad"]) != ciudad:
            continue

        resultados.append(restaurante)

    resultados.sort(
        key=lambda x: x.get("calificacion", 0),
        reverse=True
    )

    return resultados[:3]


# ==========================================================
# ACTIVIDADES
# ==========================================================

def buscar_actividades(
        actividades,
        ciudad,
        interes):

    ciudad = normalizar(ciudad)
    interes = normalizar(interes)
    resultados = []

    for actividad in actividades:
        if normalizar(actividad["ciudad"]) != ciudad:
            continue

        categoria = normalizar(
            actividad.get("categoria", "")
        )

        if interes not in categoria:
            continue

        resultados.append(actividad)

    resultados.sort(
        key=lambda x: x.get("calificacion", 0),
        reverse=True
    )

    return resultados[:3]

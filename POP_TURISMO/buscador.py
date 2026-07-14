from datetime import datetime


# ==========================================================
# FUNCIONES AUXILIARES
# ==========================================================

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

    disponibilidad = item.get("disponibilidad", [])

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

    ciudad = ciudad.lower()

    for hotel in hoteles:

        if hotel["ciudad"].lower() != ciudad:
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

    ciudad = ciudad.lower()

    resultados = []

    for restaurante in restaurantes:

        if restaurante["ciudad"].lower() != ciudad:
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

    ciudad = ciudad.lower()

    interes = interes.lower()

    resultados = []

    for actividad in actividades:

        if actividad["ciudad"].lower() != ciudad:
            continue

        categoria = actividad.get(
            "categoria",
            ""
        ).lower()

        if interes not in categoria:
            continue

        resultados.append(actividad)

    resultados.sort(
        key=lambda x: x.get("calificacion", 0),
        reverse=True
    )

    return resultados[:3]

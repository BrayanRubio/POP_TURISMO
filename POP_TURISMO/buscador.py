import unicodedata

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
    """
    Rangos ajustados a los precios reales de hoteles.json
    (min 190.000 - max 445.000).
    """
    presupuesto = normalizar(presupuesto)
    if presupuesto == "economico":
        return precio <= 280000
    elif presupuesto == "medio":
        return 280000 < precio <= 380000
    elif presupuesto == "alto":
        return precio > 380000
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
# MAPA DE SINÓNIMOS: opción del select -> categorías reales
# ==========================================================
# Las opciones del <select id="intereses"> del HTML no coinciden
# textualmente con los valores reales de "tipo_actividad" en
# actividades.json, así que cada opción se traduce a la(s)
# categoría(s) reales que debe buscar.

SINONIMOS_INTERES = {
    "playa": ["buceo", "nautico"],
    "gastronomia": ["gastronomico"],
    "cultura": ["cultural", "museo", "turismo religioso"],
    "aventura": ["aventura", "deporte extremo"],
    "vida nocturna": ["vida nocturna"],
    "compras": ["artesanias"],
    "naturaleza": ["ecoturismo", "senderismo"],
    "historia": ["tour historico", "turismo religioso", "museo"],
}


def coincide_interes(interes_normalizado, categoria_normalizada):
    terminos = SINONIMOS_INTERES.get(interes_normalizado, [interes_normalizado])
    return any(termino in categoria_normalizada for termino in terminos)


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
            actividad.get("tipo_actividad", "")
        )

        if not coincide_interes(interes, categoria):
            continue

        resultados.append(actividad)

    resultados.sort(
        key=lambda x: x.get("calificacion", 0),
        reverse=True
    )

    return resultados[:3]

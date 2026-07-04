from config import (
    HOTELES_JSON,
    RESTAURANTES_JSON,
    ACTIVIDADES_JSON,
    MAX_HOTELES,
    MAX_RESTAURANTES,
    MAX_ACTIVIDADES
)

from utilidades import (
    cargar_json,
    filtrar_ciudad,
    filtrar_presupuesto,
    seleccionar
)


# ==========================================
# CARGAR BASES DE DATOS
# ==========================================

hoteles_db = cargar_json(HOTELES_JSON)
restaurantes_db = cargar_json(RESTAURANTES_JSON)
actividades_db = cargar_json(ACTIVIDADES_JSON)


# ==========================================
# RECARGAR DATOS
# ==========================================

def recargar():

    global hoteles_db
    global restaurantes_db
    global actividades_db

    hoteles_db = cargar_json(HOTELES_JSON)
    restaurantes_db = cargar_json(RESTAURANTES_JSON)
    actividades_db = cargar_json(ACTIVIDADES_JSON)


# ==========================================
# HOTELES
# ==========================================

def buscar_hoteles(ciudad, presupuesto=None):

    hoteles = filtrar_ciudad(hoteles_db, ciudad)

    if presupuesto:

        hoteles_presupuesto = filtrar_presupuesto(
            hoteles,
            presupuesto
        )

        if hoteles_presupuesto:
            hoteles = hoteles_presupuesto

    return seleccionar(
        hoteles,
        MAX_HOTELES
    )


# ==========================================
# RESTAURANTES
# ==========================================

def buscar_restaurantes(ciudad):

    restaurantes = filtrar_ciudad(
        restaurantes_db,
        ciudad
    )

    return seleccionar(
        restaurantes,
        MAX_RESTAURANTES
    )


# ==========================================
# ACTIVIDADES
# ==========================================

def buscar_actividades(ciudad):

    actividades = filtrar_ciudad(
        actividades_db,
        ciudad
    )

    return seleccionar(
        actividades,
        MAX_ACTIVIDADES
    )


# ==========================================
# TODO EL PAQUETE
# ==========================================

def obtener_recomendaciones(ciudad, presupuesto=None):

    return {

        "hoteles": buscar_hoteles(
            ciudad,
            presupuesto
        ),

        "restaurantes": buscar_restaurantes(
            ciudad
        ),

        "actividades": buscar_actividades(
            ciudad
        )

    }


# ==========================================
# VALIDAR CIUDAD
# ==========================================

def ciudad_disponible(ciudad):

    hoteles = filtrar_ciudad(
        hoteles_db,
        ciudad
    )

    restaurantes = filtrar_ciudad(
        restaurantes_db,
        ciudad
    )

    actividades = filtrar_ciudad(
        actividades_db,
        ciudad
    )

    return (
        len(hoteles) > 0 or
        len(restaurantes) > 0 or
        len(actividades) > 0
    )


# ==========================================
# CONTADORES
# ==========================================

def total_hoteles():

    return len(hoteles_db)


def total_restaurantes():

    return len(restaurantes_db)


def total_actividades():

    return len(actividades_db)


# ==========================================
# ESTADÍSTICAS
# ==========================================

def estadisticas():

    return {

        "hoteles": total_hoteles(),

        "restaurantes": total_restaurantes(),

        "actividades": total_actividades()

    }
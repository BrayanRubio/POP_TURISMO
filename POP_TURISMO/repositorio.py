from cargador import cargar_json
from config import (
    HOTELES_JSON,
    RESTAURANTES_JSON,
    ACTIVIDADES_JSON
)


# ==========================================
# CARGA DE DATOS AL INICIAR
# ==========================================

HOTELES = cargar_json(HOTELES_JSON)

RESTAURANTES = cargar_json(RESTAURANTES_JSON)

ACTIVIDADES = cargar_json(ACTIVIDADES_JSON)


# ==========================================
# FUNCIONES DE ACCESO
# ==========================================

def obtener_hoteles():
    return HOTELES


def obtener_restaurantes():
    return RESTAURANTES


def obtener_actividades():
    return ACTIVIDADES

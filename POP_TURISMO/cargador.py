import json
from dataclasses import dataclass, field, fields
from typing import List


# =====================================================
# HOTEL
# =====================================================
@dataclass
class Hotel:
    id: int
    nombre: str
    categoria: int
    ciudad: str
    departamento: str
    direccion: str
    telefono: str
    correo: str
    pagina_web: str
    latitud: float
    longitud: float
    calificacion: float
    precio: int
    servicios: List[str] = field(default_factory=list)
    fecha_inicio: str = ""
    fecha_fin: str = ""
    imagen: str = ""


# =====================================================
# RESTAURANTE
# =====================================================
@dataclass
class Restaurante:
    id: int
    nombre: str
    ciudad: str
    departamento: str
    direccion: str
    telefono: str
    correo: str
    pagina_web: str
    latitud: float
    longitud: float
    precio_promedio: int
    calificacion: float
    tipo_comida: str
    horarios: str
    imagen: str = ""


# =====================================================
# ACTIVIDAD
# =====================================================
@dataclass
class Actividad:
    id: int
    nombre: str
    tipo_actividad: str
    ciudad: str
    departamento: str
    punto_encuentro: str
    telefono: str
    correo: str
    pagina_web: str
    latitud: float
    longitud: float
    calificacion: float
    precio: int
    duracion_horas: float
    servicios: List[str] = field(default_factory=list)
    fecha_inicio: str = ""
    fecha_fin: str = ""
    imagen: str = ""


# =====================================================
# CARGA GENÉRICA DE JSON
# =====================================================
MODELOS = {
    "hoteles": Hotel,
    "restaurantes": Restaurante,
    "actividades": Actividad,
}


def _construir(modelo, dato):
    """
    Crea una instancia del dataclass usando solo los campos
    que el modelo espera, e ignora cualquier campo extra que
    venga en el JSON (por ejemplo, punto_encuentro adicional
    o cualquier dato futuro).
    """
    nombres_validos = {f.name for f in fields(modelo)}
    filtrado = {
        clave: valor
        for clave, valor in dato.items()
        if clave in nombres_validos
    }
    return modelo(**filtrado)


def cargar_json(ruta, tipo=None):
    """
    Carga un archivo JSON y lo convierte en una lista de
    objetos (Hotel, Restaurante o Actividad).

    'tipo' puede ser "hoteles", "restaurantes" o "actividades".
    Si no se indica, se intenta deducir del nombre del archivo.
    """
    try:
        with open(ruta, encoding="utf-8") as f:
            datos = json.load(f)
    except FileNotFoundError:
        print(f"[cargador] No se encontró el archivo: {ruta}")
        return []
    except json.JSONDecodeError as e:
        print(f"[cargador] JSON inválido en {ruta}: {e}")
        return []

    if tipo is None:
        nombre = ruta.lower()
        if "hotel" in nombre:
            tipo = "hoteles"
        elif "restaurante" in nombre:
            tipo = "restaurantes"
        elif "actividad" in nombre:
            tipo = "actividades"

    modelo = MODELOS.get(tipo)
    if modelo is None:
        print(f"[cargador] Tipo desconocido para {ruta}, devolviendo datos crudos.")
        return datos

    resultados = []
    for dato in datos:
        try:
            resultados.append(_construir(modelo, dato))
        except TypeError as e:
            print(f"[cargador] Registro inválido en {ruta} (id={dato.get('id')}): {e}")

    return resultados

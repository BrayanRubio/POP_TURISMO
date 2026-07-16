from dataclasses import dataclass, field
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

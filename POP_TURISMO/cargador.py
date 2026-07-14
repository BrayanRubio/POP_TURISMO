from dataclasses import dataclass, field
from typing import List


# =====================================================
# HOTEL
# =====================================================

@dataclass
class Hotel:

    id: int

    nombre: str

    ciudad: str

    departamento: str

    direccion: str

    telefono: str

    correo: str

    pagina_web: str

    imagen: str

    latitud: float

    longitud: float

    precio: int

    calificacion: float

    servicios: List[str] = field(default_factory=list)

    disponibilidad: List[str] = field(default_factory=list)


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

    imagen: str

    latitud: float

    longitud: float

    precio_promedio: int

    calificacion: float

    tipo_comida: str

    horarios: str


# =====================================================
# ACTIVIDAD
# =====================================================

@dataclass
class Actividad:

    id: int

    nombre: str

    ciudad: str

    departamento: str

    categoria: str

    descripcion: str

    direccion: str

    telefono: str

    pagina_web: str

    imagen: str

    latitud: float

    longitud: float

    precio: int

    duracion: str

    calificacion: float

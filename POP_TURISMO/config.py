import os

# ==============================
# CONFIGURACIÓN GENERAL
# ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

STATIC_DIR = os.path.join(BASE_DIR, "static")

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")


# ==============================
# OPENAI
# ==============================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# ==============================
# ARCHIVOS JSON
# ==============================

HOTELES_JSON = os.path.join(DATA_DIR, "hoteles.json")

RESTAURANTES_JSON = os.path.join(DATA_DIR, "restaurantes.json")

ACTIVIDADES_JSON = os.path.join(DATA_DIR, "actividades.json")

CIUDADES_JSON = os.path.join(DATA_DIR, "ciudades.json")


# ==============================
# RECOMENDACIONES
# ==============================

MAX_HOTELES = 3

MAX_RESTAURANTES = 5

MAX_ACTIVIDADES = 5


# ==============================
# IDIOMAS
# ==============================

IDIOMAS = {

    "Español": "es",

    "English": "en",

    "Português": "pt",

    "Français": "fr",

    "Deutsch": "de",

    "Italiano": "it"

}

IDIOMA_DEFAULT = "Español"


# ==============================
# MENSAJES
# ==============================

SALUDO = "¡Hola! Soy POP Turismo."

DESPEDIDA = "Gracias por utilizar POP Turismo. ¡Buen viaje!"


# ==============================
# CLIMA
# ==============================

USAR_CLIMA = False


# ==============================
# OPENAI
# ==============================

USAR_OPENAI = True


# ==============================
# FALLBACK LOCAL
# ==============================

USAR_RESPUESTA_LOCAL = True
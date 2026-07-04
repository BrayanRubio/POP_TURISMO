from openai import OpenAI
from config import (
    OPENAI_API_KEY,
    USAR_OPENAI,
    IDIOMA_DEFAULT
)

from utilidades import (
    lista_texto,
    respuesta_local
)

# ==========================================
# CLIENTE OPENAI
# ==========================================

client = None

if USAR_OPENAI and OPENAI_API_KEY:

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
    except:
        client = None


# ==========================================
# PROMPT
# ==========================================

def construir_prompt(
    ciudad,
    idioma,
    presupuesto,
    intereses,
    tipo,
    dias,
    viajeros,
    transporte,
    hoteles,
    restaurantes,
    actividades
):

    hoteles_txt = lista_texto(hoteles)

    restaurantes_txt = lista_texto(restaurantes)

    actividades_txt = lista_texto(actividades)

    return f"""
Eres POP Turismo.

Eres un guía turístico profesional.

NO inventes información.

Utiliza EXCLUSIVAMENTE los datos suministrados.

Destino:

{ciudad}

Idioma:

{idioma}

Tipo de viaje:

{tipo}

Presupuesto:

{presupuesto}

Intereses:

{intereses}

Duración:

{dias} días

Viajeros:

{viajeros}

Transporte:

{transporte}

================================

HOTELES

{hoteles_txt}

================================

RESTAURANTES

{restaurantes_txt}

================================

ACTIVIDADES

{actividades_txt}

================================

Construye una guía turística elegante.

No escribas tablas.

No escribas listas largas.

Escribe como si conversarás con el turista.

Divide la respuesta por secciones usando emojis.

Incluye:

👋 Bienvenida

🏨 Hospedaje

🍽 Gastronomía

🎯 Actividades

🚖 Transporte

🌤 Clima

💡 Consejos

🎉 Despedida

Toda la respuesta debe escribirse en {idioma}.
"""


# ==========================================
# IA
# ==========================================

def generar_con_openai(
    ciudad,
    idioma,
    presupuesto,
    intereses,
    tipo,
    dias,
    viajeros,
    transporte,
    hoteles,
    restaurantes,
    actividades
):

    if client is None:
        return None

    prompt = construir_prompt(
        ciudad,
        idioma,
        presupuesto,
        intereses,
        tipo,
        dias,
        viajeros,
        transporte,
        hoteles,
        restaurantes,
        actividades
    )

    try:

        respuesta = client.responses.create(

            model="gpt-5",

            input=prompt,

            max_output_tokens=1800

        )

        return respuesta.output_text

    except Exception:

        return None


# ==========================================
# LOCAL
# ==========================================

def generar_local(
    ciudad,
    hoteles,
    restaurantes,
    actividades
):

    return respuesta_local(

        ciudad,

        hoteles,

        restaurantes,

        actividades

    )


# ==========================================
# PRINCIPAL
# ==========================================

def generar_guia(

    ciudad,

    idioma=IDIOMA_DEFAULT,

    presupuesto="",

    intereses="",

    tipo="",

    dias="",

    viajeros="",

    transporte="",

    hoteles=None,

    restaurantes=None,

    actividades=None

):

    hoteles = hoteles or []

    restaurantes = restaurantes or []

    actividades = actividades or []

    texto = generar_con_openai(

        ciudad,

        idioma,

        presupuesto,

        intereses,

        tipo,

        dias,

        viajeros,

        transporte,

        hoteles,

        restaurantes,

        actividades

    )

    if texto:

        return texto

    return generar_local(

        ciudad,

        hoteles,

        restaurantes,

        actividades

    )
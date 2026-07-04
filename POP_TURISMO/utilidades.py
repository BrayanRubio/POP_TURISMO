import json
import random
import os


# ==========================================
# CARGAR JSON
# ==========================================

def cargar_json(ruta):

    if not os.path.exists(ruta):
        return []

    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


# ==========================================
# GUARDAR JSON
# ==========================================

def guardar_json(ruta, datos):

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(
            datos,
            archivo,
            indent=4,
            ensure_ascii=False
        )


# ==========================================
# LIMPIAR TEXTO
# ==========================================

def limpiar(texto):

    if texto is None:
        return ""

    return str(texto).strip().lower()


# ==========================================
# BUSCAR POR CIUDAD
# ==========================================

def filtrar_ciudad(registros, ciudad):

    ciudad = limpiar(ciudad)

    encontrados = []

    for registro in registros:

        if limpiar(registro.get("ciudad")) == ciudad:
            encontrados.append(registro)

    return encontrados


# ==========================================
# BUSCAR POR DEPARTAMENTO
# ==========================================

def filtrar_departamento(registros, departamento):

    departamento = limpiar(departamento)

    encontrados = []

    for registro in registros:

        if limpiar(registro.get("departamento")) == departamento:
            encontrados.append(registro)

    return encontrados


# ==========================================
# BUSCAR POR CATEGORÍA
# ==========================================

def filtrar_categoria(registros, categoria):

    categoria = limpiar(categoria)

    encontrados = []

    for registro in registros:

        if limpiar(registro.get("categoria")) == categoria:
            encontrados.append(registro)

    return encontrados


# ==========================================
# BUSCAR POR PRESUPUESTO
# ==========================================

def filtrar_presupuesto(registros, presupuesto):

    presupuesto = limpiar(presupuesto)

    encontrados = []

    for registro in registros:

        if limpiar(registro.get("presupuesto")) == presupuesto:
            encontrados.append(registro)

    return encontrados


# ==========================================
# SELECCIONAR ALEATORIOS
# ==========================================

def seleccionar(registros, cantidad):

    if len(registros) <= cantidad:
        return registros

    return random.sample(registros, cantidad)


# ==========================================
# FORMATEAR PRECIO
# ==========================================

def precio(valor):

    try:

        return "${:,.0f}".format(float(valor)).replace(",", ".")

    except:

        return valor


# ==========================================
# CONVERTIR LISTA A TEXTO
# ==========================================

def lista_texto(lista):

    texto = ""

    for item in lista:

        texto += f"""

Nombre: {item.get('nombre','')}

Ciudad: {item.get('ciudad','')}

Descripción: {item.get('descripcion','')}

Precio: {item.get('precio','')}

"""

    return texto


# ==========================================
# OBTENER NOMBRES
# ==========================================

def nombres(lista):

    return [x.get("nombre") for x in lista]


# ==========================================
# CONTAR REGISTROS
# ==========================================

def contar(lista):

    return len(lista)


# ==========================================
# VALIDAR CAMPO
# ==========================================

def obtener(registro, campo):

    if campo in registro:
        return registro[campo]

    return ""


# ==========================================
# GENERAR RESPUESTA LOCAL
# ==========================================

def respuesta_local(
    ciudad,
    hoteles,
    restaurantes,
    actividades
):

    texto = f"¡Excelente elección! {ciudad} es un destino con mucho por descubrir.\n\n"

    texto += "🏨 Alojamiento recomendado:\n\n"

    for hotel in hoteles:

        texto += (
            f"• {hotel.get('nombre')} "
            f"({hotel.get('precio')}) "
            f"{hotel.get('descripcion')}\n\n"
        )

    texto += "\n🍽 Restaurantes recomendados:\n\n"

    for restaurante in restaurantes:

        texto += (
            f"• {restaurante.get('nombre')} "
            f"{restaurante.get('descripcion')}\n\n"
        )

    texto += "\n🎯 Actividades sugeridas:\n\n"

    for actividad in actividades:

        texto += (
            f"• {actividad.get('nombre')} "
            f"{actividad.get('descripcion')}\n\n"
        )

    texto += (
        "\nEsperamos que disfrutes tu viaje. "
        "Gracias por utilizar POP Turismo."
    )

    return texto
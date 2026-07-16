//======================================================
// POP TURISMO V3
//======================================================

const chat = document.getElementById("chat");
const resultado = document.getElementById("resultado");
const loader = document.getElementById("loader");


//======================================================
// AGREGAR MENSAJE AL CHAT
//======================================================

function agregarMensaje(texto, tipo = "bot") {

    const mensaje = document.createElement("div");

    mensaje.className = `message ${tipo}`;

    mensaje.innerHTML = `

        <div class="avatar">

            ${tipo === "bot" ? "🤖" : "👤"}

        </div>

        <div class="bubble">

            ${texto}

        </div>

    `;

    chat.appendChild(mensaje);

    chat.scrollTop = chat.scrollHeight;

}



//======================================================
// CONSULTAR
//======================================================

async function consultar() {

    resultado.innerHTML = "";

    loader.style.display = "block";



    const datos = {

        idioma: document.getElementById("idioma").value,

        ciudad: document.getElementById("ciudad").value,

        fecha_inicio: document.getElementById("fecha_inicio").value,

        fecha_fin: document.getElementById("fecha_fin").value,

        presupuesto: document.getElementById("presupuesto").value,

        tipo: document.getElementById("tipo").value,

        dias: document.getElementById("dias").value,

        viajeros: document.getElementById("viajeros").value,

        transporte: document.getElementById("transporte").value,

        intereses: document.getElementById("intereses").value

    };



    agregarMensaje(

        `Quiero viajar a <b>${datos.ciudad}</b>
        durante <b>${datos.dias}</b> días,
        con presupuesto <b>${datos.presupuesto}</b>.`,

        "user"

    );



    try {

        const response = await fetch("/recommend", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(datos)

        });



        const respuesta = await response.json();



        loader.style.display = "none";



        if (!respuesta.success) {

            agregarMensaje(

                respuesta.error,

                "bot"

            );

            return;

        }



        agregarMensaje(

            respuesta.mensaje,

            "bot"

        );



        crearHoteles(

            respuesta.hoteles

        );



        crearRestaurantes(

            respuesta.restaurantes

        );



        crearActividades(

            respuesta.actividades

        );



    }

    catch (error) {

        loader.style.display = "none";



        agregarMensaje(

            "Ocurrió un error al consultar el servidor.",

            "bot"

        );

    }

}
//======================================================
// CREAR TARJETAS DE HOTELES
//======================================================

function crearHoteles(hoteles) {

    if (!hoteles || hoteles.length === 0) return;

    resultado.innerHTML += `
        <h3 class="mt-4 mb-3">
            🏨 Alojamientos recomendados
        </h3>
    `;

    hoteles.forEach(hotel => {

        resultado.innerHTML += `

        <div class="card-resultado">

            <div class="card-contenido">

                <h4>${hotel.nombre}</h4>

                <div class="estrellas">

                    ${"⭐".repeat(Math.round(hotel.calificacion))}

                </div>

                <p>

                    📍 ${hotel.direccion}

                </p>

                <p class="precio">

                    $${hotel.precio.toLocaleString("es-CO")}

                </p>

                <div class="card-botones">

                    <a
                        href="tel:${hotel.telefono}"
                        class="btn btn-primary">

                        📞 Llamar

                    </a>

                    <a
                        href="https://wa.me/${hotel.telefono}"
                        target="_blank"
                        class="btn btn-success">

                        💬 WhatsApp

                    </a>

                    <a
                        href="https://maps.google.com/?q=${hotel.latitud},${hotel.longitud}"
                        target="_blank"
                        class="btn btn-outline-secondary">

                        📍 Mapa

                    </a>

                </div>

            </div>

        </div>

        `;

    });

}



//======================================================
// RESTAURANTES
//======================================================

function crearRestaurantes(restaurantes){

    if(!restaurantes || restaurantes.length===0) return;

    resultado.innerHTML += `

        <h3 class="mt-5 mb-3">

            🍽 Restaurantes

        </h3>

    `;

    restaurantes.forEach(restaurante=>{

        resultado.innerHTML += `

        <div class="card-resultado">

            <div class="card-contenido">

                <h4>${restaurante.nombre}</h4>

                <div class="estrellas">

                    ${"⭐".repeat(Math.round(restaurante.calificacion))}

                </div>

<p>

                    📍 ${restaurante.direccion}

                </p>

                <div class="card-botones">

                    <a

                        href="tel:${restaurante.telefono}"

                        class="btn btn-primary">

                        📞 Llamar

                    </a>

                    <a

                        href="https://wa.me/${restaurante.telefono}"

                        class="btn btn-success"

                        target="_blank">

                        💬 WhatsApp

                    </a>

                </div>

            </div>

        </div>

        `;

    });

}



//======================================================
// ACTIVIDADES
//======================================================

function crearActividades(actividades){

    if(!actividades || actividades.length===0) return;

    resultado.innerHTML += `

        <h3 class="mt-5 mb-3">

            🎯 Actividades

        </h3>

    `;

    actividades.forEach(actividad=>{

        resultado.innerHTML += `

        <div class="card-resultado">

            <div class="card-contenido">

                <h4>${actividad.nombre}</h4>

                <div class="estrellas">

                    ${"⭐".repeat(Math.round(actividad.calificacion))}

                </div>

                <p>

                    ${actividad.descripcion}

                </p>

                <p class="precio">

                    $${actividad.precio.toLocaleString("es-CO")}

                </p>

            </div>

        </div>

        `;

    });

}



//======================================================
// NUEVO CHAT
//======================================================

function nuevoChat(){

    chat.innerHTML=`

        <div class="message bot">

            <div class="avatar">

                🤖

            </div>

            <div class="bubble">

                ¡Hola!

                <br><br>

                Soy POP Turismo.

                Completa el formulario y prepararé una guía personalizada para tu viaje.

            </div>

        </div>

    `;

    resultado.innerHTML="";

}



//======================================================
// DESCARGAR PDF
//======================================================

async function descargarPDF(){

    const { jsPDF } = window.jspdf;

    const pdf = new jsPDF();

    pdf.setFontSize(20);

    pdf.text("POP Turismo",20,20);

    pdf.setFontSize(12);

    pdf.text("Guía turística personalizada",20,35);

    pdf.text(resultado.innerText,20,55);

    pdf.save("POP_Turismo.pdf");

}

// =======================================
// CAMBIO DE IDIOMA
// =======================================

function cambiarIdioma() {

    const idioma = document.getElementById("idioma").value;

    const t = translations[idioma];

    document.getElementById("titulo").textContent = t.titulo;
    document.getElementById("subtitulo").textContent = t.subtitulo;
    document.getElementById("planifica").textContent = t.planifica;

    document.getElementById("lblIdioma").textContent = t.idioma;
    document.getElementById("lblDestino").textContent = t.destino;
    document.getElementById("lblLlegada").textContent = t.llegada;
    document.getElementById("lblSalida").textContent = t.salida;
    document.getElementById("lblTipo").textContent = t.tipo;
    document.getElementById("lblPresupuesto").textContent = t.presupuesto;
    document.getElementById("lblDias").textContent = t.dias;
    document.getElementById("lblViajeros").textContent = t.viajeros;
    document.getElementById("lblTransporte").textContent = t.transporte;
    document.getElementById("lblActividad").textContent = t.actividad;

    document.getElementById("txtGenerar").textContent = t.generar;
    document.getElementById("txtNuevo").textContent = t.nuevo;
    document.getElementById("txtPDF").textContent = t.pdf;
// Traducir opciones de los select

document.querySelectorAll("#tipo option").forEach((opcion, i) => {
    opcion.textContent = t.tipos[i];
});

document.querySelectorAll("#presupuesto option").forEach((opcion, i) => {
    opcion.textContent = t.presupuestos[i];
});

document.querySelectorAll("#transporte option").forEach((opcion, i) => {
    opcion.textContent = t.transportes[i];
});

document.querySelectorAll("#intereses option").forEach((opcion, i) => {
    opcion.textContent = t.intereses[i];
});
}
document.getElementById("idioma").addEventListener("change", cambiarIdioma);
window.addEventListener("DOMContentLoaded", () => {
    cambiarIdioma();
});

// =======================================
// CALCULAR DURACIÓN DEL VIAJE
// =======================================

const fechaInicio = document.getElementById("fecha_inicio");
const fechaFin = document.getElementById("fecha_fin");
const dias = document.getElementById("dias");

function calcularDias() {

    if (!fechaInicio.value || !fechaFin.value) {
        dias.value = "";
        return;
    }

    const inicio = new Date(fechaInicio.value);
    const fin = new Date(fechaFin.value);

    if (fin <= inicio) {
        alert("La fecha de salida debe ser posterior a la fecha de llegada.");
        dias.value = "";
        fechaFin.value = "";
        return;
    }

    const diferencia = fin - inicio;

    const totalDias = Math.ceil(diferencia / (1000 * 60 * 60 * 24));

    dias.value = totalDias;
}

fechaInicio.addEventListener("change", calcularDias);
fechaFin.addEventListener("change", calcularDias);

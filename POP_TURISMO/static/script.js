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

            <img
                src="/static/img/hoteles/${hotel.imagen}"
                class="card-imagen">

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

            <img

                src="/static/img/restaurantes/${restaurante.imagen}"

                class="card-imagen">

            <div class="card-contenido">

                <h4>${restaurante.nombre}</h4>

                <div class="estrellas">

                    ${"⭐".repeat(Math.round(restaurante.calificacion))}

                </div>

                <p>

                    🍴 ${restaurante.tipo_comida}

                </p>

                <p>

                    📍 ${restaurante.direccion}

                </p>

                <div class="card-botones">

                    <a

                        href="tel:${restaurante.telefono}"

                        class="btn btn-primary">

                        📞

                    </a>

                    <a

                        href="https://wa.me/${restaurante.telefono}"

                        class="btn btn-success"

                        target="_blank">

                        💬

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

            <img

                src="/static/img/actividades/${actividad.imagen}"

                class="card-imagen">

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

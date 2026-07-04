async function consultar() {

    const chat = document.getElementById("chat");

    const ciudad = document.getElementById("ciudad").value;
    const idioma = document.getElementById("idioma").value;
    const presupuesto = document.getElementById("presupuesto").value;
    const intereses = document.getElementById("intereses").value;
    const tipo = document.getElementById("tipo").value;
    const dias = document.getElementById("dias").value;
    const viajeros = document.getElementById("viajeros").value;
    const transporte = document.getElementById("transporte").value;

    if(ciudad==""){
        alert("Ingrese un destino.");
        return;
    }

    // MENSAJE DEL USUARIO

    chat.innerHTML += `
    <div class="message user">

        <div class="bubble">

            Quiero viajar a <b>${ciudad}</b> durante
            <b>${dias}</b> días.

            Mi presupuesto es
            <b>${presupuesto}</b>.

            Me interesan:

            <b>${intereses}</b>

        </div>

        <div class="avatar">
            👤
        </div>

    </div>
    `;

    chat.scrollTop = chat.scrollHeight;

    // ESCRIBIENDO

    const typing = document.createElement("div");

    typing.className="message bot";

    typing.id="typing";

    typing.innerHTML=`

        <div class="avatar">
            🤖
        </div>

        <div class="typing">

            <span></span>
            <span></span>
            <span></span>

        </div>

    `;

    chat.appendChild(typing);

    chat.scrollTop=chat.scrollHeight;

    // PETICIÓN

    const respuesta = await fetch("/recommend",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            ciudad,
            idioma,
            presupuesto,
            intereses,
            tipo,
            dias,
            viajeros,
            transporte

        })

    });

    const datos = await respuesta.json();

    document.getElementById("typing").remove();

    escribirRespuesta(datos.respuesta);

}
function escribirRespuesta(texto){

    const chat=document.getElementById("chat");

    const bloque=document.createElement("div");

    bloque.className="message bot";

    bloque.innerHTML=`

        <div class="avatar">

            🤖

        </div>

        <div class="bubble" id="respuestaActual"></div>

    `;

    chat.appendChild(bloque);

    const destino=document.getElementById("respuestaActual");

    let i=0;

    function escribir(){

        if(i<texto.length){

            destino.innerHTML += texto.charAt(i);

            i++;

            chat.scrollTop=chat.scrollHeight;

            setTimeout(escribir,8);

        }

    }

    escribir();

}
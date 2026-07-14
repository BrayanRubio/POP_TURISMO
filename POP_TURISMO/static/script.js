const chat = document.getElementById("chat");

const typing = document.getElementById("typing");



function agregarUsuario(texto){

chat.innerHTML += `

<div class="mensaje usuario">

<div class="burbuja">

${texto}

</div>

<div class="avatar">

<i class="bi bi-person-fill"></i>

</div>

</div>

`;

scrollFinal();

}



function agregarBot(texto){

chat.innerHTML += `

<div class="mensaje bot">

<div class="avatar">

<i class="bi bi-robot"></i>

</div>

<div class="burbuja">

${texto.replace(/\n/g,"<br>")}

</div>

</div>

`;

scrollFinal();

}



function scrollFinal(){

chat.scrollTop=chat.scrollHeight;

}



function mostrarTyping(){

typing.style.display="flex";

scrollFinal();

}



function ocultarTyping(){

typing.style.display="none";

}
async function consultar(){


const idioma=document.getElementById("idioma").value;

const ciudad=document.getElementById("ciudad").value;

const presupuesto=document.getElementById("presupuesto").value;

const tipo=document.getElementById("tipo").value;

const dias=document.getElementById("dias").value;

const viajeros=document.getElementById("viajeros").value;

const intereses=document.getElementById("intereses").value;

const transporte=document.getElementById("transporte").value;

const fecha_inicio=document.getElementById("fecha_inicio").value;

const fecha_fin=document.getElementById("fecha_fin").value;



if(ciudad==""){

alert("Seleccione una ciudad.");

return;

}



agregarUsuario(

`Quiero viajar a <b>${ciudad}</b> durante ${dias} días.
Mi presupuesto es ${presupuesto}.`

);



mostrarTyping();



try{

const response=await fetch("/recommend",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

idioma,

ciudad,

presupuesto,

tipo,

dias,

viajeros,

intereses,

transporte,

fecha_inicio,

fecha_fin

})

});



const data=await response.json();



ocultarTyping();



agregarBot(data.respuesta);

}

catch(error){

ocultarTyping();

agregarBot(

"⚠ Ocurrió un error al consultar el servidor."

);

}

}
function limpiarChat(){

chat.innerHTML=`

<div class="mensaje bot">

<div class="avatar">

<i class="bi bi-robot"></i>

</div>

<div class="burbuja">

<h4>

👋 Bienvenido nuevamente

</h4>

<p>

Soy POP Turismo.

Estoy listo para ayudarte a planear tu viaje.

</p>

</div>

</div>

`;

}
async function descargarPDF(){

const {jsPDF}=window.jspdf;

const pdf=new jsPDF();

pdf.setFont("helvetica");

pdf.setFontSize(16);

pdf.text("POP Turismo",20,20);

pdf.setFontSize(12);

pdf.text(

chat.innerText,

20,

35,

{

maxWidth:170

}

);

pdf.save("POP_Turismo.pdf");

}

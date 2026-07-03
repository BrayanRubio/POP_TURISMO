async function consultar(){

const datos={

idioma:document.getElementById("idioma").value,

ciudad:document.getElementById("ciudad").value,

tipo:document.getElementById("tipo").value,

presupuesto:document.getElementById("presupuesto").value,

dias:document.getElementById("dias").value,

viajeros:document.getElementById("viajeros").value,

transporte:document.getElementById("transporte").value,

intereses:document.getElementById("intereses").value

}

document.getElementById("respuesta").innerHTML="⏳ Buscando las mejores recomendaciones...";

const respuesta=await fetch("/recommend",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(datos)

});

const json=await respuesta.json();

document.getElementById("respuesta").innerHTML=json.respuesta;

}
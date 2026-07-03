async function consultar(){

const datos={

idioma:document.getElementById("idioma").value,

presupuesto:document.getElementById("presupuesto").value,

intereses:document.getElementById("intereses").value,

tipo:document.getElementById("tipo").value,

dias:document.getElementById("dias").value

};

const respuesta=await fetch("/recommend",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(datos)

});

const json=await respuesta.json();

document.getElementById("respuesta").innerText=json.respuesta;

}
async function consultar(){

const datos={

ciudad:document.getElementById("ciudad").value,

presupuesto:document.getElementById("presupuesto").value,

intereses:document.getElementById("intereses").value

}

const response=await fetch("/recommend",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(datos)

});

const json=await response.json();

let html="<h2>🏨 Hoteles</h2>";

json.hoteles.forEach(h=>{

html+=`

<div class="card">

<h3>${h.nombre}</h3>

<p>${h.zona}</p>

<p>$ ${h.precio}</p>

<p>${h.descripcion}</p>

</div>

`;

});

html+="<h2>🍽 Restaurantes</h2>";

json.restaurantes.forEach(r=>{

html+=`

<div class="card">

<h3>${r.nombre}</h3>

<p>$ ${r.precio}</p>

<p>${r.descripcion}</p>

</div>

`;

});

html+="<h2>🎯 Actividades</h2>";

json.actividades.forEach(a=>{

html+=`

<div class="card">

<h3>${a.nombre}</h3>

<p>$ ${a.precio}</p>

<p>${a.descripcion}</p>

</div>

`;

});

document.getElementById("respuesta").innerHTML=html;

}
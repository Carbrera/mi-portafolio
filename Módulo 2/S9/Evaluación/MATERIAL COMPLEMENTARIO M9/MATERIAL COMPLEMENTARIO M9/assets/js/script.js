var tareas = [
    { tarea: "Pintar la fachada de la casa" },
    { tarea: "Comprar comida para el perro" },
    { tarea: "Pagar la tarjeta de crédito" }
]

mostrarTareas(tareas)

//funcion para mostrar las tareas
function mostrarTareas(tareas) {
    var cuerpoTabla = document.getElementById("cuerpo-tabla") //obteniendo el elemento
    cuerpoTabla.innerHTML = '' // limpiando el elemento para inyectar los nuevos
    for (let index = 0; index < tareas.length; index++) { //recorrido del arreglo tareas
        //inyectando (concatenando) cada elemento dentro del tbody
        cuerpoTabla.innerHTML += `
        <tr>           
            <td>${tareas[index].tarea}</td>
            <td>
              <button type="button" class="btn btn-danger" onclick="eliminar(${index})">Finalizar</button>
            </td>           
        </tr>
        ` 
    }
}

//funcion eliminar
function eliminar(indice) {
    tareas.splice(indice, 1) //eliminar elemento por indice, cuantas veces
    mostrarTareas(tareas) // ejecucion funcion mostrarTareas de nuevo
}

function mostrarformulario() {
    var formulario = document.getElementById("formulario")

    if (formulario.style.display == "none" || formulario.style.display == "") {
        formulario.style.display = "block"
    } else {
        formulario.style.display = "none"
    }
    
}

function agregar() {
    var nuevaTarea = document.getElementById("nuevaTarea").value
    tareas.push({ tarea: nuevaTarea })
    mostrarTareas(tareas)
    document.getElementById("formulario").style.display = "none"
    document.getElementById("nuevaTarea").value = ""

}
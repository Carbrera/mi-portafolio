var selectorId = document.getElementById("parrafo").innerHTML
var selectorEtiqueta = document.getElementsByTagName("h1");
var selectorClass = document.getElementsByClassName("container");
var selectorVarios = document.querySelector(".container");
var selectorTodos = document.querySelectorAll(".container");

var creandoElemento = document.createElement("p");
creandoElemento.textContent = "Creando desde Javascript";

document.body.appendChild(creandoElemento)
selectorVarios.append(creandoElemento);

var nodoPadre = document.querySelector(".container");
var nodoHijo = document.querySelector("#parrafo");

nodoPadre.removeChild(nodoHijo);
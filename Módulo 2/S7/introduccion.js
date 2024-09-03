//comentario de una sola linea

//declaración de variable en js
let nombre= "Juan"; //la variable let es una variable local
var edad= 20; //la variable var es una variable global
const pi=3.1416; //la variable const es una constante

//Tipos de datos
var mensaje="Hola, mundo"; //string = cadena de caracteres = letras. Van entre comillas
var numero=42; //number
var esVerdadero=true; //boolean = true o false.

// objetos
var persona = {
    nombre: "Juan", //clave, valor
    edad: 20
} //objeto

persona.nombre

// arreglo
var colores = ["rojo", "verde", "azul"]; // va entre corchetes y cada uno de los elementos esta en una posición

// imprimir en consola
console.log("Hola, Mundo");

//leer en una ventana emergente, con la funcion prompt(variable)
var nombreIngresado = prompt("Ingrese su nombre");

//funciones, estructuras de codigo que realizan alguna tarea o ejecutan un bloque de codigo
function suma(a, b){ // funcion llamada suma que recibe dos parametros de entrada a y b, separados por coma
    //el cuerpo o proceso de la funcion
    return a + b; // retorna la suma de a y b
}
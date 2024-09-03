//Ejercicio 2 = Escribir código
var num1 = 5;
var num2 = 10;
var resultado = num1 + num2;
console.log(resultado);
var nombre = "Pedro";
console.log(nombre + " dice que el resultado de la suma es: " + resultado);

//Ejercicio 3 = Realizar operaciones ariméticas
var num1, num2, resultado;
numero1 = prompt("Ingrese un dígito");
console.log(num1);
numero2 = prompt("Ingrese el segundo número");
numero1 = parseInt(numero1);
numero2 = parseInt(numero2);
resultado = num1 + num2;
alert("La suma de " + num1 + " y " + num2 + " es " + resultado)

//Ejercicio 4 = Funciones
function suma(numero1, numero2) {
    resultado = numero1 + numero2; 
    return resultado;
}

function resta(numero1, numero2) { 
    resultado = numero1 - numero2; 
    return resultado; 
} 

function multiplicacion(numero1, numero2) { 
    resultado = numero1 * numero2; 
    return resultado; 
} 

function division(numero1, numero2) { 
    resultado = numero1 / numero2; 
    return resultado; 
}

resultado = resta(numero1, numero2); 
alert("La resta de " + numero1 + " - " + numero2 + " es " + resultado);

resultado = multiplicacion(numero1, numero2);
alert("El producto de " + numero1 + " y " + numero2 + " es " + resultado)
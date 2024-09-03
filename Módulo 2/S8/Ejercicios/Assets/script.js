var numero = parseInt(prompt("Ingrese un número"));

try {
    if(numero != 7) throw new Error("El número no es 7");
}   catch (error) {
    console.log(error.name, error.message)
}
console.log("continua la ejecución del programa")

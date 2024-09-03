
//escribe un bucle "for" que imprima los numeros del 1 al 10


let numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
i = 0;
for (let i = 0; i < numeros.length; i++) {
    console.log (numeros[i]);
    
}


//crea un array con los nombres de tus amigos. Recorre el array e imprime cada nombre en la consola.

let amigos = ["Carlos", "Alan", "Cony", "Pamela"];
 
for (let i = 0; i < amigos.length; i++) {
    console.log (amigos[i]);
    
}

//Escribe un bucle "while" que imprima los números del 10 al 1 en orden decendente.

i = 10;
while (i > 0) {
    console.log(i);
    i--;
    
}

//Escribe un bucle "do...while" que pida al usuario un número mediante "prompt" y continue pidiendo números hasta que el usuario ingrese un número mayor a 100. Luego, imprime "Número mayor a 100 ingresado"
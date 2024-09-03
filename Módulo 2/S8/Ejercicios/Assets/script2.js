var paises = ["Chile", "Argentina", "Colombia"];

console.log(paises);

console.log(paises.length);

console.log(paises[1]);

for(let i = 0; i < paises.length; i ++){
    console.log(paises[i]);
   }

paises.push("Brasil");
console.log(paises)

paises.unshift("Uruguay");
console.log(paises);

paises.pop();
console.log(paises);

paises.shift();
console.log(paises);
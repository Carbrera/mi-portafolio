var auto = new Object();

auto.color = "rojo";
auto.numeroPuertas = 4;
auto.marca = "Samsung";

auto.acelerar = function () {
    console.log("El auto aceleró");
   }
auto.frenar = function () {
    console.log("El auto frenó");
   }
   
console.log(auto)

auto.frenar()

console.log(auto.marca);

//forma 2
var auto = {
    color: 'rojo',
    numeroPuertas: 4,
    marca: 'Samsung',
    acelerar: function () {
    console.log("El auto acelero");
    },
    frenar: function () {
    console.log("El auto freno");
    },
};

console.log(auto);
auto.acelerar();
console.log(auto.marca);

function Auto(color, numeroPuertas, marca) {
    this.color = color;
    this.numeroPuertas = numeroPuertas;
    this.marca = marca;
   }

   function Conductor(nombre, tipoLicencia, edad) {
    this.nombre = nombre;
    this.tipoLicencia = tipoLicencia;
    this.edad = edad;}
var miAuto1 = new Auto("Rojo", 4, "Nissan");
var miAuto2 = new Auto("Negro", 2, "Suzuki");

var conductor1 = new Conductor("Luis Ochoa", "B", 28);
var miAuto1 = new Auto("Rojo", 4, "Nissan", conductor1);
var miAuto2 = new Auto("Negro", 2, "Suzuki", conductor1);
console.log(miAuto1);
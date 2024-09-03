function Cliente(nombre, rut, clave, saldo) {
    this.nombre = nombre
    this.rut = rut
    this.clave = clave
    this.saldo = saldo
}

//Declaración para crear un objeto cliente
var cliente1 = new Cliente("Fulanito Perez", "210010011", "0001", 100000)
var cliente2 = new Cliente("Maria Delgado", "220020022", "0002", 200000)
var cliente3 = new Cliente("Jose Feliciano", "230030033", "0003", 300000)

var listaClientes = [cliente1, cliente2, cliente3] //lista para recorrer y buscar

//Cuando se ingrese el identificador y la clave, se revisará si coincide con alguno de los clientes registrados. 
//Si no coincide, se mostrará un mensaje de error.

alert("Bienvenido a Banca en Línea")
var identificador = prompt("Ingrese su identificador") //Ingreso de valores
var password = prompt("Ingrese su password") //Ingreso de valores

//Recorrer la lista con clientes
var usuario;
for (const iterator of listaClientes) {
    if (iterator.rut === identificador && iterator.clave === password) {
        usuario = iterator; //Cliente existe
        break;
    }
}

//Validación si el usuario fue encontrado
if (usuario) {
    alert("Bienvenido " + usuario.nombre)
    menu(usuario) //Llamada a función menú cuando el cliente existe 
}else {
    alert("Datos incorrectos")
}

//Función menú
function menu(usuario) { 
    do {
        var opcion = prompt("Seleccione que desea hacer:\n"+
            "1.- Ver saldo.\n" +
            "2.- Realizar giro\n" +
            "3.- Realizar deposito\n" +
            "4.- Salir"
        )

        switch (opcion) {
            case "1":
                verSaldo(usuario) 
                break;
            case "2":
                giro(usuario)
            break;
            case "3":
                deposito(usuario)
                break    
            case "4":
                break;
            default:
                break;
        }
    } while (opcion != "4");
}
function verSaldo(params) {
    alert("Su saldo es: " + params.saldo)
}
function giro(usuario) {
    var giro = parseInt(prompt("Su saldo es: " + usuario.saldo + ". \nIngrese el monto que desea girar:"))
                if (giro > usuario.saldo) {
                    alert("Saldo insuficiente.")
                } else {
                    usuario.saldo -= giro
                    alert("Retiro completado. Su nuevo saldo es: " + usuario.saldo)
                }
}
function deposito(usuario) {
    var deposito = parseInt(prompt("Su saldo actual es: "+ usuario.saldo + ". \nIngrese el monto que desea depositar:"))
            usuario.saldo += deposito
            alert("Depósito completado con éxito. Su nuevo saldo es: " + usuario.saldo)
}

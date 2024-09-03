do { 

var opcion = prompt("Soy el Profesor Oak \n" +
        "Ahí encima tienes 4 Pokémon \n" +
        "¿Cuál vas a elegir? \n" +
    "1.- Bulbasaur \n" +
    "2.- Charmander \n" +
    "3.- Squirtle  \n" +
    "4.- Eevee   \n" +
    "5.- No quiero")

//FUNCIONES
switch (opcion) {
    case "1":
        bulbasaur();
        break; 
    case "2":
        charmander();
        break;
    case "3":
        squirtle();
        break;
    case "4":
        eevee();
        break;
    case "5":
        alert ("Está bien. Si cambias de opinión estaré esperando.")
        break;
    default:
        alert("No tengo más que estos Pokémon, por ahora.")
        break;
}

} while (opcion !=5)
function bulbasaur() {
    var ingreso = prompt("¡Así que Bulbasaur! El inicial de tipo Planta. \n"+ "Resulta muy fácil criarlo. \n"+
        "1.- Lo quiero. \n"+
        "2.- Quiero ver otro. "
    )

    if (ingreso == "1") {
        alert("¿Estás seguro de tu decición? Ve los demás antes de tomarla")
    } else if (ingreso == "2"){
        alert("Ok. Veamos otro.")
    } else {
        alert("Solo elige una de esas dos opciones.")
    }
}

function charmander() {
    var ingreso = prompt("¡Así que Charmander! El inicial de tipo Fuego. \n"+ "Ten paciencia con él. \n"+
        "1.- Lo quiero. \n"+
        "2.- Quiero ver otro. "
    )
    if (ingreso == "1") {
        alert("¿Estás seguro de tu decición? Quizá otro te guste más")
    } else if (ingreso == "2"){
        alert("Ok. Veamos otro.")
    } else {
        alert("Solo elige una de esas dos opciones.")
    }
}

function squirtle() {
    var ingreso = prompt("¡Así que Squirtle! El inicial de tipo Agua. \n"+ "Merece mucho la pena. \n"+
        "1.- Lo quiero. \n"+
        "2.- Quiero ver otro. "
    )
    if (ingreso == "1") {
        alert("¿Estás seguro de tu decición? Veamos los otros antes de decidir.")
    } else if (ingreso == "2"){
        alert("Ok. Veamos otro.")
    } else {
        alert("Solo elige una de esas dos opciones.")
    }
}

function eevee() {
    var ingreso = prompt("¡Así que Eevee! El inicial de tipo Normal. \n"+ "Es adorable y ofrece varias posibilidades. \n"+
        "1.- Lo quiero. \n"+
        "2.- Quiero ver otro. "
    )
    if (ingreso == "1") {
        alert("¿Estás seguro de tu decición? Piénsalo bien.")
    } else if (ingreso == "2"){
        alert("Ok. Veamos otro.")
    } else {
        alert("Solo elige una de esas dos opciones.")
    }
}

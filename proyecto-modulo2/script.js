// Variable para mantener el estado de selección de botón
var botonSeleccionado = false;

// Función para generar la opción aleatoria de la computadora
function generarOpcionAleatoria() {
    var opciones = ["fa-hand-fist", "fa-hand", "fa-hand-scissors"];
    var numeroAleatorio = Math.floor(Math.random() * 3);
    return opciones[numeroAleatorio];
}

// Función para comparar la opción del usuario con la opción aleatoria de la computadora
function comparar(opcionUsuario) {
    // Obtener la opción aleatoria de la computadora
    var opcionComputadora = generarOpcionAleatoria();

    // Cambiar las clases de los elementos en intervalos de tiempo
    setTimeout(function() {
        document.getElementById("uno").classList.remove("no-dis");
    }, 0);

    setTimeout(function() {
        document.getElementById("uno").classList.add("no-dis");
        document.getElementById("dos").classList.remove("no-dis");
    }, 1000);

    setTimeout(function() {
        document.getElementById("dos").classList.add("no-dis");
        document.getElementById("tres").classList.remove("no-dis");
    }, 2000);

    setTimeout(function() {
        document.getElementById("tres").classList.add("no-dis");
    }, 3000);

    // Actualizar el icono de la computadora después de 3 segundos
    setTimeout(function () {
        var iconoComputadora = document.querySelector("#computer i");
        iconoComputadora.className = "fa-solid " + opcionComputadora;
    }, 3000); // 3000 milisegundos = 3 segundos

    // Esperar 3 segundos antes de mostrar el resultado
    setTimeout(function () {
        if (
            (opcionUsuario === "fa-hand-fist" && opcionComputadora === "fa-hand-scissors") ||
            (opcionUsuario === "fa-hand" && opcionComputadora === "fa-hand-fist") ||
            (opcionUsuario === "fa-hand-scissors" && opcionComputadora === "fa-hand")
        ) {
            document.getElementById("ganaste").classList.remove("no-dis");
            document.getElementById("perdiste").classList.add("no-dis");
            document.getElementById("empate").classList.add("no-dis");
        } else if (opcionUsuario === opcionComputadora) {
            document.getElementById("empate").classList.remove("no-dis");
            document.getElementById("ganaste").classList.add("no-dis");
            document.getElementById("perdiste").classList.add("no-dis");
        } else {
            document.getElementById("perdiste").classList.remove("no-dis");
            document.getElementById("ganaste").classList.add("no-dis");
            document.getElementById("empate").classList.add("no-dis");
        }
    }, 3000); // 3000 milisegundos = 3 segundos

    // Actualizar el estado de selección de botón
    botonSeleccionado = true;
}

// Función para cambiar la clase del elemento <i> dentro del div con id "cajauser"
function cambiarClaseIcono(clase) {
    var iconoUsuario = document.querySelector("#cajauser i");
    iconoUsuario.classList.remove("no-dis");
    iconoUsuario.className = "fa-solid " + clase;
}

// Función para restaurar la clase "no-dis" al elemento <i> dentro del div con id "cajauser"
function restaurarClaseIcono() {
    // Restaurar la clase solo si no se ha seleccionado un botón
    if (!botonSeleccionado) {
        var iconoUsuario = document.querySelector("#cajauser i");
        iconoUsuario.classList.add("no-dis");
    }
}

// Event listeners para los botones
document.getElementById("piedra").addEventListener("click", function() {
    botonSeleccionado = false; // Reiniciar el estado al hacer clic
    comparar("fa-hand-fist");
});

document.getElementById("papel").addEventListener("click", function() {
    botonSeleccionado = false;
    comparar("fa-hand");
});

document.getElementById("tijera").addEventListener("click", function() {
    botonSeleccionado = false;
    comparar("fa-hand-scissors");
});

// Event listeners para cambiar la clase en hover
document.getElementById("piedra").addEventListener("mouseover", function() {
    cambiarClaseIcono("fa-hand-fist");
});

document.getElementById("piedra").addEventListener("mouseout", function() {
    restaurarClaseIcono();
});

document.getElementById("papel").addEventListener("mouseover", function() {
    cambiarClaseIcono("fa-hand");
});

document.getElementById("papel").addEventListener("mouseout", function() {
    restaurarClaseIcono();
});

document.getElementById("tijera").addEventListener("mouseover", function() {
    cambiarClaseIcono("fa-hand-scissors ro-90");
});

document.getElementById("tijera").addEventListener("mouseout", function() {
    restaurarClaseIcono();
});

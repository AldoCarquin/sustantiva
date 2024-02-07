document.addEventListener('DOMContentLoaded', function() {
const boton = document.getElementById('boton');
const number = document.getElementById('numero');


boton.addEventListener('click', function () {

    let numeroActual = parseInt(number.innerText);


    numeroActual++;


    number.innerText = numeroActual;
});
});
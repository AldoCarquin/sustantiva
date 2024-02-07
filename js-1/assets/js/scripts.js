function guardarDatos() {
    // Obtener los valores de los campos de entrada
    var nombre = document.getElementById('nombre').value;
    var apellido = document.getElementById('apellido').value;
    document.getElementById('usuario').innerText = nombre + ' ' + apellido;

    var overallDiv = document.getElementById('overall');
    overallDiv.style.visibility = 'hidden';
    overallDiv.style.display = 'none';
}

var html1 = 0;
var html2 = 0;
var html3 = 0;
var css1 = 0;
var css2 = 0;
var css3 = 0;
var js1 = 0;
var js2 = 0;
var js3 = 0;
var promedioHtml = parseFloat(document.getElementById('htmlProm').innerText);


// HTML1
function modificarHtmlUno() {
    var notaHtmlUno = prompt("Por favor, ingresa nota de HTML1");

    if (notaHtmlUno !== null) {
        notaHtmlUno = parseFloat(notaHtmlUno);
        if (!isNaN(notaHtmlUno) && notaHtmlUno >= 0 && notaHtmlUno <= 70) {
            html1 = notaHtmlUno;
            document.getElementById('htmluno').innerText = notaHtmlUno;
        } else {
            alert("Por favor, ingresa un valor válido entre 0 y 70.");
        }
    } else {
        console.log("Entrada cancelada por el usuario");
    }
    actualizarPromedioHtml();
    actualizarPromedioPromedio();

}

// HTML2
function modificarHtmlDos() {
    var notaHtmlDos = prompt("Por favor, ingresa nota de HTML2");

    if (notaHtmlDos !== null) {
        notaHtmlDos = parseFloat(notaHtmlDos);
        if (!isNaN(notaHtmlDos) && notaHtmlDos >= 0 && notaHtmlDos <= 70) {
            html2 = notaHtmlDos;
            document.getElementById('htmldos').innerText = notaHtmlDos;
        } else {
            alert("Por favor, ingresa un valor válido entre 0 y 70.");
        }
    } else {
        console.log("Entrada cancelada por el usuario");
    }
    actualizarPromedioHtml();
    actualizarPromedioPromedio();
}

// HTML3
function modificarHtmlTres() {
    var notaHtmlTres = prompt("Por favor, ingresa nota de HTML3");

    if (notaHtmlTres !== null) {
        notaHtmlTres = parseFloat(notaHtmlTres);
        if (!isNaN(notaHtmlTres) && notaHtmlTres >= 0 && notaHtmlTres <= 70) {
            html3 = notaHtmlTres;
            document.getElementById('htmltres').innerText = notaHtmlTres;
        } else {
            alert("Por favor, ingresa un valor válido entre 0 y 70.");
        }
    } else {
        console.log("Entrada cancelada por el usuario");
    }
    actualizarPromedioHtml();
    actualizarPromedioPromedio();
}

// Actualiza el promedio de HTML
function actualizarPromedioHtml() {
    var promedioHtml = (html1 + html2 + html3) / 3;
    document.getElementById('htmlProm').innerText = promedioHtml.toFixed(0);
}

// CSS1 
function modificarCssUno() {
    var notaCssUno = prompt("Por favor, ingresa nota de CSS 1 ");

    if (notaCssUno !== null) {
        notaCssUno = parseFloat(notaCssUno);
        if (!isNaN(notaCssUno) && notaCssUno >= 0 && notaCssUno <= 70) {
            css1 = notaCssUno;
            document.getElementById('cssuno').innerText = notaCssUno;
        } else {
            alert("Por favor, ingresa un valor válido entre 0 y 70.");
        }
    } else {
        console.log("Entrada cancelada por el usuario");
    }
    actualizarPromedioCss();
    actualizarPromedioPromedio();
}

// CSS2 
function modificarCssDos() {
    var notaCssDos = prompt("Por favor, ingresa nota de CSS 2 ");

    if (notaCssDos !== null) {
        notaCssDos = parseFloat(notaCssDos);
        if (!isNaN(notaCssDos) && notaCssDos >= 0 && notaCssDos <= 70) {
            css2 = notaCssDos;
            document.getElementById('cssdos').innerText = notaCssDos;
        } else {
            alert("Por favor, ingresa un valor válido entre 0 y 70.");
        }
    } else {
        console.log("Entrada cancelada por el usuario");
    }
    actualizarPromedioCss();
    actualizarPromedioPromedio();
}

// CSS3 
function modificarCssTres() {
    var notaCssTres = prompt("Por favor, ingresa nota de CSS 3 ");

    if (notaCssTres !== null) {
        notaCssTres = parseFloat(notaCssTres);
        if (!isNaN(notaCssTres) && notaCssTres >= 0 && notaCssTres <= 70) {
            css3 = notaCssTres;
            document.getElementById('csstres').innerText = notaCssTres;
        } else {
            alert("Por favor, ingresa un valor válido entre 0 y 70.");
        }
    } else {
        console.log("Entrada cancelada por el usuario");
    }
    actualizarPromedioCss();
    actualizarPromedioPromedio();
}

// Actualiza el promedio de CSS
function actualizarPromedioCss() {
    var promedioCss = (css1 + css2 + css3) / 3;
    document.getElementById('cssProm').innerText = promedioCss.toFixed(0);
}

// Js1 
function modificarJsUno() {
    var notaJsUno = prompt("Por favor, ingresa nota de Js 1 ");

    if (notaJsUno !== null) {
        notaJsUno = parseFloat(notaJsUno);
        if (!isNaN(notaJsUno) && notaJsUno >= 0 && notaJsUno <= 70) {
            js1 = notaJsUno;
            document.getElementById('jsuno').innerText = notaJsUno;
        } else {
            alert("Por favor, ingresa un valor válido entre 0 y 70.");
        }
    } else {
        console.log("Entrada cancelada por el usuario");
    }
    actualizarPromedioJs();
    actualizarPromedioPromedio();
}

// Js2 
function modificarJsDos() {
    var notaJsDos = prompt("Por favor, ingresa nota de Js 2 ");

    if (notaJsDos !== null) {
        notaJsDos = parseFloat(notaJsDos);
        if (!isNaN(notaJsDos) && notaJsDos >= 0 && notaJsDos <= 70) {
            js2 = notaJsDos;
            document.getElementById('jsdos').innerText = notaJsDos;
        } else {
            alert("Por favor, ingresa un valor válido entre 0 y 70.");
        }
    } else {
        console.log("Entrada cancelada por el usuario");
    }
    actualizarPromedioJs();
    actualizarPromedioPromedio();
}

// Js3 
function modificarJsTres() {
    var notaJsTres = prompt("Por favor, ingresa nota de Js 3 ");

    if (notaJsTres !== null) {
        notaJsTres = parseFloat(notaJsTres);
        if (!isNaN(notaJsTres) && notaJsTres >= 0 && notaJsTres <= 70) {
            js3 = notaJsTres;
            document.getElementById('jstres').innerText = notaJsTres;
        } else {
            alert("Por favor, ingresa un valor válido entre 0 y 70.");
        }
    } else {
        console.log("Entrada cancelada por el usuario");
    }
    actualizarPromedioJs();
    actualizarPromedioPromedio();
}

// Actualiza el promedio de Js
function actualizarPromedioJs() {
    var promedioJs = (js1 + js2 + js3) / 3;
    document.getElementById('jsProm').innerText = promedioJs.toFixed(0);
}
function actualizarPromedioPromedio() {
    var promedioHtml = (html1 + html2 + html3) / 3;
    promedioCss = (css1 + css2 + css3) / 3;
    promedioJs = (js1 + js2 + js3) / 3;
    var promedioPromedio = (promedioHtml + promedioCss + promedioJs) / 3;
    document.getElementById('genProm').innerText = promedioPromedio.toFixed(0);
}


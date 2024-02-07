$(document).ready(function () {

    $("#alert").click(function () {
        var confirmacion = confirm("Presionaste el enlace. Ahora es irremediable irnos a google. Despidete de todo lo que has visto en esta página...");

        if (confirmacion) {
            window.location.href = "https://www.google.com";
        }
    });

    console.log("ola e.e")
});
$(function () {

    document.querySelector('.itemNav').classList.add('active');

    /* LIMITAR FECHA DE NACIMIENTO ANTES DE LA ACTUAL */

    let fechaNacimiento = document.querySelector('#born');

    if (fechaNacimiento != null) {
        let fechaActual = new Date().toISOString().split('T')[0];
        document.getElementById('born').min = '1950-01-01';
        document.getElementById('born').max = fechaActual;
    }

    /* CUADRO DE VERIFICACION ELIMINAR CUENTA */

    let eliminarCuenta = document.querySelector('.eliminarCuenta');

    if (eliminarCuenta != null) {
        $('.botonEliminar').click(() => {
            eliminarCuenta.addEventListener('submit', (evt) => {
                evt.preventDefault();
            });
            Swal.fire({
                title: "¿Deseas continuar?",
                text: "No podrás recuperar tu cuenta después de esto.",
                imageUrl: "../static/img/eliminarCuenta.gif",
                imageWidth: 400,
                imageHeight: 200,
                imageAlt: "Gift la roca",
                showCancelButton: true,
                confirmButtonColor: "#008f39",
                cancelButtonColor: "#d33",
                confirmButtonText: "Confirmar",
                cancelButtonText: "Cancelar"
            }).then((result) => {
                if (result.isConfirmed) {
                    eliminarCuenta.submit();
                }
            });
        });
    }

    /* MENSAJE DE VALIDACIÓN AL DAR SOBRE UN BOTÓN */

    let formulario = document.querySelector('form');

    if (formulario != null) {
        formulario.addEventListener('submit', (evt) => {
            evt.preventDefault();
            $('.error').css('display', 'none');
            $('.cargando').css('display', 'block');
            setTimeout(() => {
                $('.cargando').css('display', 'none');
                formulario.submit();
            }, 1000);
        });
    }

});
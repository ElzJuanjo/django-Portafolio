$(function () {
    /* BARRA DE NAVEGACION PRINCIPAL */

    function barraDeNavegacion() {
        const itemsMenu = document.querySelectorAll('.menu');
        const opcionesNav = document.querySelectorAll('.itemNav');
        const alturaHeader = document.querySelector('#inicio').offsetHeight;

        itemsMenu.forEach((item, index) => {
            let rangoItem;
            if (index == 0) {
                rangoItem = item.offsetTop - (alturaHeader / 2);
            } else {
                rangoItem = item.offsetTop + (alturaHeader / 2);
            }
            const alturaItem = item.offsetHeight;

            if (window.scrollY > rangoItem && window.scrollY < (rangoItem + alturaItem)) {
                opcionesNav.forEach(opcion => {
                    opcion.classList.remove('active');
                });
                opcionesNav[index].classList.add('active');
            }
        });
    }

    barraDeNavegacion();
    $(window).on('scroll', barraDeNavegacion);

});
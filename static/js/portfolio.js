$(function () {

    document.querySelector('#navProductos').classList.add('active');

    /* APLICACION DE FILTROS EN EL PORTAFOLIO */

    const navPortafolio = document.querySelectorAll('#filtroPortafolio');
    const imagenesApp = document.querySelectorAll('.app');
    const imagenesClass = document.querySelectorAll('.clases');
    const imagenesWeb = document.querySelectorAll('.web');

    function opacidadImg(img) {
        img.addEventListener('mouseenter', () => {
            img.style.transition = 'opacity 0.7s ease';
            img.style.opacity = '0.5';
            img.style.cursor = 'pointer';
        });
        img.addEventListener('mouseleave', () => {
            img.style.opacity = '1';
        });
    }

    imagenesApp.forEach(opacidadImg);
    imagenesClass.forEach(opacidadImg);
    imagenesWeb.forEach(opacidadImg);

    function transicionImg() {
        $('#imagenesP').css('opacity', '0');
        $('.app').css('opacity', '0');
        $('.clases').css('opacity', '0');
        $('.web').css('opacity', '0');

        setTimeout(function () {
            $('#imagenesP').css('opacity', '1');
            $('.app').css('opacity', '1');
            $('.clases').css('opacity', '1');
            $('.web').css('opacity', '1');
        }, 200);
    }

    function filtroImagenes(opcion) {
        switch (opcion) {
            case 0:
                $('#contenedorP').css('flex-direction', 'column');
                $('.app').css('display', 'inline');
                $('.clases').css('display', 'inline');
                $('.web').css('display', 'inline');
                break;
            case 1:
                $('#contenedorP').css('flex-direction', 'row');
                $('.app').css('display', 'inline');
                $('.clases').css('display', 'none');
                $('.web').css('display', 'none');
                break;
            case 2:
                $('#contenedorP').css('flex-direction', 'row');
                $('.app').css('display', 'none');
                $('.clases').css('display', 'inline');
                $('.web').css('display', 'none');
                break;
            case 3:
                $('#contenedorP').css('flex-direction', 'row');
                $('.app').css('display', 'none');
                $('.clases').css('display', 'none');
                $('.web').css('display', 'inline');
                break;
        }
        transicionImg();
    }

    function filtrosPortafolio(item) {
        if (item === navPortafolio[0]) {
            item.classList.add('active');
        }
        item.addEventListener('click', () => {
            navPortafolio.forEach(item2 => {
                item2.classList.remove('active');
            });
            item.classList.add('active');
            if (item === navPortafolio[0]) {
                filtroImagenes(0);
            } else if (item === navPortafolio[1]) {
                filtroImagenes(1);
            } else if (item === navPortafolio[2]) {
                filtroImagenes(2);
            } else if (item === navPortafolio[3]) {
                filtroImagenes(3);
            }
        });
    }

    navPortafolio.forEach(filtrosPortafolio);

});
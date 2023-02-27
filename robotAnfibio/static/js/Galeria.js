function mostrarImagen(fuente,nombre)
{
    //captura de elementos HTML
    nombreFoto = document.getElementById('nombreFoto')
    fuenteFoto = document.getElementById('fuenteFoto')

    nombreFoto.innerHTML = nombre
    fuenteFoto.src = '/static/' + fuente
}

function mostrarVideo()
{
    barraFoto = document.getElementById('barraFoto')
    barraVideo = document.getElementById('barraVideo')

    btnVideo = document.getElementById('btnVideo')
    btnFoto = document.getElementById('btnFoto')

    contenedorFoto = document.getElementById('fotosTotales')
    contenedorVideo = document.getElementById('videosTotales')

    contenedorFoto.style.display = 'none'
    contenedorVideo.style.display = 'none'

    barraFoto.style.display = 'none'
    barraVideo.style.display = 'none'

    btnVideo.style.color = 'black'
    btnVideo.style.backgroundColor = '#96EADA'

    btnFoto.style.color = "#96EADA"
    btnFoto.style.backgroundColor = "transparent"

    contenedorVideo.style.display = 'flex'

    barraVideo.style.display = ''
}

function mostrarFoto()
{
    barraFoto = document.getElementById('barraFoto')
    barraVideo = document.getElementById('barraVideo')

    btnVideo = document.getElementById('btnVideo')
    btnFoto = document.getElementById('btnFoto')

    contenedorFoto = document.getElementById('fotosTotales')
    contenedorVideo = document.getElementById('videosTotales')

    contenedorFoto.style.display = 'none'
    contenedorVideo.style.display = 'none'

    barraFoto.style.display = 'none'
    barraVideo.style.display = 'none'

    btnFoto.style.color = 'black'
    btnFoto.style.backgroundColor = '#96EADA'

    btnVideo.style.color = "#96EADA"
    btnVideo.style.backgroundColor = "transparent"

    contenedorFoto.style.display = 'flex'

    barraFoto.style.display = ''
}

function cerrarVideo() {
    fuenteVideo = document.getElementById('fuenteVideo')
    fuenteVideo.src = ''
}

function verVideo(fuente,nombre)
{
    //captura de elementos HTML
    nombreVideo = document.getElementById('nombreVideo')
    fuenteVideo = document.getElementById('fuenteVideo')

    nombreVideo.innerHTML = nombre
    fuenteVideo.src = '/static/' + fuente
}

function buscarVideo(elemento)
{
    videosTotales = document.querySelectorAll('.busquedaVideo')
    videosTotales.forEach(element => {
        if(element.children[1].children[0].innerText.indexOf(elemento.value) > -1)
        {
            element.style.display = ''
        }
        else
        {
            element.style.display = 'none'
        }
    });
}

function buscarFoto(elemento)
{
    fotosTotales = document.querySelectorAll('.busquedaFoto')
    fotosTotales.forEach(element => {
        if(element.children[1].children[0].innerText.indexOf(elemento.value) > -1)
        {
            element.style.display = ''
        }
        else
        {
            element.style.display = 'none'
        }
    });
}
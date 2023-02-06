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
    btnVideo = document.getElementById('btnVideo')
    btnFoto = document.getElementById('btnFoto')

    contenedorFoto = document.getElementById('fotosTotales')
    contenedorVideo = document.getElementById('videosTotales')

    contenedorFoto.style.display = 'none'
    contenedorVideo.style.display = 'none'

    btnVideo.style.color = 'black'
    btnVideo.style.backgroundColor = '#96EADA'

    btnFoto.style.color = "#96EADA"
    btnFoto.style.backgroundColor = "transparent"

    contenedorVideo.style.display = 'flex'
}

function mostrarFoto()
{
    btnVideo = document.getElementById('btnVideo')
    btnFoto = document.getElementById('btnFoto')

    contenedorFoto = document.getElementById('fotosTotales')
    contenedorVideo = document.getElementById('videosTotales')

    contenedorFoto.style.display = 'none'
    contenedorVideo.style.display = 'none'

    btnFoto.style.color = 'black'
    btnFoto.style.backgroundColor = '#96EADA'

    btnVideo.style.color = "#96EADA"
    btnVideo.style.backgroundColor = "transparent"

    contenedorFoto.style.display = 'flex'
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
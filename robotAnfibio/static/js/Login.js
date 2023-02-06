function usuarioSeleccionado(infoUsuario) {
    document.querySelectorAll('.userInfo').forEach(elemento => {
        elemento.style.display = 'none'
    })

    idUsuario = infoUsuario.slice(3)
    cntUsuario = 'cnt' + idUsuario
    document.getElementById(cntUsuario).style.display = 'flex'

    //Datos del usuario
    nombreUsuario = 'nom' + idUsuario
    codigoUsuario = 'cod' + idUsuario
    contraMensaje = 'con' + idUsuario
    contraIngreso = 'inp' + idUsuario
    submitUsuario = 'sub' + idUsuario
    saludoUsuario = 'sal' + idUsuario

    //Elementos HTML
    document.getElementById(nombreUsuario).style.display = 'none'
    document.getElementById(codigoUsuario).style.display = 'none'
    document.getElementById(contraMensaje).style.display = 'flex'
    document.getElementById(contraIngreso).style.display = 'flex'
    document.getElementById(submitUsuario).style.display = 'flex'
    document.getElementById(saludoUsuario).style.display = 'flex'

    //Datos del HTML
    document.getElementById('refrescar').style.display = 'flex'
    document.getElementById('mensajeGeneral').style.display = 'none'
}

document.addEventListener("DOMContentLoaded", ()=>{
    btnLeft = document.getElementById('btnLeft')
    btnRight = document.getElementById('btnRight')

    btnLeft.onclick = function() {
        document.getElementById('usuariosLogin').scrollLeft -= 50
    }

    btnRight.onclick = function() {
        document.getElementById('usuariosLogin').scrollLeft += 50
    }
})
document.addEventListener("DOMContentLoaded", ()=>{
    btnLeft = document.getElementById('btnIzquierda')
    btnRight = document.getElementById('btnDerecha')

    btnLeft.onclick = function() {
        document.getElementById('embarcacionSeleccion').scrollLeft -= 50
    }

    btnRight.onclick = function() {
        document.getElementById('embarcacionSeleccion').scrollLeft += 50
    }
})
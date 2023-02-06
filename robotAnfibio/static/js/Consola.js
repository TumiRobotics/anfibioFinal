document.addEventListener("DOMContentLoaded", ()=>{
    btnLeft = document.getElementById('btnLeft')
    btnRight = document.getElementById('btnRight')

    btnLeft.onclick = function() {
        document.getElementById('opcionesAdmin').scrollLeft -= 50
    }

    btnRight.onclick = function() {
        document.getElementById('opcionesAdmin').scrollLeft += 50
    }
})
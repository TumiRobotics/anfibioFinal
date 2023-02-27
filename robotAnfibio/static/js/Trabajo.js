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

function buscarBarco(elemento)
{
    codigosBarcos = document.querySelectorAll('.buscarBarco')
    codigosBarcos.forEach(element => {
        if(element.children[0].children[1].innerText.indexOf(elemento.value) > -1)
        {
            element.style.display = 'flex'
        }
        else
        {
            element.style.display = 'none'
        }
    });
}
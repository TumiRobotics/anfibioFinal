let capturaVideo = '0'

let lucesEncendidas = '0'
let hidrolavadoraEncendida = '0'
let cepillosEncendidos = '0'

function encenderLuces()
{
    if(lucesEncendidas === '0')
    {
        lucesEncendidas = '1'
        fetch('/encenderLuces')
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
    }
    else
    {
        lucesEncendidas = '0'
        fetch('/apagarLuces')
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
    }
}

function encenderHidrolavadora()
{
    if(hidrolavadoraEncendida === '0')
    {
        hidrolavadoraEncendida = '1'
        fetch('/encenderHidrolavadora')
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
    }
    else
    {
        hidrolavadoraEncendida = '0'
        fetch('/apagarHidrolavadora')
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
    }
}

function encenderCepillos()
{
    if(cepillosEncendidos === '0')
    {
        cepillosEncendidos = '1'
        fetch('/encenderCepillos')
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
    }
    else
    {
        cepillosEncendidos = '0'
        fetch('/apagarCepillos')
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
    }
}


function capturarFoto()
{
    fetch('/capturarFotoInspeccion')
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
}

function capturarVideo()
{
    if(capturaVideo === '0')
    {
        capturaVideo = '1'
        fetch('/capturarVideoInspeccion')
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
    }
    else
    {
        capturaVideo = '0'
        fetch('/detenerVideoInspeccion')
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
    }
}


document.addEventListener('DOMContentLoaded',()=>{

    let ingresoVelocidad = document.getElementById('ingresoVelocidad')
    let valorVelocidad = document.getElementById('valorVelocidad')

    ingresoVelocidad.onchange = function() 
    {
        console.log(ingresoVelocidad.value)
        valorVelocidad.innerHTML = ingresoVelocidad.value
    }

    let infoSonar = document.getElementById('sonarData');
    let graficaSonar = echarts.init(infoSonar);

    setInterval(()=>{
        fetch("/capturarInfoSonar")
        .then(response => response.json())
        .then(data => {
            info = data.data
            graficaSonar.setOption({
                    legend: {
                        data: ['line']
                    },
                    polar: {},
                    tooltip: {
                        trigger: 'axis',
                        axisPointer : {
                            type: 'cross'
                        }
                    },
                    angleAxis: {
                        type:'value',
                        startAngle: 0
                    },
                    radiusAxis: {},
                    series: [
                        {
                            coordinateSystem: 'polar',
                            name: 'line',
                            type: 'line',
                            data: info
                        }
                    ]
                }
            );
        })
    },3000)

    setInterval(()=>{
        fetch('/capturarInfoSensorInercial')
        .then(response => response.json())
        .then(data => {
            document.getElementById('d1').innerHTML = data.ddata[0]
            document.getElementById('d2').innerHTML = data.ddata[1]
            document.getElementById('v1').innerHTML = data.vdata[0]
            document.getElementById('v2').innerHTML = data.vdata[1]
            document.getElementById('n1').innerHTML = data.ndata[0]
            document.getElementById('n2').innerHTML = data.ndata[1]
        })
    },3000)

    setInterval(()=>{
        fetch('/getSizeProject')
        .then(response => response.json())
        .then(data => {
            document.getElementById('almacenamientoInfo').innerHTML = data.total
        })
    },2000)

    setInterval(()=>{
        fetch('/getInfoProject')
        .then(response => response.json())
        .then(data => {
            document.getElementById('sensorD').innerHTML = data.sensorD
            document.getElementById('sensorH').innerHTML = data.sensorH
        })
    },2000)

})
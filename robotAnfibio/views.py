from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import UsuarioAnfibio, EmbarcacionesAnfibio, InspeccionesAnfibio
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import random
import os
import cv2
import subprocess as sp
import datetime
from PIL import Image

# Create your views here.
ruta_fotos_inspeccion = ''
ruta_videos_inspeccion = ''
counter_fotos = '1'
counter_videos = '1'
app_video = None
inicio_inspeccion = None
fin_inspeccion = None

def inicio(request):
    return render(request,'robotAnfibio/inicio.html')

@csrf_exempt
def log_in(request):
    if request.method == 'POST':
        usuarioUsername = request.POST.get('usuarioUsername')
        usuarioContra = request.POST.get('usuarioContra')
        usuarioAcceso = authenticate(request,username=usuarioUsername,password=usuarioContra)
        print(usuarioAcceso)
        if usuarioAcceso is not None:
            login(request,usuarioAcceso)
            if usuarioAcceso.tipo_usuario == 'Admin':
                return HttpResponseRedirect(reverse('robotAnfibio:consola'))
            if usuarioAcceso.tipo_usuario == 'Operador':
                return HttpResponseRedirect(reverse('robotAnfibio:main'))
        else:
            return HttpResponseRedirect(reverse('robotAnfibio:login'))
    return render(request,'robotAnfibio/login.html',{
        'usuarios':UsuarioAnfibio.objects.all().order_by('id')
    })

@login_required(login_url='/login')
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('robotAnfibio:login'))

@login_required(login_url='/login')
def main(request):
    return render(request,'robotAnfibio/main.html',{
        'usuario':'Alexander'
    })

def consola(request):
    return render(request,'robotAnfibio/consola.html')

@csrf_exempt
def nuevoUsuario(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        apellidoUsuario = request.POST.get('apellidoUsuario')
        celularUsuario = request.POST.get('celularUsuario')
        emailUsuario = request.POST.get('emailUsuario')
        contraUsuario = request.POST.get('contraUsuario')
        tipoUsuario = request.POST.get('tipoUsuario')
        user_name = nombreUsuario.lower() + apellidoUsuario.lower().capitalize()
        UsuarioAnfibio(
            username=user_name,
            email=emailUsuario,
            first_name=nombreUsuario,
            last_name=apellidoUsuario,
            numero_celular=celularUsuario,
            tipo_usuario=tipoUsuario,
        ).save()
        usuario_activo = UsuarioAnfibio.objects.latest('id')
        usuario_activo.set_password(contraUsuario)
        codigoUsuario = str(usuario_activo.id)
        while len(codigoUsuario) < 4:
            codigoUsuario = '0' + codigoUsuario
        usuario_activo.codigo_usuario = 'USR-' + codigoUsuario
        usuario_activo.imagen_usuario = f'usr/usr-{codigoUsuario}.png'
        usuario_activo.save()
        Image.open(request.FILES.get('fotoUsuario')).save(f'./robotAnfibio/static/usr/usr-{codigoUsuario}.png')
        return HttpResponseRedirect(reverse('robotAnfibio:consola'))
    return render(request,'robotAnfibio/nuevoUsuario.html')

@login_required(login_url='/login')
def monitoreo(request,ind):
    global ruta_fotos_inspeccion
    global ruta_videos_inspeccion
    global inicio_inspeccion
    codigo_embarcacion = ind
    ult_inspeccion = InspeccionesAnfibio.objects.latest('id')
    indicador = str(ult_inspeccion.id + 1)
    while len(indicador) < 4:
        indicador = '0' + indicador
    codigo_inspeccion = 'INS-' + indicador
    nombre_directorio = 'ins-' + indicador + '/'
    ruta_directorio_general = './robotAnfibio/static/ins/' + nombre_directorio
    ruta_directorio_videos = ruta_directorio_general + 'videos/'
    ruta_directorio_fotos = ruta_directorio_general + 'fotos/'
    ruta_fotos = 'ins/' + nombre_directorio + 'fotos/'
    ruta_videos = 'ins/' + nombre_directorio + 'videos/'
    os.mkdir(ruta_directorio_general)
    os.mkdir(ruta_directorio_videos)
    os.mkdir(ruta_directorio_fotos)
    InspeccionesAnfibio(codigo_inspeccion=codigo_inspeccion,ruta_fotos=ruta_fotos,ruta_videos=ruta_videos,embarcacion_inspeccion=codigo_embarcacion,duracion_inspeccion='0',distancia_inspeccion='0').save()
    ruta_fotos_inspeccion = ruta_directorio_fotos
    ruta_videos_inspeccion = ruta_directorio_videos
    inicio_inspeccion = datetime.datetime.now()
    return render(request,'robotAnfibio/monitoreo.html')

@login_required(login_url='/login')
def trabajo(request):
    return render(request,'robotAnfibio/trabajo.html',{
        'embarcacionesAnfibio':EmbarcacionesAnfibio.objects.all().order_by('id'),
    })

@login_required(login_url='/login')
def estadisticas(request):
    inspecciones = InspeccionesAnfibio.objects.all().order_by('-id')
    distanciaTotal = 0.00
    nroRecorridos = 0
    duracionTotal = 0.00

    nroRecorridos = str(len(inspecciones))
    for inspecion in inspecciones:
        distanciaTotal = distanciaTotal + float(inspecion.distancia_inspeccion)
    distanciaTotal = round(distanciaTotal,2)
    distanciaTotal = str(distanciaTotal)

    for inspecion in inspecciones:
        duracionTotal = duracionTotal + float(inspecion.duracion_inspeccion)
    duracionTotal = round(duracionTotal,2)
    duracionTotal = str(duracionTotal)
    return render(request,'robotAnfibio/estadisticas.html',{
        'inspecciones':inspecciones,
        'distanciaTotal':distanciaTotal,
        'nroRecorridos':nroRecorridos,
        'duracionTotal':duracionTotal,
    })

@login_required(login_url='/login')
def galeria(request,ind):
    fuentes_fotos = []
    fuentes_videos = []
    if ind == '0':
        inspeccionesTotales = InspeccionesAnfibio.objects.all().order_by('id')
        for inspeccion in inspeccionesTotales:
            fotos_totales = os.listdir('robotAnfibio/static/' + inspeccion.ruta_fotos)
            videos_totales = os.listdir('robotAnfibio/static/' + inspeccion.ruta_videos)
            for foto in fotos_totales:
                if foto[:3] == 'img':
                    fuentes_fotos.append([inspeccion.ruta_fotos + foto, inspeccion.codigo_inspeccion + '-' + (foto.split('.')[0])])
            for video in videos_totales:
                if video[:3] == 'vid':
                    fuentes_videos.append([inspeccion.ruta_videos + video, inspeccion.codigo_inspeccion + '-' + (video.split('.')[0])])
    else:
        inspeccionInfo = InspeccionesAnfibio.objects.get(id=ind)
        fotos_totales = os.listdir('robotAnfibio/static/' + inspeccionInfo.ruta_fotos)
        videos_totales = os.listdir('robotAnfibio/static/' + inspeccionInfo.ruta_videos)
        for foto in fotos_totales:
            if foto[:3] == 'img':
                fuentes_fotos.append([inspeccionInfo.ruta_fotos + foto, inspeccionInfo.codigo_inspeccion + '-' + (foto.split('.')[0])])
        for video in videos_totales:
            if video[:3] == 'vid':
                fuentes_videos.append([inspeccionInfo.ruta_videos + video, inspeccionInfo.codigo_inspeccion + '-' + (video.split('.')[0])])

    return render(request,'robotAnfibio/galeria.html',{
        'fotos':fuentes_fotos,
        'videos':fuentes_videos,
        'ind':ind
    })

def terminarInspeccion(request):
    global ruta_fotos_inspeccion
    global ruta_videos_inspeccion
    global counter_fotos
    global counter_videos
    global app_video
    global inicio_inspeccion
    global fin_inspeccion
    fin_inspeccion = datetime.datetime.now()
    inspeccionActualizar = InspeccionesAnfibio.objects.latest('id')
    duracion_ins = fin_inspeccion - inicio_inspeccion
    duracion_total = round(duracion_ins.total_seconds(),2)
    duracion_total = duracion_total / 3600
    duracion_total = str(round(duracion_total,2))
    inspeccionActualizar.duracion_inspeccion = duracion_total
    inspeccionActualizar.save()
    ruta_fotos_inspeccion = ''
    ruta_videos_inspeccion = ''
    counter_fotos = '1'
    counter_videos = '1'
    app_video = None
    return HttpResponseRedirect(reverse('robotAnfibio:main'))

@login_required(login_url='/login')
def capturarInfoSonar(request):
    data = []
    i = 0
    while i < 360:
        data.append([random.randint(80,100),i])
        i = i + 5
    return JsonResponse({
        'data':data,
    })

@login_required(login_url='/login')
def capturarInfoSensorInercial(request):
    #Sensor Inercial
    return JsonResponse({
        'ddata':[random.randint(5,20),random.randint(5,10)],
        'vdata':[random.randint(10,20),random.randint(15,35)],
        'ndata':[random.randint(0,5),random.randint(85,95)],
    })

def capturarFotoInspeccion(request):
    global ruta_fotos_inspeccion
    global counter_fotos
    nombre_foto = 'img' + str(counter_fotos)
    counter_fotos = str(int(counter_fotos) + 1)
    #capturaFotos = cv2.VideoCapture(0)
    capturaFotos = cv2.VideoCapture("http://192.168.137.80:8080/?action=stream")
    ret, cv_img = capturaFotos.read()
    if ret:
        cv2.imwrite(ruta_fotos_inspeccion + str(nombre_foto) + ".png",cv_img)
        capturaFotos.release()
        return JsonResponse({
            'resp':'200'
        })
    else:
        return JsonResponse({
            'resp':'404'
        })

def capturarVideoInspeccion(request):
    global ruta_videos_inspeccion
    global counter_videos
    global app_video
    nombre_video = 'vid' + str(counter_videos)
    counter_videos = str(int(counter_videos) + 1)
    app_video = sp.Popen(['python3','video_cliente.py',f'{ruta_videos_inspeccion}{nombre_video}.mp4'])
    return JsonResponse({
        'resp':'Grabando',
    })

def detenerVideoInspeccion(request):
    global app_video
    if app_video is not None:
        app_video.terminate()
        app_video = None
    else:
        pass
    return JsonResponse({
        'resp':'Detenido',
    })

def encendeCepillos(request):
    print('Se apagara los cepillos')
    return JsonResponse({
        'resp':'ok'
    })

def apagarCepillos(request):
    print('Se encendera los cepillos')
    return JsonResponse({
        'reps':'ok'
    })

def encenderLuces(request):
    print('Se encenderan las luces')
    return JsonResponse({
        'resp':'ok'
    })

def apagarLuces(request):
    print('Se apagaran las luces')
    return JsonResponse({
        'resp':'ok'
    })

def encenderHidrolavadora(request):
    print('Se encendera la hidrolavadora')
    return JsonResponse({
        'resp':'ok'
    })

def apagarHidrolavadora(request):
    print('Se apagara la hidrolavoadora')
    return JsonResponse({
        'resp':'ok'
    })
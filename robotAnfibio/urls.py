from django.urls import path
from . import views

app_name='robotAnfibio'

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('login',views.log_in,name='login'),
    path('logout',views.log_out,name='logout'),
    path('main',views.main,name='main'),
    path('consola',views.consola,name='consola'),
    path('nuevoUsuario',views.nuevoUsuario,name='nuevoUsuario'),
    path('monitoreo/<str:ind>',views.monitoreo,name='monitoreo'),
    path('trabajo',views.trabajo,name='trabajo'),
    path('estadisticas',views.estadisticas,name='estadisticas'),
    path('galeria/<str:ind>',views.galeria,name='galeria'),
    path('terminarInspeccion',views.terminarInspeccion,name='terminarInspeccion'),
    path('encenderLuces',views.encenderLuces,name='encenderLuces'),
    path('apagarLuces',views.apagarLuces,name='apagarLuces'),
    path('encenderHidrolavadora',views.encenderHidrolavadora,name='encenderHidrolavadora'),
    path('apagarHidrolavadora',views.apagarHidrolavadora,name='encenderCepillos'),
    path('encenderCepillos',views.encendeCepillos,name='apagarCepillos'),
    path('apagarCepillos',views.apagarCepillos,name='apagarHidrolavadora'),
    path('capturarFotoInspeccion',views.capturarFotoInspeccion,name='capturarFotoInspeccion'),
    path('capturarVideoInspeccion',views.capturarVideoInspeccion,name='capturarVideoInspeccion'),
    path('detenerVideoInspeccion',views.detenerVideoInspeccion,name='detenerVideoInspeccion'),
    path('capturarInfoSonar',views.capturarInfoSonar,name='capturarInfoSonar'),
    path('capturarInfoSensorInercial',views.capturarInfoSensorInercial,name='capturarInfoSensorInercial'),
]
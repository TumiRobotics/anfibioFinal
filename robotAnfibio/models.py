from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.

class UsuarioAnfibio(AbstractUser):
    codigo_usuario = models.CharField(max_length=32, null=True, blank=True)
    numero_celular = models.CharField(max_length=32, null=True, blank=True)
    imagen_usuario = models.CharField(max_length=32, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=32, null=True, blank=True)

class EmbarcacionesAnfibio(models.Model):
    codigo_embarcacion = models.CharField(max_length=32, null=True, blank=True)
    imagen_embarcacion = models.CharField(max_length=32, null=True, blank=True)

class InspeccionesAnfibio(models.Model):
    codigo_inspeccion = models.CharField(max_length=32, blank=True, null=True)
    ruta_fotos = models.CharField(max_length=128, blank=True, null=True)
    ruta_videos = models.CharField(max_length=128, blank=True, null=True)
    duracion_inspeccion = models.CharField(max_length=128, blank=True, null=True)
    distancia_inspeccion = models.CharField(max_length=128, blank=True, null=True)
    fecha_inspeccion = models.DateTimeField(default=datetime.date.today)
    embarcacion_inspeccion = models.CharField(max_length=128, blank=True, null=True)

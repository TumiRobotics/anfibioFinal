from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UsuarioAnfibio(AbstractUser):
    codigo_usuario = models.CharField(max_length=32, null=True, blank=True)
    numero_celular = models.CharField(max_length=32, null=True, blank=True)
    imagen_usuario = models.CharField(max_length=32, null=True, blank=True)

class EmbarcacionesAnfibio(models.Model):
    codigo_embarcacion = models.CharField(max_length=32, null=True, blank=True)
    imagen_embarcacion = models.CharField(max_length=32, null=True, blank=True)
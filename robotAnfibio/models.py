from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UsuarioAnfibio(AbstractUser):
    codigo_usuario = models.CharField(max_length=32)
    numero_celular = models.CharField(max_length=32)
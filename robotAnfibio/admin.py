from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import UsuarioAnfibio, EmbarcacionesAnfibio, InspeccionesAnfibio

# Register your models here.
"""
Admin page is modified in this section
UsuarioRegistro is the model which modifies UsuarioAnfibio
changing its representation in admin web page
"""

class UsuarioRegistro(UserAdmin):
    list_display = ('username','email','first_name','last_name','codigo_usuario','numero_celular')
    fieldsets = (
        (
            None, {
                'fields':('username','password')
            }
        ),
        (
            "Informacion personal", {
                "fields":('first_name','last_name','email')
            }
        ),
        (
            "Permisos", {
                "fields":('is_active','is_staff','is_superuser','groups','user_permissions')
            }
        ),
        (
            "Fechas importantes", {
                'fields':('last_login','date_joined')
            }
        ),
        (
            'Informacion adicional', {
                'fields':('codigo_usuario','numero_celular')
            }
        )
    )
    add_fieldsets = (
        (
            None, {
                'fields':('username','password1','password2')
            }
        ),
        (
            "Informacion personal", {
                "fields":('first_name','last_name','email')
            }
        ),
        (
            "Permisos", {
                "fields":('is_active','is_staff','is_superuser','groups','user_permissions')
            }
        ),
        (
            "Fechas importantes", {
                'fields':('last_login','date_joined')
            }
        ),
        (
            'Informacion adicional', {
                'fields':('codigo_usuario','numero_celular')
            }
        )
    )
    

admin.site.register(UsuarioAnfibio,UsuarioRegistro)
admin.site.register(EmbarcacionesAnfibio)
admin.site.register(InspeccionesAnfibio)
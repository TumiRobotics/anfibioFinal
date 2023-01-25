# Generated by Django 4.1.5 on 2023-01-25 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotAnfibio', '0005_embarcacionesanfibio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='embarcacionesanfibio',
            name='imagen_embarcacion',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='usuarioanfibio',
            name='imagen_usuario',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='embarcacionesanfibio',
            name='codigo_embarcacion',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]

from django.db import models

# Create your models here.

class Proyecto(models.Model):
    ESTADOS = (
        ("Entregado", "Entregado"),
        ("En construcción", "En construcción"),
        ("Lanzamiento", "Lanzamiento")
    )

    imagen1 = models.ImageField(null=True, blank=True, upload_to='Proyectos')
    imagen2 = models.ImageField(null=True, blank=True, upload_to='Proyectos')
    imagen3 = models.ImageField(null=True, blank=True, upload_to='Proyectos')
    logo = models.ImageField(null=True, blank=True, upload_to='Proyectos')
    nombre = models.TextField(max_length=50)
    is_vis = models.BooleanField(default=False)
    piscina = models.BooleanField(default=False)
    gimnasio = models.BooleanField(default=False)
    salon_social = models.BooleanField(default=False)
    cancha_squash = models.BooleanField(default=False)
    parque_infantil = models.BooleanField(default=False)
    lobby = models.BooleanField(default=False)
    parqueaderos = models.BooleanField(default=False)
    cuarto_util = models.BooleanField(default=False)
    sala_cine = models.BooleanField(default=False)
    senderos = models.BooleanField(default=False)
    parque_mascotas = models.BooleanField(default=False)
    estado = models.CharField(max_length=50, choices=ESTADOS)
    ubicacion = models.TextField(max_length=50)
    site_url = models.CharField(max_length=200, null=True, blank=True)
    ig_url = models.CharField(max_length=200, null=True, blank=True)
    fb_url = models.CharField(max_length=200, null=True, blank=True)
    tiktok_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre

class ProyectoDestacado(models.Model):
    imagen = models.ImageField(null=True, blank=True, upload_to='Carrusel Destacados')
    logo = models.ImageField(null=True, blank=True, upload_to='Carrusel Destacados')
    site_url = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=50, default='¡Últimas unidades!')
    color = models.CharField(max_length=50, default='#004763')
    nombre = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre
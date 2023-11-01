from django.db import models
from galleryfield.fields import GalleryField


# Create your models here.

class Proyecto(models.Model):
    Imagen1 = models.ImageField(null=True, blank=True, upload_to='static/Imagenes/Proyectos')
    Imagen2 = models.ImageField(null=True, blank=True, upload_to='static/Imagenes/Proyectos')
    Imagen3 = models.ImageField(null=True, blank=True, upload_to='static/Imagenes/Proyectos')
    Logo = models.ImageField(null=True, blank=True, upload_to='static/Imagenes/Proyectos')
    nombre = models.TextField(max_length=50)
    areaConstruida = models.TextField(max_length=100)
    areaConstruidaUrbanismo = models.TextField(max_length=100)
    estado = models.TextField(max_length=20)
    ubicacion = models.TextField(max_length=50)
    ig_url = models.CharField(max_length=200, null=True, blank=True)
    fb_url = models.CharField(max_length=200, null=True, blank=True)
    tiktok_url = models.CharField(max_length=200, null=True, blank=True)
from django.db import models

# Create your models here.

class Proyecto(models.Model):
    ESTADOS = (
        ("Entregado", "Entregado"),
        ("En construcción", "En construcción"),
        ("Lanzamiento", "Lanzamiento"),
        ("En ventas", "En ventas")
    )
    PRIORIDADES = (
        ("Alta", "Alta"),
        ("Media", "Media"),
        ("Baja", "Baja")
    )

    imagen1 = models.ImageField(null=True, blank=True, upload_to='Proyectos')
    imagen2 = models.ImageField(null=True, blank=True, upload_to='Proyectos')
    imagen3 = models.ImageField(null=True, blank=True, upload_to='Proyectos')
    logo = models.ImageField(null=True, blank=True, upload_to='Proyectos')
    nombre = models.TextField(max_length=50)
    vis = models.BooleanField(default=False)
    comercial = models.BooleanField(default=False)
    luxury_home = models.BooleanField(default=False)
    vivienda_turistica = models.BooleanField(default=False)
    prioridad = models.CharField(max_length=50, choices=PRIORIDADES, default='Baja')
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

class Nosotros(models.Model):
    SECCIONES = (
        ("Misión", "Misión"),
        ("Visión", "Visión")
    )
    seccion = models.CharField(max_length=50, choices=SECCIONES)
    descripcion = models.TextField(max_length=None)

    def __str__(self):
        return self.seccion

class Contacto(models.Model):
    SECCIONES = (
        ("Contacto", "Contacto"),
        ("Ubicación", "Ubicación")
    )
    seccion =  models.CharField(max_length=50, choices=SECCIONES)
    nombre = models.CharField(max_length=20, null=True, blank=True)
    contenido = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre

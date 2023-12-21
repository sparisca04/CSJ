from django.contrib import admin
from .models import Proyecto, ProyectoDestacado, Nosotros, Contacto

# Register your models here.

admin.site.register(Proyecto)
admin.site.register(ProyectoDestacado)
admin.site.register(Nosotros)
admin.site.register(Contacto)

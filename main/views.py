from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Proyecto, ProyectoDestacado, Nosotros, Contacto

# Create your views here.

def home(request):
    infoContacto = Contacto.objects.all()
    proyectos = Proyecto.objects.all()
    proyectosDestacados = ProyectoDestacado.objects.all().order_by('nombre')
    return render(request, "main/home.html", {'proyectosDestacados': proyectosDestacados, 'proyectos': proyectos, 'infoContacto': infoContacto})

def proyectos(request):
    infoContacto = Contacto.objects.all()
    proyectos = Proyecto.objects.all()
    return render(request, "main/proyectos.html", {'proyectos': proyectos, 'infoContacto': infoContacto})

def nosotros(request):
    infoContacto = Contacto.objects.all()
    proyectos = Proyecto.objects.all()
    textos = Nosotros.objects.all()
    for texto in textos:
        if (texto.seccion == "Misión"):
            mision = texto
        elif (texto.seccion == "Visión"):
            vision = texto
        else:
            mision = ''
            vision = ''
    return render(request, "main/nosotros.html", {'proyectos': proyectos, 'mision': mision, 'vision': vision, 'infoContacto': infoContacto})

def contact(request):
    infoContacto = Contacto.objects.all()
    proyectos = Proyecto.objects.all()
    return render(request, "main/contact.html", {'proyectos': proyectos, 'infoContacto': infoContacto})

def proyecto(request, id):
    infoContacto = Contacto.objects.all()
    proyectos = Proyecto.objects.all()
    proyecto = get_object_or_404(Proyecto, id=id)
    return render(request, "main/proyecto.html", {'proyecto':proyecto, 'proyectos': proyectos, 'infoContacto': infoContacto})
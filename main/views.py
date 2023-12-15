from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Proyecto, ProyectoDestacado

# Create your views here.

def home(request):
    proyectos = Proyecto.objects.all()
    proyectosDestacados = ProyectoDestacado.objects.all().order_by('nombre')
    return render(request, "main/home.html", {'proyectosDestacados': proyectosDestacados, 'proyectos': proyectos})

def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, "main/proyectos.html", {'proyectos': proyectos})

def nosotros(request):
    proyectos = Proyecto.objects.all()
    return render(request, "main/nosotros.html", {'proyectos': proyectos})

def contact(request):
    proyectos = Proyecto.objects.all()
    return render(request, "main/contact.html", {'proyectos': proyectos})

def proyecto(request, id):
    proyectos = Proyecto.objects.all()
    proyecto = get_object_or_404(Proyecto, id=id)
    return render(request, "main/proyecto.html", {'proyecto':proyecto, 'proyectos': proyectos})
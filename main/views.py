from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Proyecto, ProyectoDestacado

# Create your views here.
def home(request):
    proyectos = ProyectoDestacado.objects.all()
    return render(request, "main/home.html", {'proyectos': proyectos})

def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, "main/proyectos.html", {'proyectos': proyectos})

def nosotros(request):
    return render(request, "main/nosotros.html")

def contact(request):
    return render(request, "main/contact.html")

def proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    return render(request, "main/proyecto.html", {'proyecto':proyecto})
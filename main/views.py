from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"main/home.html")

def proyectos(request):
    return render(request, "main/proyectos.html")

def nosotros(request):
    return render(request, "main/nosotros.html")

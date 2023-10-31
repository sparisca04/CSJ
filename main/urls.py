from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('proyectos/', views.proyectos),
    path('nosotros/', views.nosotros),
    path('contact/', views.contact),
    path('proyecto/', views.proyecto)
]

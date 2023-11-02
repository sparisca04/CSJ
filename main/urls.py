from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contact/', views.contact, name='contactanos'),
    path('proyecto/<int:id>/', views.proyecto, name='proyecto')
]

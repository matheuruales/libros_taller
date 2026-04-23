from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.ListaAutoresView.as_view(), name='lista_autores'),
    path('autores/crear/', views.CrearAutorView.as_view(), name='crear_autor'),
    path('libros/', views.ListaLibrosView.as_view(), name='lista_libros'),
    path('libros/crear/', views.CrearLibroView.as_view(), name='crear_libro'),
]

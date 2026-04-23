from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.ListaAutoresView.as_view(), name='lista_autores'),
    path('autores/crear/', views.CrearAutorView.as_view(), name='crear_autor'),
    path('autores/<int:pk>/actualizar/', views.actualizar_autor, name='actualizar_autor'),
    path('autores/<int:pk>/actualizar-generic/', views.ActualizarAutorView.as_view(), name='actualizar_autor_generic'),
    path('libros/', views.ListaLibrosView.as_view(), name='lista_libros'),
    path('libros/crear/', views.CrearLibroView.as_view(), name='crear_libro'),
    path('libros/<int:pk>/actualizar/', views.actualizar_libro, name='actualizar_libro'),
    path('libros/<int:pk>/actualizar-generic/', views.ActualizarLibroView.as_view(), name='actualizar_libro_generic'),
]

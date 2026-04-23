from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Autor, Libro
from .forms import AutorForm, LibroForm


class ListaAutoresView(ListView):
    model = Autor
    template_name = 'gestion/lista_autores.html'
    context_object_name = 'autores'


class CrearAutorView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_form.html'
    success_url = reverse_lazy('lista_autores')


class ListaLibrosView(ListView):
    model = Libro
    template_name = 'gestion/lista_libros.html'
    context_object_name = 'libros'


class CrearLibroView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_form.html'
    success_url = reverse_lazy('lista_libros')

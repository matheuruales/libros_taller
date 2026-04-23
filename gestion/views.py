from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
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


def actualizar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'gestion/actualizar_libro.html', {'form': form, 'libro': libro})


class ActualizarLibroView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/actualizar_libro_generic.html'
    success_url = reverse_lazy('lista_libros')

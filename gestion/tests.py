from django.test import TestCase
from django.urls import reverse

from .models import Autor, Libro


class EliminarAutorViewTests(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(
            nombre='Gabriel Garcia Marquez',
            correo='gabo@example.com',
            nacionalidad='Colombiana',
            fecha_nacimiento='1927-03-06',
            biografia='Autor de Cien anos de soledad.',
        )
        self.libro = Libro.objects.create(
            titulo='Cien anos de soledad',
            fecha_publicacion='1967-05-30',
            genero='Realismo magico',
            isbn='9780307474728',
            autor=self.autor,
        )

    def test_eliminar_autor_function_view_elimina_autor_y_libros_relacionados(self):
        response = self.client.post(reverse('eliminar_autor', args=[self.autor.pk]))

        self.assertRedirects(response, reverse('lista_autores'))
        self.assertFalse(Autor.objects.filter(pk=self.autor.pk).exists())
        self.assertFalse(Libro.objects.filter(pk=self.libro.pk).exists())

    def test_eliminar_autor_generic_view_elimina_autor(self):
        response = self.client.post(reverse('eliminar_autor_generic', args=[self.autor.pk]))

        self.assertRedirects(response, reverse('lista_autores'))
        self.assertFalse(Autor.objects.filter(pk=self.autor.pk).exists())


class EliminarLibroViewTests(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(
            nombre='Jorge Luis Borges',
            correo='borges@example.com',
            nacionalidad='Argentina',
            fecha_nacimiento='1899-08-24',
            biografia='Autor de Ficciones.',
        )
        self.libro = Libro.objects.create(
            titulo='Ficciones',
            fecha_publicacion='1944-01-01',
            genero='Cuento',
            isbn='9788420633124',
            autor=self.autor,
        )

    def test_eliminar_libro_function_view_elimina_libro(self):
        response = self.client.post(reverse('eliminar_libro', args=[self.libro.pk]))

        self.assertRedirects(response, reverse('lista_libros'))
        self.assertFalse(Libro.objects.filter(pk=self.libro.pk).exists())
        self.assertTrue(Autor.objects.filter(pk=self.autor.pk).exists())

    def test_eliminar_libro_generic_view_elimina_libro(self):
        response = self.client.post(reverse('eliminar_libro_generic', args=[self.libro.pk]))

        self.assertRedirects(response, reverse('lista_libros'))
        self.assertFalse(Libro.objects.filter(pk=self.libro.pk).exists())

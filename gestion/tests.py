from django.test import TestCase
from django.urls import reverse

from .models import Autor, Libro


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

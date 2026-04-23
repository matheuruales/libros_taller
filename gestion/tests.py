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

from django.db import models

# Create your models here.
from applications.autor.models import Autor
from .managers import LibroManager


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(
        max_length=50
    )
    fecha = models.DateField('Fecha de lanzamineto')
    portada = models.ImageField(upload_to='portada')
    visitas = models.PositiveIntegerField()
    objects = LibroManager()

    def __str__(self):
        return self.titulo
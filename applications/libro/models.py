from django.db import models

# Create your models here.
from applications.autor.models import Autor


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

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

    def __str__(self):
        return self.titulo
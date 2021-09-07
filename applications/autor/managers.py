from django.db import models

from django.db.models import Q

class AutorManager(models.Manager):
    """ managers para el modelo autor """
    def listar_autores(self):
        return self.all()

    def listar_50years(self):
        return self.filter(edad=50)

    def buscar_autor(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
        )
        return resultado

    def buscar_autor2(self, kword):
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        )
        return resultado

    def buscar_autor3(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
        ).exclude(edad__exact=50)
        return resultado
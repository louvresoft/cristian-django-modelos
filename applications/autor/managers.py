from django.db import models

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
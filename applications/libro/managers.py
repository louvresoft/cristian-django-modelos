import datetime

from django.db import models

from django.db.models import Q

class LibroManager(models.Manager):
    """ managers para el modelo libro """

    def buscar_libro(self, kword):
        # mayor que 50
        resultado = self.filter(
            titulo__icontains=kword
        )
        print("resultado =>", resultado)
        return resultado

    def buscar_libro2(self, kword, fecha1, fecha2):

        # convertir fechas proporcionadas por navegador a django
        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2)
        )
        return resultado
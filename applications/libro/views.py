from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.


#models local
from .models import Libro

class ListLibros(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        f1 = self.request.GET.get("fecha1", '')
        f2 = self.request.GET.get("fecha2", '')
        print("se ejecita aqui")
        if f1 and f2:
            return Libro.objects.buscar_libro2(palabra_clave, f1, f2)
        else:
            print("palabra clave", palabra_clave)
            a = Libro.objects.buscar_libro(palabra_clave)
            print("a", a)
            return a


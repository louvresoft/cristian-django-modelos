from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.


#models local
from .models import Autor

class ListAutores(ListView):
    context_object_name = 'lista_autores'
    template_name = 'autor/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        return Autor.objects.buscar_autor(palabra_clave)

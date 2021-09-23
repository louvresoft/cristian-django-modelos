from django.contrib import admin
from .models import Libro, Categoria
# Register your models here.

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass
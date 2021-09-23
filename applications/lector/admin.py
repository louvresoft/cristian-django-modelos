from django.contrib import admin
from .models import Lector, Prestamo
# Register your models here.

@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    pass

class Prestamo(admin.ModelAdmin):
    pass

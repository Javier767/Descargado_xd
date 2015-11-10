from django.contrib import admin
from .models import Cliente

# Register your models here.

@admin.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('dni', 'nombre','apellidos', 'distrito', 'provincia', 'departamento', 'direccion', 'telefono'  )
	search_fields = ('dni', 'nombre')
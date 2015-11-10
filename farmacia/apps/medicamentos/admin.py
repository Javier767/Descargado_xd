from django.contrib import admin
from apps.medicamentos.models import Categoria, Medicamentos


# Register your models here.
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre',  )

@admin.register(Medicamentos)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'categoria','nombre','descripcion', 'fecha_expiracion', 'fecha_produccion', 'tipo', 'precio_Compra','precio_venta', 'stock')
	search_fields = ('nombre', 'descripcion')

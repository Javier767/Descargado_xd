from django.db import models
from django.db.models import signals
from apps.clientes.models import Cliente

# Create your models here.
class Categoria(models.Model):
	#codigo = models.CharField(max_length=10, unique=True)	
	nombre = models.CharField(max_length=60)

	def __unicode__(self):
		return u'%s' % (self.nombre)

class Medicamentos(models.Model):
	TIPO = (
        ('generico', 'Generico'),
        ('comercial', 'Comercial'),
    )
	codigo = models.CharField(max_length=10, unique=True)
	categoria = models.ForeignKey(Categoria)	
	tipo = models.CharField(choices=TIPO, max_length=30)
	nombre = models.CharField(max_length=200, unique=True)
	componente = models.CharField(max_length=200)
	concentracion = models.CharField(max_length=50)
	sanitario = models.CharField(max_length=200)
	fecha_expiracion = models.DateField()
	fecha_produccion = models.DateField()
	descripcion = models.TextField(max_length=400)		
	precio_Compra = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	precio_venta = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	stock = models.PositiveSmallIntegerField()

	def __unicode__(self):
		return self.nombre

	def preeciototal(self):
		precio_total=self.precio_compra*self.stock		
		return precio_total

from django.db import models
from apps.medicamentos.models import Medicamentos
from apps.clientes.models import Cliente
from django.db.models import signals

class Ticket(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True)    
    medicamento = models.ManyToManyField(Medicamentos, through='Detalle_Tickets')
    fecha = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.codigo


class Detalle_Tickets(models.Model):
    ticket=models.ForeignKey(Ticket)
    medicamento=models.ForeignKey(Medicamentos)
    cantidad=models.IntegerField(max_length=9)

    def precioventa(self):
        return (self.medicamento.precio_venta)

    def total_venta(self):
        total=(self.medicamento.precio_venta*self.cantidad)            
        return total  

    def totalt(self):
        detalles = Detalle_Tickets.objects.filter(medicamento=self.pk)
        total = 1
        for detalle in detalles:
            suma = self.medicamento.precio_venta * self.cantidad
            total = total + suma
            return total

    def __unicode__(self):
        return self.medicamento.nombre


def update_stock(sender, instance, **kwargs):
    instance.medicamento.stock -= instance.cantidad
    instance.medicamento.save()

# register the signal
signals.post_save.connect(update_stock, sender=Detalle_Tickets, dispatch_uid="update_stock_count")
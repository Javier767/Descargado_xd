# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Medicamentos
from .forms import MedicamentoForm, CrearmedicamentoForm
from django.http import HttpResponse
import csv

class ListaMedicamentos(ListView):
	context_object_name = 'medicamentos'
	model = Medicamentos
	template_name = 'medicamentos/lista_medicamentos.html'
	paginate_by = 10

	def get_queryset(self):
		queryset = super(ListaMedicamentos, self).get_queryset()
		# búsqueda
		q = self.request.GET.get('q', '')
		if q:
			queryset = queryset.filter(
				Q(nombre__icontains=q) |
				Q(descripcion__icontains=q)

				)
		return queryset


class DetalleView(DetailView):
	model = Medicamentos
	template_name = 'medicamentos/detalle_medicamentos.html'


class ActualizarView(UpdateView):
	form_class = MedicamentoForm
	template_name = 'medicamentos/editar_medicamentos.html'
	model = Medicamentos
	success_url='/medicamentos'


class CreateMedicamentos(CreateView):
	form_class = CrearmedicamentoForm
	template_name = 'medicamentos/create_medicamentos.html'
	model = Medicamentos
	success_url = '/medicamentos'


class EliminarView(DeleteView):
	model = Medicamentos
	success_url='/medicamentos'
	template_name = 'medicamentos/eliminar_medicamento.html'




def CargaAtenciones_ant(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="atenciones.csv"'
	registrants= Medicamentos.objects.all()
	writer = csv.writer(response,delimiter="|")
	writer.writerow(['id','codigo','categoria','tipo','nombre','componente','concentracion','sanitario','fecha_expiracion','fecha_produccion','descripcion','precio_Compra','precio_venta','stock'])
	for registrant in registrants:
		writer.writerow([registrant.id, 
                            registrant.codigo, 
                            registrant.categoria,
                            registrant.tipo,
                            registrant.nombre.encode('utf-8'),
                            registrant.componente.encode('utf-8'),
                            registrant.concentracion.encode('utf-8'),
                            registrant.sanitario,
                            registrant.fecha_expiracion,
                            registrant.fecha_produccion,
                            registrant.descripcion.encode('utf-8'),
                            registrant.precio_Compra,
                            registrant.precio_venta,
                            registrant.stock
                            ])
	return response
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response 
from django.shortcuts import render_to_response as render
from django.template import RequestContext as ctx
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext # For CSRF
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect

#reporte pdf
from django.http import HttpResponseRedirect
from datetime import *
import xhtml2pdf.pisa as pisa
from django import http
from django.template.loader import get_template
from django.template import Context
import cStringIO as StringIO
import cgi

from .forms import TodoListForm, TodoItemForm, RangoForm
from .models import Cabecera
from django.views.generic import ListView

def realizar_compra(request):
    # This class is used to make empty formset forms required
    # See http://stackoverflow.com/questions/2406537/django-formsets-make-first-required/4951032#4951032
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

    TodoItemFormSet = formset_factory(TodoItemForm, max_num=10, formset=RequiredFormSet)

    if request.method == 'POST': # If the form has been submitted...
        todo_list_form = TodoListForm(request.POST) # A form bound to the POST data
        # Create a formset from the submitted data
        todo_item_formset = TodoItemFormSet(request.POST, request.FILES)        
        if todo_list_form.is_valid() and todo_item_formset.is_valid():
            todo_list = todo_list_form.save()
            for form in todo_item_formset.forms:
                todo_item = form.save(commit=False)
                todo_item.list = todo_list
                todo_item.save()
            return HttpResponseRedirect('confirmacion_compra') # Redirect to a 'success' page
    else:
        todo_list_form = TodoListForm()
        todo_item_formset = TodoItemFormSet()
    
    # For CSRF protection
    # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/ 
    c = {'todo_list_form': todo_list_form,
         'todo_item_formset': todo_item_formset,
        }
    c.update(csrf(request))
    return render_to_response('compras/realizar_compra.html', c)


class ListaCompras(ListView):
    context_object_name = 'compras'
    model = Cabecera
    template_name = 'compras/lista_compras.html'
    paginate_by = 6

 #   def get_queryset(self):
  #      queryset = super(ListaCliente, self).get_queryset()
  #      return queryset.filter(author_id=self.kwargs['author_id'])

    def get_queryset(self):
        queryset = super(ListaCompras, self).get_queryset()
        # búsqueda
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(
                Q(distribuidor__icontains=q) |
                Q(codigo__icontains=q)
                )
        return queryset


def reportecompras(request, pk):
    compra = Cabecera.objects.get(pk=pk)
    medicamentos = compra.cabecera.all()

    total = 0
    for expe in medicamentos:
        total = (expe.cantidad * expe.medicamento.precio_Compra) + total

    return render('compras/reportecompras.html', locals(), context_instance=ctx(request))



def write_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), \
            content_type='application/pdf')
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))


def generar_pdf(request):
    if request.method == "POST":
        formbusqueda = RangoForm(request.POST)
        if formbusqueda.is_valid():
            fecha_in = formbusqueda.cleaned_data['fecha_i']
            fecha_fi = formbusqueda.cleaned_data['fecha_f']
            rango = Cabecera.objects.filter(fecha__range=(fecha_in, fecha_fi)).order_by('distribuidor')
            return write_pdf ('compras/pdf.html',{'pagesize' : 'legal', 'rango' : rango})
            #return render_to_response ('empleados/test.html',{'rango':rango},context_instance=RequestContext(request))
        else:
            error = "Hay un error en las fechas proporcionadas"
            return render_to_response('compras/reporte_pdf.html', {'error': error}, context_instance=RequestContext(request))

    return render_to_response('compras/reporte_pdf.html', {'rangoform': RangoForm()}, context_instance=RequestContext(request))
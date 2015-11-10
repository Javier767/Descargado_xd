from django.conf.urls import patterns, url, include
from .views import ListaCliente
from django.conf.urls import *
from .views import index, imprimirCompras
from django.views.generic import TemplateView

urlpatterns = patterns('',
#urlpatterns = patterns('dynamicform.todo.views',
    url(r'^compras/$', index, name="compras"),   
    url(r'thanks$', TemplateView.as_view(template_name="compras/thanks.html")),
    url(r'^imprimir/(?P<pk>\d+)/$', 'apps.compras.views.imprimirCompras', name='imprimir'),
    url(r'^lista_compras/$', ListaCliente.as_view(), name = 'lista_compras'),
)

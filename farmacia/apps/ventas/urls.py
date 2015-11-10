from django.conf.urls import patterns, url
from .views import List_ticket, Detail_Tickets


urlpatterns = patterns('',
	url(r'^ventas1', List_ticket.as_view(), name='ventas'),
	url(r'^realizar_venta','apps.ventas.views.realizar_Ticket', name = 'realizar_venta'),
	url(r'^venta/detalle_venta/(?P<pk>\d+)/$', Detail_Tickets.as_view(), name='detalle_venta'),
	   )

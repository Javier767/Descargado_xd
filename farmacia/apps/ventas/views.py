from django.shortcuts import render, redirect
from .forms import AgregarVentaForm
from .models import Ticket, Detalle_Tickets
from django.views.generic import  TemplateView, DetailView, ListView
from django.contrib.auth.decorators import permission_required
from django.db.models import Sum
from braces.views import LoginRequiredMixin

class List_ticket(ListView):
    context_object_name = 'ticket'
    template_name ='venta/list_tickets.html'
    model = Detalle_Tickets

    def get_context_data(self, **kwargs):
        context = super(List_ticket,self).get_context_data(**kwargs)
        context['ticket'] = Ticket.objects.all()
        return context

class Detail_Tickets(LoginRequiredMixin, ListView):
    login_url='/'
    template_name ='venta/detalle_venta.html'
    model = Detalle_Tickets

    def get_context_data(self, **kwargs):
        context = super(Detail_Tickets,self).get_context_data(**kwargs)        
        context['detalle'] = Detalle_Tickets.objects.filter(ticket=self.kwargs['pk'])
        return context




def realizar_Ticket(request):
	if request.method == "POST":
		modelform = AgregarTicketForm(request.POST)
		if modelform.is_valid():
			modelform.save()
			return redirect("/realizar_ventas/")
	else:
		modelform = AgregarTicketForm()
	return render(request, "ventas/realizar_Tventas.html", {"form": modelform})

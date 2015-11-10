from django.contrib import admin

from apps.ventas.models import Detalle_Tickets, Ticket


class Detalle_TicketsInline(admin.TabularInline):
    model = Detalle_Tickets

class TicketAdmin(admin.ModelAdmin):
    inlines = (Detalle_TicketsInline,)
    #search_fields = ('fecha', '')


admin.site.register(Ticket, TicketAdmin)	
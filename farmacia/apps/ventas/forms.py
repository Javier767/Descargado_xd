from django import forms
from apps.ventas.models import Ticket


class AgregarVentaForm(forms.ModelForm):
	class Meta:
		model = Ticket




#campo = forms.ModelMultipleChoiceField(queryset=Tabla.objects.all(), 

#widget=forms.CheckboxSelectMultiple())
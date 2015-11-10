from .models import * # Change as necessary
from django.forms import ModelForm
from django import forms

class TodoListForm(ModelForm):
  class Meta:
    model = Cabecera

class TodoItemForm(forms.ModelForm):
	class Meta:
		model = DetalleCompra
		exclude = ('list',)
		widgets = {
				'medicamento': forms.Select(attrs={'class': 'form-control'}),
				'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
				
			}
	
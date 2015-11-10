#encoding:utf-8
from django import forms
from .models import Medicamentos


class MedicamentoForm(forms.ModelForm):
	class Meta:
		model = Medicamentos
		exclude = ('codigo',)

		widgets = {			
			'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '6' }),
			'precio_Compra': forms.NumberInput(attrs={'class': 'form-control'}),
			'precio_venta': forms.NumberInput(attrs={'class': 'form-control'}),
			'categoria': forms.Select(attrs={'class': 'form-control'}),
			'tipo': forms.Select(attrs={'class': 'form-control'}),
			}

class CrearmedicamentoForm(forms.ModelForm):
	class Meta:
		model = Medicamentos	
		widgets = {
				'codigo': forms.TextInput(attrs={'class': 'form-control'}),
				'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '6' }),
				'precio_Compra': forms.NumberInput(attrs={'class': 'form-control'}),
				'precio_venta': forms.NumberInput(attrs={'class': 'form-control'}),
				'categoria': forms.Select(attrs={'class': 'form-control'}),
				'tipo': forms.Select(attrs={'class': 'form-control'}),
				'fecha_expiracion': forms.DateInput(attrs={'class':'datepicker'}),
				'fecha_produccion': forms.DateInput(attrs={'class':'datepicker'}),
			}
	
#encoding:utf-8
from django import forms
from apps.clientes.models import Cliente

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente

	dni = forms.CharField(widget=forms.NumberInput(attrs={
		'placeholder': 'DNI',
		'size': '8'}))
	nombre = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Nombre Cliente',
		'size': '40'}))	
	apellidos = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Apellidos',
		'size': '40'}))	
	distrito = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Distrito',
		'size': '40'}))	
	provincia = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'provincia',
		'size': '40'}))	
	departamento = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'departamento',
		'size': '40'}))	
	direccion = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Direccion',
		'size': '40'}))	
	telefono = forms.CharField(widget=forms.NumberInput(attrs={
		'placeholder': 'Telefono',
		'size': '8'}))

	def clean_dni(self):
		diccionario_limpio = self.cleaned_data
		dni = diccionario_limpio.get('dni')
		if len(dni) < 8 or len(dni) > 8:
			raise forms.ValidationError("debe ser de 8 Digitos")
		return dni

	def clean_nombre(self):
		nombre = self.cleaned_data['nombre']
		if not nombre.isalpha():
			raise forms.ValidationError('No puede contener números')
		return nombre
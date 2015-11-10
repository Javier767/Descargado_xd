 # -*- coding: utf-8 -*- 
from django.db import models
from django.conf import settings

class Cliente(models.Model):
	dni = models.IntegerField(unique=True)	
	nombre = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=100)	
	distrito = models.CharField(max_length=40)
	provincia = models.CharField(max_length=40)
	departamento = models.CharField(max_length=40)
	direccion = models.CharField(max_length=100)
	telefono = models.IntegerField(verbose_name='Telefono')
	user = models.ForeignKey(settings.AUTH_USER_MODEL)

	def __unicode__(self):
		return self.nombre
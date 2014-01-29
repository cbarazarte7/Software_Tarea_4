from django.db import models

class espacio(models.Model):
	nombre = models.CharField(max_length=140)
	ubicacion = models.CharField(max_length=140)
	capacidad = models.IntegerField()
	
	def __unicode__(self):
		return self.nombre

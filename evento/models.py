from django.db import models
from espacio.models import espacio

class evento(models.Model):
	nombre = models.CharField(max_length=140)
	duracion = models.IntegerField()
	hora_inicio = models.TimeField()
	fecha = models.DateField()
	tipo = models.CharField(max_length=100)
	lugar = models.ForeignKey(espacio)
	
	def __unicode__(self):
		return self.nombre



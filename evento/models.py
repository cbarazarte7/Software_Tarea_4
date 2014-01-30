from django.db import models
from espacio.models import espacio

class evento(models.Model):
	nombre = models.CharField(max_length=140)
	duracion = models.TimeField()
	fecha_inicio = models.DateField()
	lugar = models.ForeignKey(espacio)
	
	def __unicode__(self):
		return self.nombre

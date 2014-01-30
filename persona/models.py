from django.db import models

class persona(models.Model):
	nombre = models.CharField(max_length=60)
	apellido = models.CharField(max_length=60)
	email = models.EmailField()
	pais = models.CharField(max_length=60)
	institucion = models.CharField(max_length=140)
	url = models.URLField()
	telefono = models.IntegerField()
	
	def __unicode__(self):
		return self.nombre

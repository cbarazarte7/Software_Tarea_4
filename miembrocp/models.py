from django.db import models

class miembrocp(models.Model):
	nombre = models.CharField(max_length=60)
	apellido = models.CharField(max_length=60)
	email = models.EmailField()
	pais = models.CharField(max_length=60)
	institucion = models.CharField(max_length=140, null=True)
	url = models.URLField(null=True)
	telefono = models.CharField(max_length=140, null=True)
	esPresidente = models.NullBooleanField()
	
	def __unicode__(self):
		return self.nombre

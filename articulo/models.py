from django.db import models

class articulo(models.Model):
	titulo = models.CharField(max_length=140)
	autor = models.CharField(max_length=60)
	pais = models.CharField(max_length=140)
	texto = models.CharField(max_length=140)
	puntuacion = models.IntegerField(default=0)
	puntajes = models.IntegerField(default=0)
	num_eval = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.titulo

from django.db import models
from autor.models import autor

class articulo(models.Model):
	titulo = models.CharField(max_length=140)
	autor = models.ForeignKey(autor)
	#autor = models.CharField(max_length=140)
	texto = models.CharField(max_length=140)
	puntuacion = models.IntegerField(default=0)
	puntajes = models.IntegerField(default=0)
	num_eval = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.titulo

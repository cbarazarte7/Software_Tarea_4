from django.db import models
from autor.models import autor
from django.core.validators import MaxValueValidator, MinValueValidator

class articulo(models.Model):
	titulo = models.CharField(max_length=140)
	autor = models.ForeignKey(autor)
	texto = models.CharField(max_length=140,null=True)
	puntuacion = models.FloatField(default=0.0,validators=[MaxValueValidator(5.0), MinValueValidator(0.0)])
	puntajes = models.FloatField(default=0.0)
	num_eval = models.FloatField(default=0.0)
	
	def __unicode__(self):
		return self.titulo

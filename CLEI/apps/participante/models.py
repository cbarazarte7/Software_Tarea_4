from datetime import datetime
from django.db import models

class Participante(models.Model):
	name = models.CharField(max_length=100)
	id_document = models.CharField(max_length=10)

class Inscripcion(models.Model):
	created = models.DateTimeField(default=datetime.now)
	participante = models.ForeignKey(Participante, related_name="inscripciones")

#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.db import models
from django.core.exceptions import ValidationError

from models import autor, articulo

# Formulario para crear:
class articuloForm(forms.Form):
	titulo = forms.CharField(widget=forms.TextInput())
	autor = forms.ModelChoiceField(queryset=autor.objects.all())
	texto = forms.CharField(widget=forms.TextInput(),required=False)	
	
# Formulario para evaluar:
class evaluateForm(forms.Form):
	def validar_puntaje(value):
		if value > 5.0 or value < 1.0:
			raise ValidationError("La puntuacion debe estar entre 1 y 5")

	articulo = forms.ModelChoiceField(queryset=articulo.objects.all())
	puntuacion = forms.FloatField(widget=forms.NumberInput(), validators=[validar_puntaje])

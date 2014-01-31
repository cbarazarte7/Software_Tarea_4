#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.db import models

from models import autor, articulo

# Formulario para crear:
class articuloForm(forms.Form):
	titulo = forms.CharField(widget=forms.TextInput())
	autor = forms.ModelChoiceField(queryset=autor.objects.all())
	texto = forms.CharField(widget=forms.TextInput(),required=False)	
	
# Formulario para evaluar:
class evaluateForm(forms.Form):
	articulo = forms.ModelChoiceField(queryset=articulo.objects.all())
	puntuacion = forms.FloatField(widget=forms.NumberInput(),min_value=1.0,max_value=5.0,help_text='Recuerde: Debe estar entre 1.0 y 5.0')
	
# Formulario para aceptar (por nota):
class acceptForm(forms.Form):
	nota = forms.FloatField(widget=forms.NumberInput(),min_value=1.0,max_value=5.0,help_text='Recuerde: Debe estar entre 1.0 y 5.0')

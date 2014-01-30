#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.db import models
from models import autor
from models import articulo

# Formulario para crear:
class articuloForm(forms.Form):
	titulo = forms.CharField(widget=forms.TextInput())
	autor = forms.ModelChoiceField(queryset=autor.objects.all())
	texto = forms.CharField(widget=forms.TextInput(),required=False)	
	
# Formulario para evaluar:
class evaluateForm(forms.Form):
	articulo = forms.ModelChoiceField(queryset=articulo.objects.all())
	puntuacion = forms.FloatField(widget=forms.NumberInput())

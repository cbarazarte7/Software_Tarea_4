#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.db import models
from models import autor

class articuloForm(forms.Form):
	titulo = forms.CharField(widget=forms.TextInput())
	autor = forms.ModelChoiceField(queryset=autor.objects.all())
	texto = forms.CharField(widget=forms.TextInput())	
	puntuacion = forms.IntegerField(widget=forms.NumberInput())
	puntajes = forms.IntegerField(widget=forms.NumberInput())
	num_eval = forms.IntegerField(widget=forms.NumberInput())

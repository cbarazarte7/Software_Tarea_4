#encoding:utf-8
from django.forms import ModelForm
from django import forms
from evento.models import evento
from django.forms.extras.widgets import SelectDateWidget
from django.db import models


class articuloForm(forms.Form):
	titulo = forms.CharField(widget=forms.TextInput())
	autor = forms.CharField(widget=forms.TextInput())
	texto = forms.CharField(widget=forms.TextInput())	
	puntuacion = forms.IntegerField(widget=forms.NumberInput())
	puntajes = forms.IntegerField(widget=forms.NumberInput())
	num_eval = forms.IntegerField(widget=forms.NumberInput())

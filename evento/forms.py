#encoding:utf-8
from django.forms import ModelForm
from django import forms
from evento.models import evento

class eventoForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput())
	duracion = forms.TimeField(widget=forms.TextInput())
	fecha_inicio = forms.DateField(widget=forms.TextInput())	
	lugar = forms.CharField(widget=forms.TextInput())
#encoding:utf-8
from django.forms import ModelForm
from django import forms
from evento.models import evento
from django.forms.extras.widgets import SelectDateWidget
from models import espacio
from django.db import models


class eventoForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput())
	duracion = forms.TimeField(widget=forms.TextInput())
	fecha_inicio = forms.DateField(widget=forms.TextInput())	
	lugar = forms.ModelChoiceField(queryset=espacio.objects.all())
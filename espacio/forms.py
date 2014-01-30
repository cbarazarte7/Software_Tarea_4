#encoding:utf-8
from django.forms import ModelForm
from django import forms
from models import espacio

# Formulario para crear:
class espacioForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput())
	ubicacion = forms.CharField(widget=forms.TextInput())
	capacidad = forms.IntegerField(widget=forms.TextInput())

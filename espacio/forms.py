#encoding:utf-8
from django.forms import ModelForm
from django import forms
from models import espacio

class espacioForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput())
	ubicacion = forms.CharField(widget=forms.TextInput())
	capacidad = forms.IntegerField(widget=forms.TextInput())
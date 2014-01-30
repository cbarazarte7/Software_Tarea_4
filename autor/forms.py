#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.db import models


class autorForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput())
	apellido = forms.CharField(widget=forms.TextInput())
	email = forms.EmailField(widget=forms.EmailInput())	
	pais = forms.CharField(widget=forms.TextInput())
	institucion = forms.CharField(widget=forms.TextInput())
	url = forms.URLField(widget=forms.URLInput())
	telefono = forms.CharField(widget=forms.TextInput())

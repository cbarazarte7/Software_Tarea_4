from django.shortcuts import render, render_to_response
from models import espacio
from forms import espacioForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse



def nuevo_espacio(request):
	if request.method=='POST':
		formulario = espacioForm(request.POST, request.FILES)
		if formulario.is_valid():
			e = espacio()
			e.nombre = formulario.cleaned_data['nombre']
			e.ubicacion = formulario.cleaned_data['ubicacion']			
			e.capacidad = formulario.cleaned_data['capacidad']			
			e.save()
			return HttpResponseRedirect('/espacio/create')
	else:
		formulario = espacioForm()
	return render_to_response('espacioform.html', {'formulario':formulario}, context_instance=RequestContext(request))


# Create your views here.

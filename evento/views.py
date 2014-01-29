from django.shortcuts import render, render_to_response
from models import evento
from forms import eventoForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse



def nuevo_evento(request):
	if request.method=='POST':
		formulario = eventoForm(request.POST, request.FILES)
		if formulario.is_valid():
			e = evento()
			e.nombre = formulario.cleaned_data['nombre']
			e.duracion = formulario.cleaned_data['duracion']			
			e.fecha_inicio = formulario.cleaned_data['fecha_inicio']
			e.lugar = formulario.cleaned_data['lugar']			
			e.save()
			return HttpResponseRedirect('/evento/create')
	else:
		formulario = eventoForm()
	return render_to_response('eventoform.html', {'formulario':formulario}, context_instance=RequestContext(request))


from django.shortcuts import render, render_to_response, get_object_or_404
from models import espacio
from forms import espacioForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

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

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def results(request):
    objectlist = espacio.objects.all()
    context = RequestContext(request,{'objectlist':objectlist,})
    return render(request, 'espacio/results.html', context)

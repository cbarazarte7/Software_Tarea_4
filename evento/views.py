from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from models import evento
from forms import eventoForm

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")


def results(request):
    objectlist = evento.objects.all()
    context = RequestContext(request,{'objectlist':objectlist,})
    return render(request, 'evento/results.html', context)
    

def nuevo_evento(request):
	if request.method=='POST':
		formulario = eventoForm(request.POST, request.FILES)

		if formulario.is_valid():
			e = evento()
			e.nombre = formulario.cleaned_data['nombre']
			e.duracion = formulario.data['duracion']
			e.hora_inicio = formulario.data['hora_inicio']			
			e.fecha = formulario.cleaned_data['fecha']
			e.tipo = formulario.cleaned_data['tipo']
			e.lugar_id = formulario.data['lugar']
			e.save()
			return HttpResponseRedirect('/evento/results')
	else:
		formulario = eventoForm()
	return render_to_response('eventoform.html', {'formulario':formulario}, context_instance=RequestContext(request))

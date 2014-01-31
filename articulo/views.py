from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext
from django import forms
from django.forms.util import ErrorList

from articulo.models import articulo
from forms import articuloForm, evaluateForm

def index(request):
    return HttpResponse("Seccion de articulos del CLEI.")


def results(request):
    objectlist = articulo.objects.all()
    context = RequestContext(request,{'objectlist':objectlist,})
    return render(request, 'articulo/results.html', context)


def evaluate(request):
	if request.method=='POST':
		formulario = evaluateForm(request.POST, request.FILES)

		if formulario.is_valid():
			a = formulario.cleaned_data['articulo']		  
			a.puntajes += float(formulario.data['puntuacion'])
			a.num_eval += float(1)
			a.puntuacion = float(a.puntajes/a.num_eval)

			a.save()
			return HttpResponseRedirect('/articulo/results')
	else:
		formulario = evaluateForm()
	return render_to_response('evaluateform.html', {'formulario':formulario}, context_instance=RequestContext(request))
def nuevo_articulo(request):
	if request.method=='POST':
		formulario = articuloForm(request.POST, request.FILES)

		if formulario.is_valid():
			a = articulo()
			a.titulo = formulario.cleaned_data['titulo']
			a.autor = formulario.cleaned_data['autor']			
			a.texto = formulario.cleaned_data['texto']
			a.save()
			return HttpResponseRedirect('/articulo/evaluate')
	else:
		formulario = articuloForm()
	return render_to_response('articuloform.html', {'formulario':formulario}, context_instance=RequestContext(request))

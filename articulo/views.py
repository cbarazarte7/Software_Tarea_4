from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext

from articulo.models import articulo
from forms import articuloForm, evaluateForm, acceptForm

def index(request):
    return render_to_response('articulo.html', context_instance=RequestContext(request))


def results(request):
    objectlist = articulo.objects.all()
    context = RequestContext(request,{'objectlist':objectlist,})
#    return render(request, 'articulo/results.html', context)
    return render_to_response('articulo/results.html', context_instance=context)
    
    
def show_accepted(request):
    objectlist = articulo.objects.filter(estado='aceptado')
    context = RequestContext(request,{'objectlist':objectlist,})
    return render(request, 'articulo/accepted.html', context)


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
			return HttpResponseRedirect('/articulo/results')
	else:
		formulario = articuloForm()
	return render_to_response('articuloform.html', {'formulario':formulario}, context_instance=RequestContext(request))
	
def accept(request):
	if request.method=='POST':
		formulario = acceptForm(request.POST, request.FILES)

		if formulario.is_valid():
			nota = float(formulario.data['nota'])
			objectlist = articulo.objects.all()
			for a in objectlist:
					if a.puntuacion >= nota and a.es_aceptable:
						a.estado = 'aceptado'
					else:
						a.estado = 'rechazado'
					a.save()
			
			return HttpResponseRedirect('/articulo/accepted')
	else:
		formulario = acceptForm()
	return render_to_response('acceptform.html', {'formulario':formulario}, context_instance=RequestContext(request))

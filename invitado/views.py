from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext

from invitado.models import invitado
from forms import invitadoForm

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")


def results(request):
    objectlist = invitado.objects.all()
    context = RequestContext(request,{'objectlist':objectlist,})
    return render(request, 'invitado/results.html', context)

        
def nuevo_invitado(request):
	if request.method=='POST':
		formulario = invitadoForm(request.POST, request.FILES)

		if formulario.is_valid():
			e = invitado()
			e.nombre = formulario.data['nombre']
			e.apellido = formulario.data['apellido']			
			e.email = formulario.data['email']
			e.pais = formulario.data['pais']
			e.institucion = formulario.data['institucion']
			e.url = formulario.data['url']
			e.telefono = formulario.data['telefono']
			e.save()
			return HttpResponseRedirect('/invitado/create')
	else:
		formulario = invitadoForm()
	return render_to_response('invitadoform.html', {'formulario':formulario}, context_instance=RequestContext(request))

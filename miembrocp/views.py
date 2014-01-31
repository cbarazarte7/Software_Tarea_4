from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext

from miembrocp.models import miembrocp
from forms import miembrocpForm

def index(request):
    return HttpResponse("Seccion de miembros de comite de programa.")


def results(request):
    objectlist = miembrocp.objects.all()
    context = RequestContext(request,{'objectlist':objectlist,})
    return render(request, 'miembrocp/results.html', context)

        
def nuevo_miembrocp(request):
	if request.method=='POST':
		formulario = miembrocpForm(request.POST, request.FILES)

		if formulario.is_valid():
			e = miembrocp()
			e.nombre = formulario.data['nombre']
			e.apellido = formulario.data['apellido']			
			e.email = formulario.data['email']
			e.pais = formulario.data['pais']
			e.institucion = formulario.data['institucion']
			e.url = formulario.data['url']
			e.telefono = formulario.data['telefono']
			e.esPresidente = formulario.data['esPresidente']
			e.save()
			return HttpResponseRedirect('/miembrocp/create')
	else:
		formulario = miembrocpForm()
	return render_to_response('miembrocpform.html', {'formulario':formulario}, context_instance=RequestContext(request))

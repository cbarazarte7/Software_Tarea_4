from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from miembro_cp.models import miembro_cp

from django.contrib.auth.models import User
from django.template import RequestContext
from forms import autorForm

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def results(request):
    objectlist = miembro_cp.objects.all()
    context = RequestContext(request,{'objectlist':objectlist,})
    return render(request, 'miembro_cp/results.html', context)
        
def nuevo_miembro_cp(request):
	if request.method=='POST':
		formulario = autorForm(request.POST, request.FILES)

		if formulario.is_valid():
			e = miembro_cp()
			e.nombre = formulario.data['nombre']
			e.apellido = formulario.data['apellido']			
			e.email = formulario.data['email']
			e.pais = formulario.data['pais']
			e.institucion = formulario.data['institucion']
			e.url = formulario.data['url']
			e.telefono = formulario.data['telefono']
			e.esPresidente = formulario.data['esPresidente']
			e.save()
			return HttpResponseRedirect('/miembro_cp/create')
	else:
		formulario = miembro_cpForm()
	return render_to_response('miembro_cpform.html', {'formulario':formulario}, context_instance=RequestContext(request))


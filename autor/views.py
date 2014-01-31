from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext

from autor.models import autor
from forms import autorForm

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")


def results(request):
    objectlist = autor.objects.all()
    context = RequestContext(request,{'objectlist':objectlist,})
    return render(request, 'autor/results.html', context)

        
def nuevo_autor(request):
	if request.method=='POST':
		formulario = autorForm(request.POST, request.FILES)

		if formulario.is_valid():
			e = autor()
			e.nombre = formulario.data['nombre']
			e.apellido = formulario.data['apellido']			
			e.email = formulario.data['email']
			e.pais = formulario.data['pais']
			e.institucion = formulario.data['institucion']
			e.url = formulario.data['url']
			e.telefono = formulario.data['telefono']
			e.save()
			return HttpResponseRedirect('/autor/results')
	else:
		formulario = autorForm()
	return render_to_response('autorform.html', {'formulario':formulario}, context_instance=RequestContext(request))

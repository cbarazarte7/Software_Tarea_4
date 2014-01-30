from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from articulo.models import articulo

from django.contrib.auth.models import User
from django.template import RequestContext
from forms import articuloForm

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def results(request):
    objectlist = articulo.objects.all()
    context = RequestContext(request,{'objectlist':objectlist,})
    return render(request, 'articulo/results.html', context)

def evaluate(request, articulo_id):
    a = get_object_or_404(articulo, pk=articulo_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        
def nuevo_articulo(request):
	if request.method=='POST':
		formulario = articuloForm(request.POST, request.FILES)

		if formulario.is_valid():
			e = articulo()
			e.titulo = formulario.cleaned_data['titulo']
			e.autor = formulario.data['autor']			
			e.texto = formulario.cleaned_data['texto']
			e.puntuacion = formulario.data['puntuacion']
			e.puntajes = formulario.data['puntajes']
			e.num_eval = formulario.data['num_eval']
			e.save()
			return HttpResponseRedirect('/articulo/create')
	else:
		formulario = articuloForm()
	return render_to_response('articuloform.html', {'formulario':formulario}, context_instance=RequestContext(request))


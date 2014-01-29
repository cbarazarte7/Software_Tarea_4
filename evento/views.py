from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from evento.models import evento

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def results(request, evento_id):
    e = get_object_or_404(evento, pk=evento_id)
    return render(request, 'evento/results.html', {'evento': e})

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from espacio.models import espacio

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def results(request, espacio_id):
    e = get_object_or_404(espacio, pk=espacio_id)
    return render(request, 'espacio/results.html', {'espacio': e})

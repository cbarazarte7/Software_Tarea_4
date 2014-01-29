from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

from evento.models import evento

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def results(request):
    objectlist = evento.objects.all()
    context = RequestContext(request,{'objectlist':objectlist,})
    return render(request, 'evento/results.html', context)

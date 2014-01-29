from django.conf.urls import patterns, url
from views import nuevo_espacio
from espacio import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
    url(r'results/$', views.results, name='results'),
    url(r'create/$', nuevo_espacio, name='create'),
)

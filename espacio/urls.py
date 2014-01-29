from django.conf.urls import patterns, url

from espacio import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
    url(r'^(?P<espacio_id>\d+)/results/$', views.results, name='results'),
)

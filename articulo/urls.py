from django.conf.urls import patterns, url

from articulo import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
    url(r'^(?P<articulo_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<articulo_id>\d+)/evaluate/$', views.evaluate, name='evaluate'),
)

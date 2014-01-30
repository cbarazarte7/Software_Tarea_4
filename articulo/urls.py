from django.conf.urls import patterns, url

from articulo import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'create/$', views.nuevo_articulo, name='create'),
    url(r'results/$', views.results, name='results'),
    url(r'evaluate/$', views.evaluate, name='evaluate'),
)

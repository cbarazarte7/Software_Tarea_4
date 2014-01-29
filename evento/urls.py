from django.conf.urls import patterns, url
from views import nuevo_evento
from articulo import views


urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),

    	url(r'create/$', nuevo_evento)
#    url(r'^(?P<articulo_id>\d+)/evaluate/$', views.evaluate, name='evaluate'),
)

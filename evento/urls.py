from django.conf.urls import patterns, url

from evento import views
from views import nuevo_evento

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'results/$', views.results, name='results'),
    	url(r'create/$', nuevo_evento)
)

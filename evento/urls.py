from django.conf.urls import patterns, url

from evento import views
from views import nuevo_evento, coincidente_soc

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
		url(r'results/$', views.results, name='results'),
		url(r'create/$', nuevo_evento),
		url(r'coincidente_soc/$', coincidente_soc),
)

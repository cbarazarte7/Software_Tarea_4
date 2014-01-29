from django.conf.urls import patterns, url

from evento import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<evento_id>\d+)/results/$', views.results, name='results'),
)

from django.conf.urls import patterns, url

from evento import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'results/$', views.results, name='results'),
)

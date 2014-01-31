from django.conf.urls import patterns, url

from miembrocp import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'create/$', views.nuevo_miembrocp, name='create'),
    url(r'results/$', views.results, name='results'),
)

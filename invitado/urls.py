from django.conf.urls import patterns, url

from invitado import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'create/$', views.nuevo_invitado, name='create'),
    url(r'results/$', views.results, name='results'),
)

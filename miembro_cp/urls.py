from django.conf.urls import patterns, url

from autor import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
    url(r'results/$', views.results, name='results'),
    url(r'create/$', views.nuevo_miembro_cp)
)

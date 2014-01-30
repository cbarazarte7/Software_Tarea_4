from django.conf.urls import patterns, include, url

from django.contrib import admin

import articulo
import espacio
import evento
import persona
import autor
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CLEI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'CLEI.views.login_user'),
    url(r'^home/', 'CLEI.views.home', name='home'),
    
    url(r'^articulo/', include('articulo.urls')),

    url(r'^espacio/', include('espacio.urls')),
    url(r'^evento/', include('evento.urls')),    
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/articulo/(?P<articulo_id>\d+)/results', articulo.views.results, name='resultsart'),
    url(r'^espacio/', include('espacio.urls')),
    url(r'^admin/espacio/(?P<espacio_id>\d+)/results', espacio.views.results, name='resultsesp'),
    url(r'^evento/', include('evento.urls')),
    url(r'^admin/evento/(?P<evento_id>\d+)/results', evento.views.results, name='resultseven'),
    url(r'^autor/', include('autor.urls')),
    url(r'^admin/autor/(?P<autor_id>\d+)/results',autor.views.results, name='resultsaut'),
)

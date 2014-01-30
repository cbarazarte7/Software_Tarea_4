from django.conf.urls import patterns, include, url
from django.contrib import admin

import articulo
import autor
import espacio
import evento
import miembrocp
import invitado

admin.autodiscover()

urlpatterns = patterns('',
    # CLEI:
    url(r'^$', 'CLEI.views.login_user'),
    #url(r'^home/', 'CLEI.views.home', name='home'),
    
    # Articulo:
    url(r'^articulo/', include('articulo.urls')),
    
    # Autor:
    url(r'^autor/', include('autor.urls')),

		# Espacio:
    url(r'^espacio/', include('espacio.urls')),

		# Evento:
    url(r'^evento/', include('evento.urls')),    
    #Miembro CP
    url(r'^miembrocp/', include('miembrocp.urls')),
    #Invitado
    url(r'^invitado/', include('invitado.urls')),
    
    # Admin:
    #url(r'^autor/', include('autor.urls')),
    #url(r'^admin/articulo/(?P<articulo_id>\d+)/results', articulo.views.results, name='resultsart'),
    #url(r'^admin/espacio/(?P<espacio_id>\d+)/results', espacio.views.results, name='resultsesp'),
    #url(r'^admin/evento/(?P<evento_id>\d+)/results', evento.views.results, name='resultseven'),
    #url(r'^admin/autor/(?P<autor_id>\d+)/results',autor.views.results, name='resultsaut'),
)

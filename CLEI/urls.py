from django.conf.urls import patterns, include, url

from django.contrib import admin

import articulo
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CLEI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'CLEI.views.login_user'),
    url(r'^home/', 'CLEI.views.home', name='home'),
    
    url(r'^articulo/', include('articulo.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/(?P<articulo_id>\d+)/results', articulo.views.results, name='results'),
)

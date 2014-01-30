from django.contrib import admin
from miembrocp.models import miembrocp

class miembrocpAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['nombre']}),
  	(None, {'fields': ['apellido']}),
  	(None, {'fields': ['email']}),
  	(None, {'fields': ['pais']}),
  	(None, {'fields': ['institucion']}),
  	(None, {'fields': ['url']}),
  	(None, {'fields': ['telefono']}),
  	(None, {'fields': ['esPresidente']}),
  ]

admin.site.register(miembrocp, miembrocpAdmin)

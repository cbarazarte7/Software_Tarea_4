from django.contrib import admin
from invitado.models import invitado

class invitadoAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['nombre']}),
  	(None, {'fields': ['apellido']}),
  	(None, {'fields': ['email']}),
  	(None, {'fields': ['pais']}),
  	(None, {'fields': ['institucion']}),
  	(None, {'fields': ['url']}),
  	(None, {'fields': ['telefono']}),
  ]

admin.site.register(invitado, invitadoAdmin)

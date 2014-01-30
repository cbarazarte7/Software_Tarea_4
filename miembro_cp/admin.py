from django.contrib import admin
from miembro_cp.models import miembro_cp

class miembro_cpAdmin(admin.ModelAdmin):
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

admin.site.register(miembro_cp, miembro_cpAdmin)

from django.contrib import admin
from autor.models import autor

class autorAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['nombre']}),
  	(None, {'fields': ['apellido']}),
  	(None, {'fields': ['email']}),
  	(None, {'fields': ['pais']}),
  	(None, {'fields': ['institucion']}),
  	(None, {'fields': ['url']}),
  	(None, {'fields': ['telefono']}),
  ]

admin.site.register(autor, autorAdmin)

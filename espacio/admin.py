from django.contrib import admin
from espacio.models import espacio

class espacioAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['nombre']}),
  	(None, {'fields': ['ubicacion']}),
		(None, {'fields': ['capacidad']}),
  ]

admin.site.register(espacio, espacioAdmin)

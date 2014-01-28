from django.contrib import admin
from articulo.models import articulo

class articuloAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['titulo']}),
  	(None, {'fields': ['autor']}),
  	(None, {'fields': ['pais']}),
		('Informacion adicional', {'fields': ['texto'], 'classes': ['collapse']}),
  ]

admin.site.register(articulo, articuloAdmin)

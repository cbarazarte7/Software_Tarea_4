from django.contrib import admin
from evento.models import evento

class eventoAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['nombre']}),
  	(None, {'fields': ['duracion']}),
		(None, {'fields': ['fecha_inicio']}),
		(None, {'fields': ['lugar']}),
  ]

admin.site.register(evento, eventoAdmin)

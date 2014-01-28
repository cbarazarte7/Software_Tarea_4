from datetime import datetime

from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .forms import ParticipanteForm
from .models import Participante

class CreateParticipanteView(CreateView):
	model = Participante
	form_class = ParticipanteForm
	template_name = "participante/create_participante.html"

	def get_context_data(self, *args, **kwargs):
		context = super(CreateParticipanteView, self).get_context_data(*args, **kwargs)

		context.update({
			'hola': 'como estas?'
			})

		return context

	def get_success_url(self):
		return reverse('ver_participante',args=[self.object.id])

class VerParticipanteView(DetailView):
	model = Participante
	template_name = "participante/ver_participante.html"
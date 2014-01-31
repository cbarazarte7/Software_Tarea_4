from django.shortcuts import render, render_to_response, get_object_or_404
from models import evento
from forms import eventoForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import datetime

 
# Calcula la hora de finalizacion de un evento sumando la duracion a la hora de inicio    
  
def sumar_minutos(ev):
	
	##d = datetime.datetime.strptime(ev.duracion, '%H:%M')

	return ev.hora_inicio + datetime.timedelta(minutes=int(ev.duracion))  

# A partir de las horas de inicio y duracion de dos eventos, determina si coinciden
    
def coincidir(evento1, evento2):
	hora_inicio_e1 = evento1.hora_inicio
	hora_fin_e1 = evento1.hora_fin
	hora_inicio_e2 = evento2.hora_inicio
	hora_fin_e2 = evento2.hora_fin
 	return not( ( (hora_inicio_e1<hora_inicio_e2) and (hora_fin_e1<hora_inicio_e2 )) or ( (hora_inicio_e1>hora_fin_e2) and (hora_fin_e2>hora_fin_e1) ) )
  
# Determina si dos eventos coinciden en hora y lugar  
  
def coincidir_lugar(ev):    
	f = ev.fecha
	lista = evento.objects.filter(fecha=f)    
   	for i in lista:
		if i.tipo != 'Social' and i.lugar == evento.lugar:
			if coincidir(ev,i):
	  			return True
	return False

# Determina si un evento coincide con otro social 
 
def coincidir_social(ev):
  	f = ev.fecha
	lista = evento.objects.filter(fecha=f)     
  	for i in lista:
		if i.tipo == 'Social':
			if coincidir(ev,i):
				return True
  	return False
    
# Determina si un evento coincide con otro no social    
    
def coincidir_no_social(ev):
	f = ev.fecha
	lista = evento.objects.filter(fecha=f) 
	for i in lista:
		if i.tipo != 'Social':
			if coincidir(ev,i):
				return True
	return False
    
# Determina el evento no social con el que coincide un evento    
    
def encontrar_coincidente_no_soc(ev):
    f = ev.fecha
    lista = evento.objects.filter(fecha=f)
    for i in lista:
    	if i.tipo != 'Social':
			if coincidir(ev,i):
		  		return i    

# Determina el evento social con el que coincide un evento

def encontrar_coincidente_soc(ev):
	f = ev.fecha
	lista = evento.objects.filter(fecha=f)    
	for i in lista:
		if i.get_tipo() == 'Social':
			if coincidir(ev,i):
				return i       

def eliminar_coincidentes(ev):
	f = ev.fecha
	lista = evento.objects.filter(fecha=f)
	for i in lista:
		if coincidir(ev,i):
			i.delete()



def programar_evento(evento):
	# Caso evento social
    if evento.tipo == 'Social':
      # Si no coincide con otro evento social, se agrega al programa
    	if not coincidir_social(evento):
			
			# Se eliminan del programa los eventos no sociales con que coincida
			eliminar_coincidentes(evento)
			evento.save()
      		# Si coincide con otro evento social, se consulta cual agregar o eliminar
     	else:
     		coincidente_soc(evento)
			#coincidente = encontrar_coincidente_soc(evento)
			#context = RequestContext(request,{'coincidente':coincidente,'evento':evento,})
			#return render(request, 'evento/coincidente_soc.html', context)

			# print 
			# print "El evento coincide con "+coincidente.get_nombre()
			# print "Desea agregar "+evento.get_nombre()+"? S/N"
			# opcion = raw_input (">> ")
			# print
			# if opcion == "S":
  	#   			self.seleccionar_dia(evento).remove(coincidente)
  	#   			self.seleccionar_dia(evento).append(evento)
    # Caso evento no social
    else:
      # Se agrega el evento si no coincide con otro no social en lugar o con alguno social
    	if not (coincidir_social(evento) or coincidir_lugar(evento)):
			evento.save()


def nuevo_evento(request):
	if request.method=='POST':
		formulario = eventoForm(request.POST, request.FILES)

		if formulario.is_valid():
			e = evento()
			e.nombre = formulario.cleaned_data['nombre']
			e.duracion = formulario.cleaned_data['duracion']
			e.hora_inicio = formulario.cleaned_data['hora_inicio']	
			e.hora_fin = formulario.cleaned_data['hora_fin']		
			e.fecha = formulario.cleaned_data['fecha']
			e.tipo = formulario.cleaned_data['tipo']
			e.lugar_id = formulario.data['lugar']
			programar_evento(e)
			return HttpResponseRedirect('/evento/results')
	else:
		formulario = eventoForm()
	return render_to_response('eventoform.html', {'formulario':formulario}, context_instance=RequestContext(request))

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def coincidente_soc(ev):
	coincidente = encontrar_coincidente_soc(ev)
	context = RequestContext(request,{'coincidente':coincidente,'evento':ev,})
	return render(request, 'evento/coincidente_soc.html', context)

def results(request):
    objectlist = evento.objects.all()
    context = RequestContext(request,{'objectlist':objectlist,})
    return render(request, 'evento/results.html', context)

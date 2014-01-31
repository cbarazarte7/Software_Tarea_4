#! /usr/bin/python

# ------------------------------------------------------------
# Ingenieria de Software
# Tarea 3

# Programacion.py
# Clase que representa una programacion.
#
# Autores: 
#	   Carla Barazarte, 08-10096.
#	   Alejandro Garbi, 08-10398.
# 	   Michelle Fernandez, 09-10279.
#	   Jose Figueredo, 10-10245.
#	   Alejandro Guillen, 10-10333.
#	   Donato Rolo, 10-10640.
# ------------------------------------------------------------

from ctypes import *
import os

from Evento import *
import datetime

class Programacion:
  def __init__(self):
    self.dia1 = []
    self.dia2 = []
    self.dia3 = []
    self.dia4 = []
    self.dia5 = []
    self.eventos = []

# Getters y setters de la clase

  def get_dia1(self):
    return self.dia1
  
  def set_dia1(self, dia1):
    self.dia1 = dia1
    
  def get_dia2(self):
    return self.dia2
  
  def set_dia2(self, dia2):
    self.dia2 = dia2    
    
  def get_dia3(self):
    return self.dia3
  
  def set_dia3(self, dia3):
    self.dia3 = dia3    
    
  def get_dia4(self):
    return self.dia4
  
  def set_dia4(self, dia4):
    self.dia4 = dia4
    
  def get_dia5(self):
    return self.dia5
  
  def set_dia5(self, dia5):
    self.dia5 = dia5    
    
  def get_eventos(self):
    return self.eventos
  
  def set_eventos(self, eventos):
    self.eventos = eventos
    
# Calcula la hora de finalizacion de un evento sumando la duracion a la hora de inicio    
  
  def sumar_minutos(self, evento):
    hora_inicio = datetime.datetime.strptime(evento.get_hora_inicio(), '%H:%M')
    duracion = evento.get_duracion()
    return hora_inicio + datetime.timedelta(minutes = int(duracion))    

# A partir de las horas de inicio y duracion de dos eventos, determina si coinciden
    
  def coincidir(self, evento1, evento2):
    hora_inicio_e1 = datetime.datetime.strptime(evento1.get_hora_inicio(), '%H:%M')
    hora_fin_e1 = self.sumar_minutos(evento1)
    hora_inicio_e2 = datetime.datetime.strptime(evento2.get_hora_inicio(), '%H:%M')
    hora_fin_e2 = self.sumar_minutos(evento2)
    return not( ( (hora_inicio_e1<hora_inicio_e2) and (hora_fin_e1<hora_inicio_e2 )) or ( (hora_inicio_e1>hora_fin_e2) and (hora_fin_e2>hora_fin_e1) ) )
  
# Determina si dos eventos coinciden en hora y lugar  
  
  def coincidir_lugar(self, evento):    
   lista = self.seleccionar_dia(evento)    
   for i in lista:
      if i.get_tipo() != 'Social' and i.get_lugar() == evento.get_lugar():
	if self.coincidir(evento,i):
	  return True
   return False

# Retorna la lista correspondiente al dia del evento
   
  def seleccionar_dia(self, evento):
    if evento.get_fecha() == 'dia1':
      return self.dia1
    elif evento.get_fecha() == 'dia2':
      return self.dia2
    elif evento.get_fecha() == 'dia3':
      return self.dia3
    elif evento.get_fecha() == 'dia4':
      return self.dia4
    elif evento.get_fecha() == 'dia5':
      return self.dia5
 
# Determina si un evento coincide con otro social 
 
  def coincidir_social(self, evento):
    lista = self.seleccionar_dia(evento)    
    for i in lista:
      if i.get_tipo() == 'Social':
	if self.coincidir(evento,i):
	  return True
    return False
    
# Determina si un evento coincide con otro no social    
    
  def coincidir_no_social(self, evento):
    lista = self.seleccionar_dia(evento)    
    for i in lista:
      if i.get_tipo() != 'Social':
	       if self.coincidir(evento,i):
	         return True
    return False
    
# Determina el evento no social con el que coincide un evento    
    
  def encontrar_coincidente_no_soc(self, evento):
    lista = self.seleccionar_dia(evento)    
    for i in lista:
      if i.get_tipo() != 'Social':
	if self.coincidir(evento,i):
	  return i    

# Determina el evento social con el que coincide un evento

  def encontrar_coincidente_soc(self, evento):
    lista = self.seleccionar_dia(evento)    
    for i in lista:
      if i.get_tipo() == 'Social':
	if self.coincidir(evento,i):
	  return i    
	
# Agrega un evento al programa de CLEI

  def programar_evento(self, evento):
    # Caso evento social
    if evento.get_tipo() == 'Social':
      # Si no coincide con otro evento social, se agrega al programa
      if not self.coincidir_social(evento):
	self.seleccionar_dia(evento).append(evento)
	# Se eliminan del programa los eventos no sociales con que coincida
	while self.coincidir_no_social(evento):
	  self.seleccionar_dia(evento).remove(self.encontrar_coincidente_no_soc(evento))
      # Si coincide con otro evento social, se consulta cual agregar o eliminar
      else:
	coincidente = self.encontrar_coincidente_soc(evento)
	print 
	print "El evento coincide con "+coincidente.get_nombre()
	print "Desea agregar "+evento.get_nombre()+"? S/N"
	opcion = raw_input (">> ")
	print
	if opcion == "S":
  	  self.seleccionar_dia(evento).remove(coincidente)
  	  self.seleccionar_dia(evento).append(evento)
    # Caso evento no social
    else:
      # Se agrega el evento si no coincide con otro no social en lugar o con alguno social
      if not (self.coincidir_social(evento) or self.coincidir_lugar(evento)):
	self.seleccionar_dia(evento).append(evento)

# Genera la programacion de todos los eventos
	
  def generar_programacion(self):
    for i in self.eventos:
      self.programar_evento(i)
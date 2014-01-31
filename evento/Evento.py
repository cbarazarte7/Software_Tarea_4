#! /usr/bin/python

# ------------------------------------------------------------
# Ingenieria de Software
# Tarea 3

# Evento.py
# Clase que representa un evento.
#
# Autores: 
#	   Carla Barazarte, 08-10096.
#	   Alejandro Garbi, 08-10398.
# 	   Michelle Fernandez, 09-10279.
#	   Jose Figueredo, 10-10245.
#	   Alejandro Guillen, 10-10333.
#	   Donato Rolo, 10-10640.
# ------------------------------------------------------------
from Conferencia import *
#self.moderador = None
  
def get_id(self):
  return self.id
  
def set_id(self, id):
  self.id = id
  
def get_nombre(self):
  return self.nombre
  
def set_nombre(self, nombre):
  self.nombre = nombre
    
def get_tipo(self):
  return self.tipo
  
def set_tipo(self, tipo):
  self.tipo = tipo
  
def get_duracion(self):
  return self.duracion
    
def set_duracion(self, duracion):
  self.duracion = duracion
    
def get_fecha(self):
  return self.fecha
    
def set_fecha(self,fecha):
  self.fecha = fecha
    
def get_hora_inicio(self):
  return self.hora_inicio
    
def set_hora_inicio(self,hora_inicio):
  self.hora_inicio = hora_inicio
    
def get_lugar(self):
  return self.lugar
    
def set_lugar(self,lugar,lista_espacios):
  while not self.existe_lugar(lugar, lista_espacios):
    print "Ingrese un id de lugar valido:"
    lugar = raw_input(">> ")
  self.lugar = lugar

  # def get_moderador(self):
  #   return self.moderador

  # def set_moderador(self, moderador):
  #   self.moderador = moderador

  # def asignar_moderador(self, conf):
  #   print
  #   print("MODERADOR")
  #   print("---------")
  #   print
    
  #   cp = conf.get_cp()
  #   miembros = cp.get_miembros()
  #   usuario = None

  #   while (self.moderador == None):
  #     correo = raw_input("correo: ")

  #     # Revisar si el usuario ya existe chequeando por correo.
  #     x = 0
  #     while (x < len(miembros)) and (usuario == None):
  #       if miembros[x].get_correo() == correo:
  #         usuario = miembros[x]
  #       x += 1
      
  #     if usuario == None:
  #       print
  #       print("----------------------------------------------")
  #       print("No existe ningun Miembro CP asociado al correo")
  #       print
  #       print(" \"" + correo + "\".")
  #       print("----------------------------------------------")
  #       print

  #     else:
  #       self.moderador = miembros[x]
	
def existe_lugar(self, lugar, lista_espacios):
  for k in lista_espacios:
    if k.get_id()==lugar:
      return True
  return False
    
def to_string(self):
  print
  print("Id: " + self.id)
  print("Nombre: " + self.nombre)
  print("Duracion: " + self.duracion)
  print("Fecha: " + self.fecha)
  print("Hora de Inicio: " + self.hora_inicio)
  print("Lugar: " + self.lugar)
  if (self.tipo in ["charla", "ponencia"]):
    print("Moderador: " + self.moderador)
  print

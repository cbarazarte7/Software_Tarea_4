#! /usr/bin/python

# ------------------------------------------------------------
# Ingenieria de Software
# Tarea 3

# Conferencia.py
# Clase que representa una conferencia.
#
# Autores: Michelle Fernandez, 09-10279.
#	   Donato Rolo, 10-10640.
#	   Carla Barazarte, 08-10096
#	   Alejandro Garbi, 08-10398
#	   Jose Figueredo, 10-10245
#	   Alejandro Guillen, 10-10333
# ------------------------------------------------------------
class Conferencia:
    def __init__(self):
      self.nombre = None
      self.siglas = None
      self.topicos = []
      self.max_articulos = None
      
      self.articulos = []
      self.aceptables = []
      self.aceptados = []
      self.empatados = []      
      self.rechazados = []
      
      self.pres_articulos = False
      self.cp = None
      self.inscritos = []
      self.espacios = []
      self.eventos = []
      
    def get_nombre(self):
      return self.nombre
      
    def set_nombre(self, nombre):
      self.nombre = nombre
      
    def get_siglas(self):
      return self.siglas
      
    def set_siglas(self, siglas):
      self.siglas = siglas
    
    def set_pres_articulos(self, pres_articulos):
      self.pres_articulos = pres_articulos
      
    def get_pres_articulos(self):
      return self.pres_articulos
    
    def get_cp(self):
      return self.cp
    
    def set_topicos(self, topicos):
      self.topicos = topicos
      
    def get_topicos(self):
      return self.topicos
    
    def get_max_articulos(self):
      return self.max_articulos
      
    def set_max_articulos(self, max_articulos):
      self.max_articulos = max_articulos
  
    def get_articulos(self):
      return self.articulos
  
    def set_articulos(self, articulos):
      self.articulos = articulos
   
    def get_aceptados(self):
      return self.aceptados
  
    def set_aceptados(self, articulos):
      self.aceptados = articulos
      
    def get_empatados(self):
      return self.empatados
  
    def set_empatados(self, empatados):
      self.empatados = empatados   
      
    def get_aceptables(self):
      return self.aceptables
  
    def set_aceptables(self, aceptables):
      self.aceptables = aceptables

    def get_rechazados(self):
      return self.rechazados

    def set_rechazados(self, rechazados):
      self.rechazados = rechazados
      
    def get_articulo(self, num):
      return self.articulos[num]

    def get_inscritos(self):
      return self.inscritos
      
    def get_eventos(self):
      return self.eventos
      
    def agregar_evento(self,evento):
      self.eventos.append(evento)

    def get_espacios(self):
      return self.espacios

    def agregar_espacio(self, espacio):
      self.espacios.append(espacio)

    def encontrar_articulo(self, articulo):
      articulos = self.articulos
      
      x = 0
      while (x < len(articulos)) and not (articulos[x].get_titulo() == articulo.get_titulo()):
	x += 1
	
      if (x == len(articulos)):
	return False
	
      return True

    ##
    # agregar_articulo
    # Agrega un articulo a una lista dada.
    #
    # Entrada: Lista, Articulo.
    ##
    def agregar_articulo(self, lista, articulo):
      lista.append(articulo)
       

    def evaluar(self, titulo, puntos):
      articulos = self.get_articulos()
      x = -1
      fin = False
      
      while (x < len(articulos)) and not fin:
	x += 1
	fin = (articulos[x].get_titulo() == titulo)      

      num_evaluaciones = self.articulos[x].get_num_evaluaciones()
      num_evaluadores = self.articulos[x].get_num_evaluadores()

      self.articulos[x].agregar_puntuacion(puntos)
      self.articulos[x].set_num_evaluaciones(num_evaluaciones + 1)
      self.articulos[x].promediar()

    def evaluar_promedio(self, titulo):
      recibidos = self.articulos
      x = -1
      fin = False

      while (x < len(recibidos)) and not fin:
        x += 1
        fin = (recibidos[x].get_titulo() == titulo)
 
      articulo = recibidos[x]
      num_evaluadores = articulo.get_num_evaluadores()
      num_evaluaciones = articulo.get_num_evaluaciones()
      promedio = articulo.get_promedio()
      max_articulos = self.max_articulos
 
      if num_evaluaciones == num_evaluadores:
        if not (promedio <= 2):
          self.agregar_articulo(self.aceptables, articulo)
          #self.agregar_articulo(self.aceptables, self.get_articulo(x))

        # Rechazar articulo por promedio.
        else:
          articulo.set_estado_final(4)
          self.agregar_articulo(self.rechazados, articulo)
          #self.agregar_articulo(self.rechazados, self.get_articulo(x))

    def calcular_aceptados(self):
      art_aceptables = self.aceptables
      max_articulos = self.max_articulos

      print len(art_aceptables) 
      print (max_articulos)
      
      if (len(art_aceptables) > max_articulos):
	promedio_min = art_aceptables[max_articulos - 1].get_promedio()
        print "promedio_min: "
        print promedio_min
      
	if (art_aceptables[max_articulos].get_promedio() == promedio_min): 
          print "hay empatados"
	  x = max_articulos - 2
	  while (x >= 0) and (art_aceptables[x].get_promedio() == promedio_min):
	    x -= 1
	    
	  y = x + 1
	  while (y < len(art_aceptables)) and (art_aceptables[y].get_promedio() == promedio_min):
	    y += 1
	    
	  for i in range(x + 1):
            # Aceptado.
            art_aceptables[i].set_estado_final(1)
	    self.aceptados.append(art_aceptables[i])
	    
	  for i in range(x + 1, y):
	    self.empatados.append(art_aceptables[i])
	    
	else:
	  for x in range(len(art_aceptables)):
            if (x < max_articulos):
              # Aceptado.
              art_aceptables[x].set_estado_final(1)
              self.aceptados.append(art_aceptables[x])
            else:
              # Rechazado por falta de cupo.
              art_aceptables[x].set_estado_final(3)
              self.rechazados.append(art_aceptables[x])
          
	  
      # Si la cantidad de articulos aceptables es menor a la cantidad de 
      # articulos que se aceptaran en la conferencia, se agrega a la lista
      # de aceptados toda la lista de aceptables.
      else:
	for x in range(len(art_aceptables)):
          art_aceptables[x].set_estado_final(1)
	  self.aceptados.append(art_aceptables[x])
	    

    def armar_listas(self):
      recibidos = self.articulos
      print "len recibidos: "
      print len(recibidos)
      if (not self.pres_articulos):
        for x in range(len(recibidos)):
          self.evaluar_promedio(recibidos[x].get_titulo())

        # Armar lista de aceptados y empatados
        self.calcular_aceptados()
	
    def llamar_pres_articulos(self):
      self.set_pres_articulos(True)
      # Avisar a los inscritos.
      
    def fin_pres_articulos(self):
      self.set_pres_articulos(False)
      # Organizar listas de aceptados/empatados
    
    def agregar_inscrito(self, inscrito):
      self.inscritos.append(inscrito)
      
    def get_eventos(self):
      return self.eventos
      
    def agregar_evento(self,evento):
      self.eventos.append(evento)

    def get_espacios(self):
      return self.espacios

    def agregar_espacio(self, espacio):
      self.espacios.append(espacio)
    
    #def printTopicos(self):
      #topicos = self.topicos
      #for x in range(len(topicos)):
	#print '%s%d%s' % ("[", x, "] " + topicos[x])
	#print
    
    def to_string(self):
      print("CONFERENCIA")
      print("------------")
      print("Nombre: " + self.nombre)
      print("Siglas: " + self.siglas)
      print("Topicos: ")
      print(self.topicos)
      print("------------")      
      if not(self.cp == None):
	self.cp.to_string()

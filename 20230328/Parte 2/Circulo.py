#coding: utf-8

class Ponto():
	def __init__(self, x,y): #construtora
#definiir atributos
		self._x = x
		self._y = y
		self._dist_origem()
		print("Distância até origem ponto:", self._d)

	def _set_coordenadas(self, x ,y):
		self._x = x
		self._y = y
		
	def _get_coordenadas(self):
		return(self._x, self._y)

	def _dist_origem(self):
		d = pow(self._x,2) + self._y**2
		self._d = pow(d,0.5) #Calcula raiz quadrada

class Circulo(Ponto):
	def __init__(self, raio, x, y):
		self.x = x
		self.y = y
		self._raio = raio
		Ponto.__init__(self, self.x,self.y)
		print("Distância até a origem: ", self._d)

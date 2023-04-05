#coding: utf-8

class Ponto():
	def __init__(self,x,y): #construtora
		self._x = 0
		self._y = 0
		self._set_coordenadas(x, y)
		self._dist_origem()
		

	def _set_coordenadas(self, x ,y):
		self._x = x
		self._y = y
		

	def _get_coordenadas(self):
		return(self._x, self._y)

	def _dist_origem(self):
		d = pow(self._x,2) + self._y**2
		self._d = pow(d,0.5) #Calcula raiz quadrada

if __name__=="__main__":
	A = Ponto(3,4)
	#A._set_coordenadas(2,3)
	print(A._get_coordenadas())
	print("x = ",A._x, " y = ",A._y)
	print("Distância até origem: ",A._d)

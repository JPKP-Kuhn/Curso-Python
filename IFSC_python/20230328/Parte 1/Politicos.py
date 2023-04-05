#coding: utf-8

class Politico():
	def __init__(self):
		self._nome = ""
		self._partido = ""
		self._cargo = ""
	#Setters
	def _set_nome(self, nome):
		self._nome = nome

	def _set_partido(self, partido):
		self._partido = partido

	def _set_cargo(self, cargo):
		self._cargo = cargo

	#getters
	def _apresentacao(self):
		print("Olá, meu nome é: ", self._nome)
		print("Meu cargo é: ", self._cargo)
		print("Meu partido é: ", self._partido)

if __name__ == "__main__":
	Pol1 = Politico()
	Pol1._set_nome("Bob")
	Pol1._set_cargo("Prefeito")
	Pol1._set_partido("Partido da Fenda do Bikini")
	Pol1._apresentacao()

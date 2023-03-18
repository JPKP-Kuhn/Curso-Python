#coding: utf-8

class Pessoa():
	def __init__(self): 
		self._nome = ""
		self._idade = -1
		self._sexo = ""

	def _set_pessoa(self):
		self._nome = input("Nome: ") 
		self._idade = input("Idade: ")
		self._sexo = input("Sexo: ")
	
	def _get_pessoa(self): 
		print("Dados da pessoa: ") 
		print("Nome: ", self._nome)	
		print("Idade: ", self._idade)
		print("Sexo: ", self._sexo)	


if __name__=="__main__":
	A = Pessoa()
	A._set_pessoa()
	A._get_pessoa()				

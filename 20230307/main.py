#coding: utf-8

from ClassePessoa import*
#import ClassePessoa as pes

class Arquivo(): 
	def __init__(self):
		self.Pessoas = []
	
	def _set_dado_arquivo(self):
		A = Pessoa()
		print("Adicionar pessoa ao arquivo.") 
		Nome= input("\tEntre com o nome ")
		Idade = input("\tEntre com a idade ")
		Sexo = input("\tEntre com a o sexo ") 
		A._set_pessoa2(Nome, Idade, Sexo)
		self.Pessoas.append(A) 
			
		


if __name__=="__main__":
	Arq1 = Arquivo()
	for i in range(3):
		Arq1._set_dado_arquivo()			





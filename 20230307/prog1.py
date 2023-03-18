# coding:utf-8

class Pessoa_(): 
	_nome = ""
	_idade = -1
	_sexo = ""

def Cadastra_pessoa(): 
	print("Insira pessoa") 
	A = Pessoa_()
	A._nome = input("Nome: ")
	A._idade = input("Idade: ") # type: ignore
	A._sexo = input("Sexo: ")
	return A

def Mostra_pessoa(Pessoas): 
	for i in range(len(Pessoas)): 
		print("Pessoa ", i+1)
		print("\tNome: ", Pessoas[i]._nome)
		print("\tIdade: ", Pessoas[i]._idade)
		print("\tSexo: ", Pessoas[i]._sexo)

if __name__=="__main__": 
	Pessoas=[]	#Criei uma lista de pessoas. 
	for i in range(3): 
		Pessoas.append(Cadastra_pessoa())
	'''	  	
	P1 = Cadastra_pessoa()
	P2 = Cadastra_pessoa()
	P3 = Cadastra_pessoa()
	Pessoas.append(P1)
	Pessoas.append(P2)
	Pessoas.append(P3)
	'''
	Mostra_pessoa(Pessoas)


#coding: utf-8
#Funcionamento de uma Caixa acoplada de Vaso sanitário
#from CaixaAcoplada import *
import CaixaAcoplada as CA
import servico as SE

if __name__ == "__main__":

	Vaso = CA.CaixaAcoplada()
	Acao = SE.servico(Vaso)
	Vaso._encher()
	Acao._servico()

	continuar = input('Deseja continuar? S/n ').upper()
	while continuar == "S":
		Acao._servico()
		continuar = input('Deseja continuar? S/n ').upper()
	print("Número de vezes que a descarga foi usada: ", Vaso._alavanca._contador)

'''
    for i in range(3):
        print('Número de descargasa dadas: ', Vaso._alavanca._contador)
 '''
#coding: utf-8
#Funcionamento de uma Caixa acoplada de Vaso sanitário
#from CaixaAcoplada import *
import CaixaAcoplada as CA
import servico as SE

if __name__ == "__main__":
	Acao = SE.servico()
	Vaso = CA.CaixaAcoplada()
	Vaso._encher()
	Acao._servico()
	for i in range(3):
		Vaso._descarga()
	print("Número de vezes que a descarga foi usada: ", Vaso._alavanca._contador)

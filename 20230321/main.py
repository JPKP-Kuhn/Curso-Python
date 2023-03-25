#coding: utf-8

#from CaixaAcoplada import *
import CaixaAcoplada as CA

if __name__ == "__main__":
	Vaso = CA.CaixaAcoplada()
	Vaso._encher()
	for i in range(3):
		Vaso._descarga()
	print("Número de vezes que o vaso foi usado: ", Vaso._alavanca._contador)

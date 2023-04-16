#coding: utf-8

import ClasseCorrentista as CC
import time as t

if __name__=="__main__":
	Correntistas = []
	C1 = CC.Correntista("Jose Ivan", "11Abr23", 1000)
	Correntistas.append(C1)
	C2 = CC.Correntista("Lucas",  "11Abr23", 1000)
	Correntistas.append(C2)
	C3 = CC.Correntista("Joao",  "11Abr23", 1000)
	Correntistas.append(C3)

	Correntistas[1]._set_Deposito(500, tempo)
	t.sleep(0.2345)
	tempo = t.asctime(t.localtime(t.time()))
	
	Correntistas[1]._set_Retirada(200, tempo)
	Correntistas[1]._get_Operacoes()

	print("Dados dos correntistas")
	for i in range(len(Correntistas)):
		A = Correntistas[i]._get_dados_correntistas()
		print("\tData de abertura:", A)

'''
	print(C1._get_dados_correntista())
	print(C2._get_dados_correntista())
'''

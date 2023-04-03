#coding: utf-8
#from Politicos importPolitico
#from Politicos import*
import Politicos as P
import Governador as G

if __name__ == "__main__":
	'''
	Pol1 = P.Politico()
	Pol1._set_nome("Bob")
	Pol1._set_cargo("Prefeito")
	Pol1._set_partido("Partido da Fenda do Bikini")
	Pol1._apresentacao()
	'''
	Gov1 = G.Governador("Patrick", "Estrela do mar", "Vila da Fenda")
	Gov1._apresentacao()

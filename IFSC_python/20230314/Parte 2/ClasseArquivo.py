#coding: utf-8
import ClassePessoa as cp
'''
Métodos
função setter >> insere informações
função getter >> recebe informações
função operacional >> faz algo interno a classe
'''

class _Arquivo():
    def __init__(self): #função de construção, Self define a si mesmo
        self._pessoas = [] #_minúsculo pra variáveis dentro de classes
    '''
    def _set_pessoa(self):
        P1 = cp._Pessoa()
        print("Informações sobre a pessoa: ")
        P1._nome=input("Nome: ")
        P1._sexo=input("Sexo: ")
        P1._idade=input("Idade: ")
        self._pessoas.append(P1)
'''
    def _set_pessoa2(self, nome, sexo, idade):
            #P = cp._Pessoa(nome, sexo, idade)
            self._pessoas.append(cp._Pessoa(nome, sexo, idade))

    def _get_pessoas(self):
            for i in range(len(self._pessoas)):
                print("\n\nPessoa", i+1)
                print("Nome = ", self._pessoas[i]._nome)
                print("Sexo = ", self._pessoas[i]._sexo)
                if(self._pessoas[i]._idade==-1):
                    print("Idade confidencial")
                else:
                    print("Idade = ", self._pessoas[i]._idade)

    def _remove_pessoa(self, nome):
        cont = -1
        for i in range (len(self._pessoas)):
            if (self._pessoas[i]._nome==nome):
                cont = i
                self._pessoas[i]
        P = self._pessoas.pop(cont)
        return P
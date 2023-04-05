#coding: utf-8

import ClassePessoa as cp

class _Arquivo():
    def __init__(self):
        self._pessoas = []

    def _set_pessoa(self):
        P1 = cp._Pessoa()
        print('Informações da pessoa:')
        P1._nome=input('Nome: ')
        P1._sexo=input('Sexo: ')
        P1._idade=int(input('Idade: ') )
        self._pessoas.append(P1)
        if(P1._idade > 30):
            P1._idade = -1
            print('Idade confidencial')


    def _set_pessoa2(self, nome, sexo, idade):
        P = cp._Pessoa()
        P._nome=nome
        P._sexo=sexo
        P._idade=idade
        P._verifica_saida_idade()
        self._pessoas.append(P)

    def _get_pessoas(self):
        for i in range (len(self._pessoas)):
            print('\n\nPessoa', i+1)
            print('Nome = ', self._pessoas[i]._nome)
            print('Sexo = ', self._pessoas[i]._sexo)
            if(self._pessoas[i]._idade==-1):
                print('Idade confidencial')
            else:
                print('Idade = ', self._pessoas[i]._idade)


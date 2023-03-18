#coding: utf-8

class _Pessoa():
    def __init__(self, nome, sexo, idade):
        self._nome = nome
        self._sexo = sexo
        self._idade = idade
        self._verifica_saida_idade()

    def _verifica_saida_idade(self):
        if((self._sexo == "F")and(self._idade>30)):
            self._idade_secreta = self._idade
            self._idade=-1
        else:
             self._idade_secreta = False

    def _mostra_pessoa(self):
        print("Nome", self._nome)
        print("Sexo", self._sexo)
        print("Idade", self._idade)

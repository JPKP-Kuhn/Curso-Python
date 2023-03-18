#coding: utf-8

class _Pessoa():
    def __init__(self):
        self._nome = ""
        self._sexo = ""
        self._idade = -1

    def _verifica_saida_idade(self):
        if(self._sexo == "F")and(self._idade > 30):
            self._idade_secreta = self._idade
            self._idade = -1
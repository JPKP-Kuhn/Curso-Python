#coding: utf-8

import ClasseArquivo as ca

if __name__ == "__main__":
    Arq1 = ca._Arquivo()
    Arq1._set_pessoa()
    Arq1._set_pessoa2("Joana", "F", 32)
    Arq1._get_pessoas()
#coding: utf-8
import ClasseArquivo as ca

if __name__ == "__main__":
    Arq1 = ca._Arquivo()
    Arq1._set_pessoa2("Joana", "F", 32)
    Arq1._set_pessoa2("Marcia", "F", 29)
    Arq1._set_pessoa2("Antonio", "M", 24)
    Arq1._set_pessoa2("Rafael", "M", 40)
    print("Lista original")
    Arq1._get_pessoas()
    P = Arq1._remove_pessoa("Antonio")
    print("Lista final")
    Arq1._get_pessoas()
    print("Pessoa retirada : ")
    P._mostra_pessoa()

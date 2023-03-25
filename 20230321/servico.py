#coding: utf-8

if __name__ == "__main__":
    print('Só pra saber qual foi o serviço \n não precisa levar a sério, só brincadeira, kkkk')

class servico():
    def __init__(self):
        
        self._servico1 = 1
        self._servico2 = 2
    
    def _servico(self):
        decisao = input('Número do serviço que foi feito: ')
        if(decisao == 1):
            print('Dê a descarga e feche a tampa')
        else:
            print('Depressa! Dê a descarga e feche a tampa!')



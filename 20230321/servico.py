#coding: utf-8
import CaixaAcoplada as CA

if __name__ == "__main__":
    print('Só pra saber qual foi o serviço \n não precisa levar a sério, só brincadeira, kkkk')

class servico():
    def __init__(self, vaso):

        self._CaixaAcoplada = vaso
    
    def _servico(self):
        decisao = input('Número do serviço que foi feito: ')
        if(decisao == 1):
            print('Dê a descarga e feche a tampa')
        else:
            print('Depressa! Dê a descarga e feche a tampa!')
        self._CaixaAcoplada._descarga()
        if self._CaixaAcoplada._nivel_agua == self._CaixaAcoplada._nivel_maximo:
            self._CaixaAcoplada._encher()
        


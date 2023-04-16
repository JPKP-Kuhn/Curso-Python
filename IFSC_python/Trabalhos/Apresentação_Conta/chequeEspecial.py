#coding: utf-8
import contaBancaria as cB

class chequeEspecial(cB.contaBancaria):
    def __init__(self):
        super().__init__()
        self._limite = 0
        self._juros = 0.025
        self._renda = 0
        self._saldo_medio = 0
        
    def _set_renda(self, renda):
        self._renda = renda
        self._set_limite()

    def retirada(self, valor): #Polimorfismo
        if self._saldo - valor < self._limite:
           print('Limite de cheque especial insuficiente')
        else: 
            if self._saldo - valor < 0:
                self._saldo -= valor + (valor * self._juros)
            else:
                 self._saldo -= valor
            self._set_extrato('Retirada', valor)
        return self._saldo

    def _get_renda(self):
        return self._renda
    
    
    def _set_limite(self):
        if self._renda < 5000:
            self._limite = -2000
        else:
            self._limite = -5000


    def _get_limite(self):
        return self._limite

    
    def _set_saldo_medio(self, periodo):
        filtrado = list(filter(lambda saldo: int(saldo['Data'][:2]) == periodo, self.
        _extrato))
        if len(filtrado) != 0:
            saldo_medio = 0

            for extrato in filtrado:
                saldo_medio += extrato['Saldo Atual']
            saldo_medio = saldo_medio/len(filtrado)
            self._saldo_medio = saldo_medio
        return self._saldo_medio

    def _get_saldo_medio(self):
        return self._saldo_medio
    
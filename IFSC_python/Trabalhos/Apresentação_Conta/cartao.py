#coding: utf-8

import contaBancaria as cB
import datetime as d

class cartao(cB.contaBancaria):
    def __init__(self):
        super().__init__()
        self._limite_compra = 0
        self._compra_internacional = False
        self._compra_aprox = False
        self._juros_atraso = 0.03


    def _set_cartao(self, saldo):
        if saldo > 5000:
            self._limite_compra = 2500
            self._compra_internacional = True
        else:
            self._limite_compra = 1000

    def _get_cartao(self):
        return {
            "Limite de compra": self._limite_compra,
            "Compra internacional": self._compra_internacional,
            "Compra por aproximação": self._compra_aprox,
            "Juros de atraso": self._juros_atraso
        }
    
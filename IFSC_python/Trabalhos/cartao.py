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

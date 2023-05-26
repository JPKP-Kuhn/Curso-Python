#coding: utf-8
import pygame as pyg
class ValvulaAlimentacao(): 
	def __init__(self): 
		print("Valvula de alimentação criada") 
		self._vazao_entrada=3 #Vazao em litros/segundo
		self._status = "Fechada"

	def _abrirValvula(self):
		self._status = "Aberta"
		
	def _fecharValvula(self):
		self._status = "Fechada"

	def _get_vazao_entrada(self): 
		return 	self._vazao_entrada
		
	def _get_status(self): 
		return self._status	

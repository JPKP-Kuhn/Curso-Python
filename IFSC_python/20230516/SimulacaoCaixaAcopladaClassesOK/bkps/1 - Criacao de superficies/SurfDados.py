#coding: utf-8
		
import pygame as pyg

class SurfDados():  
	def SurfDados(self):	#Observar que nao é funcao construtora 
		self.SurfDados = pyg.Surface([260,400])	#Cria superficie para área de dados
		self.SurfDadosCor = (120,120,120)		#cinza escuro
		self.SurfDados.fill(self.SurfDadosCor)	#pinta a superficie .

		


#-*- coding: utf-8  -*-

import os
import pygame
import menu
import malha
#import tetromino

from tetromino import Tetromino



#Funcao de escrita
def escreverTela(fonte, mensagem, cor):
    text = font.render(str(mensagem), True, cor)
    text = text.convert_alpha()
    return text



def preparaBloco(end):	#Sao 7 tipos de blocos.; 
	blocos = []
	bloco = pygame.image.load(end).convert_alpha()
	bloco = pygame.transform.scale(bloco, (bloco_largura * 7, bloco_altura))
	for i in range(7):
		bloco_sup = bloco.subsurface(i * bloco_largura, 0, bloco_largura, bloco_altura)
		blocos.append(bloco_sup)
	return blocos


#Cor do texto:
Cor_do_texto = (255, 255, 255)

# Variaveis de tela
min_CoordenadaTela = (0, 0)		#Usado na etapa de construcao +- L220
Resolucao_tela = (680, 880)#Formato de tupla, para nao ser alterada
#Resolucao_tela = (340, 440)

#Dados dos blocos
bloco_largura, bloco_altura = 32, 32


mudNivel = 1	#Numeros de linhas para mudar o nível.


FPS = 60	#Numero de frames por segundo.
VelocidadeInicial = 1			
coord_prox_tetromino = (Resolucao_tela[0] / 10, Resolucao_tela[1] * 0.65)

Mostrador_relogio = True		#Mostrador do tempo de jogo em segundos
Mostrador_dados = False		 

Amplificador_Velocidade = 0.85
nvis = 3	#quantidade de vezes que mantem as linhas acumuladas invisíveis.


#Informacoes do jogo na tela
Coord_placar = (20, 50)
Coord_relogio = (20, 100)
Coord_nivel_jogo = (20, 150)
Coord_fps = (20, 200)

Coord_prox_bloco = (Resolucao_tela[0] / 10, Resolucao_tela[1] * 0.65)
Coord_seguinte = (Coord_prox_bloco[0] - 10, Coord_prox_bloco[1] - 3 * bloco_altura)

#Letra usada 
Fonte_Usada = 'Letra/SadanaSquare.ttf'
#Fonte_Usada = 'Letra/sewer.ttf'
#Fonte_Usada = 'Letra/stocky.ttf'

pygame.init()
pygame.display.set_caption("Memo Tetris")
tela_modo = pygame.display.set_mode(Resolucao_tela)
pygame.key.set_repeat(100, 70)

bloco_basico_end = "Figuras/blocos.png"
bloco_aux_end = "Figuras/bloco_aux.png"


# Carrega o pano de fundo
PanoFundoJogo = 'Figuras/back2.jpeg'
#PanoFundoMenu = 'Figuras/back2.jpeg' 
#PanoFundoMenu = 'Figuras/bricks.jpg' 
PanoFundoMenu = 'Figuras/333873.png' 
PanoFundo = pygame.image.load(PanoFundoJogo).convert()
PanoFundo = pygame.transform.scale(PanoFundo, tela_modo.get_size())

# Carrega fonte 
font = pygame.font.Font(Fonte_Usada, 36)

bloco_basico = preparaBloco(bloco_basico_end)
bloco_aux = preparaBloco(bloco_aux_end)

ProxSuperficie = escreverTela(font, "Próximo tetris", Cor_do_texto)

#Chama a classe Menu no módulo Menu
menu_itens = ['Jogar :-)', 'Sair :-(']	#Permite alteracao para ver outras opcoes.
menu_jogo = menu.Menu('Memo TETRIS ', PanoFundoMenu, Resolucao_tela, Fonte_Usada)

# Opcoes do menu
opcoes_usuario = ['Jogar', 'Sair do jogo']



for item in menu_itens:
	menu_jogo.add_item(item)

#Dados para formação da malha: 
colunas = 10
linhas = 20
compr_bloco = 32
altura_bloco = 32	

PanoFundoMalha = "Figuras/malha_quadriculada.png"
#PanoFundoMalha = "Figuras/malha_lisa.jpg"

while True:	
	while True:
		menu_jogo.mostra_tela(tela_modo)
		pygame.display.flip()		
        # Espera pela acao do jogador
		event = pygame.event.wait()	
		entrada_usuario = menu_jogo.verificaAcao(event)
		if entrada_usuario == menu_itens[0]:  
			break	# Inicia Jogo, sai da tela.

		elif entrada_usuario == menu_itens[1] or event.type == pygame.QUIT:  # quit
			exit()#Sai do jogo

	#Inicia a malha do jogo
	malha = malha.Malha(colunas, linhas, compr_bloco, altura_bloco, Resolucao_tela, PanoFundoMalha)
	
	velocidade_tetromino = VelocidadeInicial

	tetromino_atual = Tetromino((compr_bloco, altura_bloco), malha.get_coord_centro_tela(), velocidade_tetromino)
	# Cria proximo tetromino
	tetromino_proximo = Tetromino((compr_bloco, altura_bloco), coord_prox_tetromino, velocidade_tetromino)

	game_over = game_parado = joga_tetromino = False
	clock = pygame.time.Clock()
	tempo_total = 0.0
	nivel_do_jogo = 1
	dt = 1.0 / FPS
	acumulo = 0.0
	difficulty_level = 1


##########################
	invlinha = 0 	#Contador para fazer as linhas aparecerem
	invis = True

	while not game_over:		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:	
				#Tecla tem que ter sido apertada na tecla esc	
				#Possibilita sair pelo teclado teclando esc
				game_over = True
				invis = False
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
				tetromino_atual.move_direita()
				
				if malha.violaFronteira(tetromino_atual.get_coords()) or malha.sobrepoe(tetromino_atual.get_coords()):
					tetromino_atual.move_esquerda()


			elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
				tetromino_atual.move_esquerda()
				
				if malha.violaFronteira(tetromino_atual.get_coords()) or malha.sobrepoe(tetromino_atual.get_coords()):
					tetromino_atual.move_direita()
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
				tetromino_atual.rotacao_horaria()
				
				if malha.violaFronteira(tetromino_atual.get_coords()) or malha.sobrepoe(tetromino_atual.get_coords()):
					tetromino_atual.rotacao_antihoraria()
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
				tetromino_atual.rotacao_antihoraria()
					
				if malha.violaFronteira(tetromino_atual.get_coords()) or malha.sobrepoe(tetromino_atual.get_coords()):
					tetromino_atual.rotacao_horaria()
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:				
				tetromino_atual.aumenta_veloc()
			elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:				
				tetromino_atual.limpa_velocidade()	#Paralisa o tetromino (pausa)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:	#lanca a peca para baixo com tudo. 
				# lança peça
				joga_tetromino = True
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
				# Inicia modo pausa
				pause = True
				malha.mostra_Mensagem(tela_modo, font, Cor_do_texto, 'Jogo pausado')
				while pause:
					event = pygame.event.wait()
					if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
						pause = False
					elif event.type == pygame.QUIT:
						exit()
					elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
						malha.mostra_Mensagem(tela_modo, font, Cor_do_texto, 'Jogo retornado')
						
						break	
				#print("Saida do jogo L162")
				game_parado = True
	
		#Define aqui frame_time
		if game_parado:
			frame_time = dt
			game_parado = False
			clock.tick(FPS)
		else:
			frame_time = clock.tick(FPS) / 1000.0  # convert to seconds


		acumulo += frame_time		
		while acumulo >= dt and not game_over:
			while True:
				tetromino_atual.move_baixo(dt)
				sobrepoe = malha.sobrepoe(tetromino_atual.get_coords())
				if not joga_tetromino or sobrepoe:
					joga_tetromino = False
					break
			avancalinha = False		
			# tetromino alcanca o chao ou bate em outro tetramino.
			if sobrepoe:
				tetromino_atual.move_cima()
				malha.atualizar(tetromino_atual.get_coords(), tetromino_atual.get_color_index(), avancalinha)
				# Aumenta dificuldade toda vez que mudNivel linhas estejam completadas.
				if malha.get_placar() // mudNivel + 1 != difficulty_level:
					difficulty_level += 1
					velocidade_tetromino *= Amplificador_Velocidade

				# Troca os tetraminos, encerra o atual e cria novo
				tetromino_atual = tetromino_proximo
				tetromino_atual.set_coords(malha.get_coord_centro_tela())
				tetromino_atual.set_veloc(velocidade_tetromino)
				tetromino_proximo = Tetromino((bloco_largura, bloco_altura), Coord_prox_bloco, velocidade_tetromino)
				if (invlinha==nvis)or(avancalinha==True): 
					invis = False
					invlinha = 0
				else: 
					invlinha+=1
					invis = True
			game_over = malha.is_game_over()
			if game_over==True: 
				invis = False
			acumulo -= dt


		# create strings
		if Mostrador_relogio:
			tempo_total += frame_time		#Tempo de cada frame
			time_string = "Tempo de jogo " + '{0:02d}'.format(int(tempo_total // 60))+ ":" + '{0:02d}'.format(int(tempo_total % 60))
			relogio_espaco = escreverTela(font, time_string, Cor_do_texto)
		if Mostrador_dados:
			fps_string = "FPS: " + str(int(clock.get_fps()))
			fps_surface = escreverTela(font, fps_string, Cor_do_texto)
		placar_string = "Pontos: " + str(malha.get_placar())
		placar_espaco = escreverTela(font, placar_string, Cor_do_texto)
		nivel_string = "Nível: " + str(difficulty_level)
		nivel_espaco = escreverTela(font, nivel_string, Cor_do_texto)


		# Draw
		tela_modo.blit(PanoFundo, min_CoordenadaTela)
		tela_modo.blit(placar_espaco, Coord_placar)
		tela_modo.blit(nivel_espaco, Coord_nivel_jogo)
		if Mostrador_relogio:
			tela_modo.blit(relogio_espaco, Coord_relogio)
		if Mostrador_dados:
			tela_modo.blit(fps_surface, Coord_fps)
		tela_modo.blit(ProxSuperficie, Coord_seguinte)
		malha.mostrador(tela_modo, bloco_basico, invis)#Funcao que traz a dificuldade ao problema. 



		if not game_over:#Comentar tres primeiras linhas para provocar invisibilidade. 
			assist_coords = malha.get_coord_bloco_aux(tetromino_atual.get_coords())	
			for coord in assist_coords:	
				tela_modo.blit(bloco_aux[tetromino_atual.get_color_index()], coord)			
			
				
			tetromino_atual.mostra_tetromino(tela_modo, bloco_basico)



		tetromino_proximo.mostra_tetromino(tela_modo, bloco_basico)
		pygame.display.flip()

	malha.mostra_Mensagem(tela_modo, font, Cor_do_texto, 'Fim de Papo')
	clock.tick(1)#Pelo menos um frame por segundo para passar.

	exit()			



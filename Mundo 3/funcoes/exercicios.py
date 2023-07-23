#Ex1 çalculo de área
'''
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.2f}x{comp:.2f} é de {a:.2f}m²')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)

#Ex2 texto alinhado
def escreva(txt):
    print('~' * (len(txt)))
    print(f'{txt:^{len(txt) + 2}}')
    print('~' * (len(txt) + 2))
escreva('Olá, Mundo!')
escreva('João Pedro Kuhn')

#Ex3 contador
def contagem(inicio, fim, passo):
    if passo == 0: passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        fim -= 1
        if passo > 0:
            passo *= -1
    for i in range(inicio, fim + 1, passo):
        print( i , end=' ')
    print(' FIM!')
contagem(1, 10, 1)
contagem(10, 0, 2)
contagem(-10, 50, 3)
contagem(20, 10, -1)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)

#Ex4 maior de vários valores
def maior(*num):
    print(f'Foram passados {len(num)} valores: ')
    for i in num:
        print(i, end=', ')
    print(f'\nO maior valor é {max(num)}')
maior(3, 4, 10, 9, 15)
'''

#Ex5 Soma de valores pares aleatórios
from random import randint
def sorteia(lista):
    for i in range(5):
        lista.append(randint(0, 10))
    print(f'Os valores sorteados foram: {lista}')

lista = []
sorteia(lista)

def somaPar(lista):
    par = 0
    for i in lista:
        if i % 2 == 0:
            par += i
    print(f'Somando os valores pares de {lista} temos {par}')

somaPar(lista)

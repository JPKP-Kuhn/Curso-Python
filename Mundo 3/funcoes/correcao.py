#Ex1
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a:.1f}m².')

#Programa Principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)

#Ex2
def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)

escreva('OI')
escreva('João')

#Ex3
from time import sleep

def contador(i, f, p):
    print('-=' * 20)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
    print('-=' * 20)


contador(1, 10, 1)
contador(10, 0, 2)
print('personalize a contagem: ')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

#Ex4
from time import sleep

def maior(*num):
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informado {cont} valores ao todo.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

#Ex5
from random import randint
from time import sleep

def sorteia(lista):
    for cont in range(5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)

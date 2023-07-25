#Ex1 calculo de área
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

#Parte 2

#Ex1 votação
from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))

#Ex2 fatorial
def fatorial(n, show=False):
    """
    Calcula o fatorial de um número
    n = número a ser calculado
    show = mostra ou não a conta
    return: o valor do fatorial de n
    """
    f = 1
    if not show:
        for i in range(n, 0, -1):
            f *= i
        return f
    else:
        for i in range(n, 0, -1):
            f *= i
            if i == 1:
                return f'{i} = {f}'
            else:
                print(f'{i} x ', end='')

print(fatorial(5, show=True))
print(fatorial(5))

#Ex3 ficha de jogador de futebol
def ficha(nome='<desconhecido>', gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
ficha(nome, gols)

#Ex4 input de um valor numérico
def leiaInt(num):
    while not num.isnumeric():
        print('ERRO! Digite um número inteiro válido.')
        num = input('Digite um número: ')
    return int(num)

n = leiaInt('Digite um número: ')
print(f'Você digitou o numero {n}')


#Ex5 notas e médias
def notas(*num, sit=False):
    """
    Retorna um dicionário com informações sobre a turma -
    num = notas dos alunos, quantidade, maior, menor e média
    sit = mostra ou não a situação da turma, Boa ou Ruim pela média
    """
    turma = {'notas': len(num),
             'maior': max(num),
             'menor': min(num),
             'media': round(float(sum(num)/len(num)), 2)}
    if sit:
        return turma
    else:
        if turma['media'] >= 7:
            turma['situacao'] = 'Boa'
        else:
            turma['situacao'] = 'Ruim'
        return turma
    
print(help(notas))
print(notas(5.5, 2.5, 1.5, sit=True))
print(notas(9, 8, 7.5, 6.5))

#Outra ideia pro exercício 5
def notas(*num, sit=False):
    """
    Retorna um dicionário com informações sobre a turma -
    num = notas dos alunos, quantidade, maior, menor e média
    sit = mostra ou não a situação da turma, Boa ou Ruim pela média
    """
    turma = {'notas': len(num),
             'maior': max(num),
             'menor': min(num),
             'media': round(float(sum(num)/len(num)), 2)}
    if sit:
        return turma
    else:
        if turma['media'] >= 7:
            turma['situacao'] = 'Boa'
        else:
            turma['situacao'] = 'Ruim'
        return turma

notas_list = []

s = 'S'
while s == 'S':
    nota = float(input('Digite uma nota: '))
    notas_list.append(nota)
    s = input('Deseja continuar? [S/N] ').upper()[0]

situacao = input('Deseja ver a situação da turma? [S/N] ').upper()[0]
if situacao in 'S':
    print(notas(*notas_list, sit=True))
else:
    print(notas(*notas_list))

#Ex6 mini sistema de interactve help
def escreva(txt):
    print('~' * (len(txt) + 2))
    print(f'{txt:^{len(txt) + 2}}')
    print('~' * (len(txt) + 2))

def ajuda(com):
    print(help(com))

print('SISTEMA DE AJUDA PyHELP')
while True:
    codigo = input('Função ou Biblioteca > ')
    if codigo.upper() == 'FIM':
        escreva('ATÉ LOGO!')
        break
    else:
        (ajuda(codigo))
        escreva(f'Acessando o manual do comando \'{codigo}\'')

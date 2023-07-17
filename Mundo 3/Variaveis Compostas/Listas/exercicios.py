#Ex1 Entrada de dados lista

lista = []
for i in range(5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f' {i}...', end='')
print(f'\nO menor valor digitado foi {min(lista)} nas posições', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f' {i}...', end='')
print()

#Ex2 Ordenar entradas
continuar = 'S'
lista = []
while continuar == 'S':
    v = int(input('Digite um valor: '))
    if v not in lista:
        lista.append(v)
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
lista.sort()
print(lista)

#Ex3 ordenar array sem sort
ordem = []
for i in range(5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > ordem[-1]:
        ordem.append(n)
        print('Adicionado ao final da lista...')
    elif n < ordem[0]:
        ordem.insert(0, n)
        print('Adicionado na posição 0 da lista...')
    elif n < ordem[-1]:
        for i, v in enumerate(ordem):
            if n < v:
                ordem.insert(i, n)
                print(f'Adicionado na posição {i} da lista...')
                break
print(ordem)

#Ex4 leitura de inputs
cont = 'S'
array = []
c = 0
while cont == 'S':
    num = int(input('Digite um valor: '))
    array.append(num)
    cont = input('Quer continuar? [S/N] ').upper().strip()[0]
    if num == 5:
        c += 1
array.sort(reverse=True)
print(f'Foram digitado {len(array)} valores')
print(f'Os valores em ordem decrescente são {array}')
if 5 in array:
    print(f'O valor 5 faz parte da lista e foi digitado {c} vezes')
else:
    print('O valor 5 não faz parte da lista')

#Ex5 lista par e ímpar
cont = 's'
lista = []
while cont == 's':
    num = int(input('Digite um valor: '))
    lista.append(num)
    cont = input('Quer continuar? [S/N] ').lower().strip()[0]
print(f'A lista completa é {lista}')
par = []
impar = []
for v in lista:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')

#Ex6 Expressão matemática
expressao = []
exp = input('Digite uma expressão matemática com parênteses: ')
expressao.append(exp)
print(expressao)
for i, v in enumerate(expressao):
    if v.count('(') == v.count(')'):
        print('Expressão válida!')
    else:
        print('Expressão inválida!')
    

##################### -Listas Compostas- #####################
#Ex1 cadastro de pessoas, nome e peso
pessoas = []
dados = []
cadastro = 'S'
maior = menor = 0
while cadastro == 'S':
    nome = input('Digite um nome: ')
    peso = float(input('Digite o peso: '))
    cadastro = input('Quer continuar? [S/N] ').upper().strip()[0]
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    if len(pessoas) == 1:
        maior = menor = pessoas[0][1]
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()

#Ex2 lista com valores pares e ímpares
numeros = []
par = []
impar = []
for i in range(7):
    n = int(input(f'Digite o {i+1}º valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    par.sort()
    impar.sort()
numeros.append(par[:])
numeros.append(impar[:])
print(numeros)
print(f'Os valores pares digitados foram {numeros[0]}')
print(f'Os valores ímpares digitados foram {numeros[1]}')

#Ex3 matriz 3x3
matriz = [[], [], []]
par = coluna3 = maiorlinha2 = 0
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
print('-='*30)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if j == 2:
            coluna3 += matriz[i][j]
        if i == 1:
            if j == 0 or matriz[i][j] > maiorlinha2:
                maiorlinha2 = matriz[i][j]
    print()
print('-='*30)
#Ex4 Aprimoramento do anterior
for i in matriz:
    for j in i:
        if j % 2 == 0:
            par += j
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {maiorlinha2}')

#Ex5 MEGA SENA
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
from random import randint
sorteio = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = []
print('-='*3, f'SORTEANDO {sorteio} JOGOS', '-='*3)
for i in range(sorteio):
    for j in range(6):
        numero = randint(1, 60)
        if numero not in jogos:
            jogos.append(numero)
    jogos.sort()
    print(f'Jogo {i+1}: {jogos}')
    jogos.clear()

#Ex6 Boletim de alunos
resp = 'S'
alunos = {
    "nome": [],
    "notas": [],
    "media": []
}
while resp == 'S':
    alunos["nome"].append(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    alunos["notas"].append([nota1, nota2])
    alunos["media"].append((nota1 + nota2) / 2)
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, v in enumerate(alunos["nome"]):
    print(f'{i:<4}{v:<10}{alunos["media"][i]:>8.1f}')

mostrarNotas = 0
while mostrarNotas != 999:
    mostrarNotas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrarNotas == 999: break
    print(f'Notas de {alunos["nome"][mostrarNotas]} são {alunos["notas"][mostrarNotas]}')

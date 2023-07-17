#Ex1
listnum = []
maior = menor = 0
for c in range(0, 5):
    listnum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listnum[c]
    else:
        if listnum[c] > maior:
            miaor = listnum[c]
        if listnum[c] < menor:
            menor = listnum[c]
print('-='*30)
print(f'Você digitou os valores {listnum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listnum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listnum):
    if v == menor:
        print(f'{i}...', end='')
print()

#Ex2
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = input('Quer continuar? [S/N] ').strip().upper()[0]
    if r == 'N':
        break
print('-='*30)
numeros.sort()
print(f'Você digitou os valores {numeros}')

#Ex3
lista = []
for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados foram {lista}')

#Ex4
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N': break
print('-='*30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')

#Ex5
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N': break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')

#Ex6
expr = input('Digite a expressão: ')
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')


##Listas compostas
#Ex1
temp = []
princ = []
mai = men = 0
while True:
    temp.append(input('Nome:'))
    temp.append(float(input('Peso:')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai: mai = temp[1]
        if temp[1] < men: men = temp[1]
    princ.append(temp[:])
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    temp.clear()
    if resp == 'N':
        break
print('-='*30)
print(f'Os dados foram {princ}')
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end=' ')
print()

#Ex2
num = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i} valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
print(f'Todos os valores digitados foram {num}')
print(f'Os valores pares foram {sorted(num[0])}')
print(f'Os valores ímpares foram {sorted(num[1])}')

#Ex3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3): #for de linha
    for c in range(0, 3): #for de coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

#Ex4
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3): #for de linha
    for c in range(0, 3): #for de coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[l][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')

#Ex5
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 0
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f' SORTEANDO {quant} JOGOS ', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*3, '< Boa Sorte >', '-='*3)

#Ex6
ficha = list()
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar[S/N]? ').strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999: 
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

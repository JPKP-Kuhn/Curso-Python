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

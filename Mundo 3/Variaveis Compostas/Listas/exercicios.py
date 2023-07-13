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
    

#Ex1
cont = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", 
    "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", 
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}.')

#Ex2
brasileirao = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
               'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
               'Atlético-PR','Bahia', 'São Paulo', 'Fluminense', 'Sport Recife')
print(f'Lista de times: {brasileirao}')
print('-='*15)
print(f'Os 5 primeiros colocados são {brasileirao[0:5]}')
print(f'Os 4 últimos são {brasileirao[-4:]}')
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print(f'O Chapecoense está na {brasileirao.index("Chapecoense")+1}ª posição')

#Ex3
from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0,10))
print(f'Os valores sorteados foram: {n}')
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')

#Ex4
num = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print('O valor 9 apareceu ', num.count(9), 'vezes')
print(f'O valor 3 apareceu na posição {num.index(3)+1}º posição' if 3 in num else 'O valor 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

#Ex5
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]:>7.2f}')
print('-'*40)

#Ex6
palavras = ('aprender', 'programar', 'linguagem', 'python',
             'curso', 'gratis', 'praticar', 'trabalhar', 'mercado', 'programador')
for i in palavras:
    print(f'\nNa palavra {i} temos ', end='')
    for letra in i:
        if letra in 'aeiou':
            print(letra, end=' ')

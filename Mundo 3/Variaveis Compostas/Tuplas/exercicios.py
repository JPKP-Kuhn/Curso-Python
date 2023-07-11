#Ex1 Contagem até 20

contagem = (
    "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete",
    "dezoito", "dezenove", "vinte"
)
n = 21
while n not in range(0, 21):
    n = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {contagem[n-1]}.')

#Ex2 Colocados do brasileirão série B 2023
brasileirao = ('Criciúma', 'Sport Recife', 'Vila Nova', 'Novorizontino', 
               'EC Vitória', 'Mirassol', 'Juventude', 'Guarani', 'Ceará SC',
               'Botafogo SP', 'Atlético-GO', 'CRB', 'Ponte Preta', 'Ituano',
               'Sampaio Corrêa', 'Chapecoense', 'Tombense', 'Londrina', 'Avaí',
               'ABC')
print(f'Os 5 primeiros colocados são {brasileirao[0:5]}')
print(f'Os últimos 4 são {brasileirao[-4:]}')
print(sorted(brasileirao))
print(brasileirao.index('Chapecoense')+1)

#Ex3 Tupla com números aleatórios
from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(tupla)
print(max(tupla))
print(min(tupla))

#Ex4 Valores guardados numa tupla
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))
valores = (a, b, c, d)
print(valores)
print('O 9 apareceu', valores.count(9))
if 3 in valores:
    print('O 3 foi digitado na posição ', valores.index(3))
else:
    print('O 3 não foi digitado')
for i in range(0, len(valores)):
    if valores[i] % 2 == 0:
        print('Pares: ', end='')
        print(valores[i])

#Ex5 Listagem de produtos
materialEscolar = ('Lápis', 1.75, 'Borracha', 2.00)
print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)
print('{:<30}R${:>5}'.format(materialEscolar[0], materialEscolar[1]))
print('{:<30}R${:>5}'.format(materialEscolar[2], materialEscolar[3]))

#Ex6 Palvaras com vogais

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'computador', 'futuro', 'tecnologia', 'sequoia')

for i in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[i]} temos ', end='')
    for j in range(0, len(palavras[i])):
        if palavras[i][j] in 'aeiou':
            print(palavras[i][j], end=' ')
print()


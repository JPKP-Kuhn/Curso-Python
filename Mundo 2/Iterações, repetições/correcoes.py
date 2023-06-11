from time import sleep
from datetime import date

#Ex 1
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print("BUM! BUM! POOW!")

#Ex2
for n in range(2, 51, 2):
    print(n, end=' ')
print("Acabou")

#Ex3
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        contador += 1
print(f'A soma de todos os valores é solicitados é {soma}')

#Ex4
num = int(input("Digite um número para tabuada: "))
for c in range(1, 11):
    print("{} x {:2} = {}".format(num, c, num*c))

#Ex5
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input("Digite o {}º valor: ".format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print("Você informou {} números e a soma foi {}".format(cont, soma))


#Ex6
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo+razão, razão):
    print("{}".format(c), end='↛')
print("Acabou")

#Ex7
num = int(input('Digite um número: '))
tot = 0
for i in range(1, num+1):
    if num % i ==0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i),end='')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')

#Ex8
frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''
inverso = ''
for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]
'''
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')

#Ex9
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a  {}º pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))

#Ex10
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Peso da {}º pessoa').format(i))
    if i == 1:
        maior = i
        menor = i
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi de {maior}kg')
print(f'O menor peso foi de {menor}kg')

#Ex11
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulheres = 0
for p in range(1, 5):
    print('----{}º PESSOA ----'.format(p))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulheres += 1
mediaidade = somaidade / 4
print(f'A média da idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
print(f'Ao todo são {totmulheres} com menos de 20 anos')
from random import randint
from math import factorial
#Ex1
sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0] #Fatiamento da string
while sexo not in 'MmFf':
    sexo = input('Dados inválidos, informe seu sexo: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')

#Ex2
computador = randint(0, 10)
print('Pensei em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou!')
print(f'Acertou com {palpites} tentativas')

#Ex3
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto entre {} e {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
    print('=-='*10)
print('Fim do programa! Volte sempre!')

#Ex4
n = int(input('Digite o seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')

#sem biblioteca
n = int(input('Digite o seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'O fatorial de {n} é {f}')

#Ex5
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
c = 1
while c <= 10:
    print('{} -->'.format(termo), end='')
    termo += razao
    c += 1

#Ex6
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais !=0:
    total += mais
    while c <= total:
        print('{} -->'.format(termo), end='')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    print(f'Progressão finalizada com {total} termos mostrados')
print('FIM')

print('-='*30)
print('Sequência de Fibonacci')
print('-='*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} -> {t2}', end='')
count = 3
while count <= n:
    t3 = t1 + t2
    print(' -> {t3}', end='')
    t1 = t2
    t2 = t3
    count += 1
print('FIM')

num = c = soma = 0
num = int(input('Digite um número inteiro [999 para parar]: '))
while num != 999:
    soma += num
    c += 1
    num = int(input('Digite um número inteiro [999 para parar]: '))
print(f'Você digitou {c} números')

#Ex7
resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi de {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

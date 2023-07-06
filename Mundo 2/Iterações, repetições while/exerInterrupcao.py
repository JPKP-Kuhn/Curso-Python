from random import randint

#Ex1 soma e contagem de números inteiros
soma = i = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999: break
    soma += n
    i += 1
print(f'A soma foi {soma} com um total de {i} números digitados')

#Ex2 Tabuada
while True:
    x = int(input('Digite um número para sua tabuada: '))
    if x < 0: break
    for i in range(1, 11):
        print(f'{x} x {i} = {x*i}')

#Ex3 Jogo de par ou ímpar
print('Jogar par ou ímpar! Jogador tem a preferência')
i = 0
while True:
    jogador = input('Par ou Ímpar? ').strip()
    escolha = int(input('Escolha um número entre 0 e 10: '))
    computador = randint(0, 10)
    if (escolha + computador) % 2 == 0 and jogador == 'Par':
        print(f'O compuador jogou {computador}')
        print('Jogador venceu!')
        i += 1
    elif (escolha + computador) % 2 == 0 and jogador == 'Ímpar':
        print(f'O compuador jogou {computador}')
        print('Computador venceu!')
        break
    elif (escolha + computador) % 2 != 0 and jogador == 'Ímpar':
        print(f'O compuador jogou {computador}')
        print('Jogador vence!')
        i += 1
    elif (escolha + computador) % 2 != 0 and jogador == 'Par':
        print(f'O compuador jogou {computador}')
        print('Computador vence!')
        break
print(f'O jogador venceu {i} vezes')


#Ex4 leitura de pessoas
controlador = 'S'
adulto = homem = mulherAbaixo20 = 0
print('Cadastro de pessoas')
while controlador in 'Ss':
    idade = int(input('Informe a idade: '))
    sexo = input('Informe o sexo:[M/F] ')
    controlador = input('Você quer continuar?[S/N] ')
    if controlador not in 'SsNn':
        controlador = input('Você quer continuar?[S/N] ')
    if idade > 18:
        adulto += 1
    if sexo in 'Mm':
        homem += 1
    if idade < 20 and sexo in 'Ff':
        mulherAbaixo20 += 1
print(f'Foram cadastradas {adulto} pessoas acima de 18, {homem} homens e {mulherAbaixo20} mulheres abixo de 20')

#Ex5 nome e peço de produtos
controlador = 'S'
menor = float('inf')
total = caro = 0
barato = ''
print('Produtos para compras')
while controlador in 'Ss':
    nomeProduto = input('Nome do produto: ')
    preco = float(input('Preço do produto: R$'))
    controlador = input('Continuar?[S/N] ')
    total += preco
    if preco > 1000:
        caro += 1
    if preco < menor:
        menor = preco
        barato = nomeProduto
print(f'Total gasto R${total:.2f}, {caro} produtos custam mais de R$1000 e o produto mais barato é o {barato}')

#Ex6 Caixa eletrônico com cédulas de 50, 20, 10 e 1
valor = int(input('Valor inteiro que queira sacar: '))
notas50 = valor // 50
notas20 = valor // 20
notas10 = valor // 10
notas1 = valor // 1
if (valor - notas50*50) != valor:
    valor -= notas50*50
    notas20 = valor // 20
if (valor - notas20*20) != valor:
    valor -= notas20*20
    notas10 = valor // 10
notas10 = valor // 10
if (valor - notas10*10) != valor:
    valor -= notas10*10
    notas1 = valor // 1
notas1 = valor // 1
print(f' {notas50} notas de 50,\n {notas20} notas de 20,\n {notas10} notas de 10,\n {notas1} notas de 1')
    


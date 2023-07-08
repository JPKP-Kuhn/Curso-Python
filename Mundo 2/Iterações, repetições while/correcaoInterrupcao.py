from random import randint

#Ex1
soma = i = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999: break
    i += 1
    soma += num
print(f'A soma dos valores é foi {soma}, foram {i} valores digitados')

#Ex2 Tabuada
while True:
    n = int(input('Tabuada de qual núemro? '))
    if n < 0: break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('-'*30)

#Ex3 Jogo de par ou ímpar
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P/I]').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print('Deu par' if total % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes')

#Ex4
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ''
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F]').strip().upper()[0]
    if idade > 18: tot18+=1
    if sexo == 'M': totH+=1
    if sexo == 'F' and idade < 20: totM20+=1
    resp = ''
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]').strip().upper()[0]
    if resp == 'N': break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'Total de {totM20} mulheres com menos de 20 anos')

#Ex5
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = input('Nome do produto:')
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if  preco > 1000: totmil+=1
    if cont == 1 or preco < menor: 
        menor = preco
        barato = produto
    resp = ''
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]').strip().upper()[0]
    if resp == 'N': break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'Total  da compra foi de R${total:.2f}')
print(f'Temos {totmil} prprodutos custando mais de mil reais')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')


#Ex6
print('='*30)
print('{:^30}'.format('Banco CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0: break
print('='*30)
print('Volte sempre ao Banco CEV! Tenha um bom dia!')

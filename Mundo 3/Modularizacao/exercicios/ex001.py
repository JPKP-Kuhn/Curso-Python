import moedas

preco = float(input('Digite o preço: R$'))
'''
print(f'A metade de {moedas.moeda(preco)} é {moedas.metade(preco, True)}')
print(f'O dobro de {moedas.moeda(preco)} é {moedas.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(preco, 10, True)}')
print(f'Diminuindo 10%, temos {moedas.diminuir(preco, 10, True)}')
print(f'Aumentando em 23%, temos {moedas.aumentar(preco, 23, True)}')
print(f'Diminuindo em 77%, temos {moedas.diminuir(preco, 77, True)}')
'''
moedas.resumo(preco, 10, 25)

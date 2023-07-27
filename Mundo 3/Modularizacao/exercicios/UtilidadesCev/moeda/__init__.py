def dobro(n, monetario=False):
    if monetario:
        return moeda(n*2)
    else:
        return n*2

def metade(n, monetario=False):
    if monetario:
        return moeda(n/2)
    else:
        return n/2

def aumentar(n, p, monetario=False):
    if monetario:
        return moeda(n * (1 + p/100))
    else:
        return n * (1 + p/100)

def diminuir(n, p, monetario=False):
    if monetario:
        return moeda(n * (1 - p/100))
    else:
        return n * (1 - p/100)

def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')

def resumo(n, a=0, d=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{d}% de redução: \t{diminuir(n, d, True)}')
    print('-'*30)
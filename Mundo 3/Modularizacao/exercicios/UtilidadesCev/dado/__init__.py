def leiaDinheiro(r):
    r = input('Digite o preço: R$').strip().replace(',', '.') #Remove espaços e substitui vírgula por ponto
    if r.isalpha() or r == '':
        print('Erro! Digite um valor válido!')
        return leiaDinheiro(r)
    else:
        return float(r)
                 
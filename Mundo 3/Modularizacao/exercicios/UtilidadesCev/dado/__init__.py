def leiaDinheiro(r):
    r = input('Digite o preço: R$').strip().replace(',', '.') #Remove espaços e substitui vírgula por ponto
    if r.isalpha() or r == '':
        print('Erro! Digite um valor válido!')
        return leiaDinheiro(r)
    else:
        return float(r)
    
def leiaDinheiro1(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
        
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor
                 
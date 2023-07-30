def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO! O usuário não informou os dados!\033[m')
            return 0
        else:
            return num

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(vetor):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in vetor:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
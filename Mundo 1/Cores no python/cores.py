print("\033[31mOlá, mundo!")
print("\033[31;43mOlá, mundo! \033[m")
print("\033[1;31;43mOlá, mundo! \033[m")
print("\033[4;31;45mOlá, mundo! \033[m")
print("\033[7;31mOlá, mundo! \033[m")
print("\033[7;30mOlá, mundo! \033[m")
print("\033[33;44mOlá, mundo! \033[m")
print("\033[7;33;44mOlá, mundo! \033[m")

a =3
b =5
print("Os valores das cores são \033[32m{}\033[m  e \033[31m{}\033[m".format(a, b))

nome = 'João'
print("Olá, muito prazer em te conhecer, {}{}{}!!!".format('\033[1;4;34m',nome, '\033[m'))

sobrenome = 'Kuhn'
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretobranco': '\033[7;30m'
}
print("Olá, muito prazer em te conhecer, {}{}{}!!!".format(cores['amarelo'],sobrenome, cores['limpa']))

print('\033[1;32;40m-=' * 10, cores['limpa'])
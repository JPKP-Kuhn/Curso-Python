#Utilizar funções pra uma rotina
'''
def mostralinha():
    print('-' * 30)

#Programa principal
mostralinha()
print('     JOGADOR     ')
mostralinha()


def mensagem(msg):
    print('-' * 30)
    print(f'{msg:<30}')
    print('-' * 30)

mensagem('Sistema de alunos')

a = 2
b = 3
s = a + b
print(s)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
soma(4, 5)
soma(b=4, a=5)

#Empacotamento de parâmetros
def contador(*num): #Símbolo de desempacotamento, vai ter vários parâmetros
    for v in num:
        print(f'{v} ', end='')
    print(f'FIM! Ao todo são {len(num)} números.')

contador(2, 1, 7) #Vai ser uma tupla
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lista):
    for i in range(len(lista)):
        lista[i] *= 2

valores = [6, 3, 4, 2, 7, 1, 9]
print(valores)
dobra(valores)
print(valores)
'''
#Funções parte 2

#Interactive help
help(print) #Mostra o manual da função print
print(input.__doc__) #Mostra o manual da função input
#para sair é quit

#Docstrings
#É a documentação de uma função, uma string de documentação
#Toda função deve ter uma docstring, as internas do python tem, com o help

def contador(i, f, p):
    '''
    DOCSTRING
    -> Faz uma contagem e mostra na tela
    i = início da contagem
    f = fim da contagem
    p = passo da contagem
    return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c} ', end=' ')
        c += p
    print('FIM!')

contador(2, 10, 2)
help(contador) #Mostra a docstring da função

#Parâmetros opcionais
def somar(a, b, c = 0): #C é opcional, se não for passado, vai valer 0
    '''
    Faz a soma de três valores e mostra o resultado na tela
    '''
    s = a+b+c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)

#Dá pra colocar todos os parâmetros como opcionais
def soma(a=0, b=0, c=0):
    s = a+b+c
    print(f'A soma vale {s}')
soma()

#Escopo de variáveis
#Escopo é o local onde a variável vai existir e onde ela vai deixar de existir


def teste():
    x = 8 #Variável local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Program aprincipal
n = 2 #Variável global
print(n)
teste()
#print(f'No programa principal, x vale {x}') #Vai dar erro, pois x é local

def local(b):
    global a #Agora a é global
    a = 8 #Variável local
    b += 4
    c = 2
    print(f'Valor de a {a}')
    print(f'Valor de b {b}')
    print(f'Valor de c {c}')

a = 5 #a global
local(a)
print(f'Valor de a {a}')

#Retorno de valores return

def somar(a=0, b=0, c=0):
    s = a+b+c
    return s #Retorna o valor de s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')

#Prática
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

def par(n=0):
    if n%2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))
if par(num):
    print('É par')
else:
    print('Não é par')

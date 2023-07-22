#Utilizar funções pra uma rotina
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

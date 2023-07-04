from random import randint
#Ex1 identificação do sexo até digitar corretamente
genero = input('Digite seu sexo [M/F]: ')
while genero not in 'MF':
    genero = input('Dado inválido, digite novamente [M/F]: ')

#Ex2 Jogo de adivinhação
computador = randint(0, 10)
jogada = int(input('Adivinhe o número pensado pelo computador entre 0 e 10: '))
tentativas = 1
while jogada != computador:
    jogada = int(input('Ainda não, tente de novo: '))
    tentativas += 1
print(f'Parabéns, você conseguiu adivinhar em {tentativas} tentativas')

#Ex3 fazendo operações matemáticas
n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))
while True:
    escolha = int(input('''O que você quer fazer com esses valores?
    [1]Somar; [2]multiplar; [3]maior; [4]novos números; [5]sair do programa'''))

    if escolha == 1:
        print(n1 + n2)
    elif escolha == 2:
        print(n1 * n2)
    elif escolha == 3:
        print(max(n1, n2))
    elif escolha == 4:
        n1 = int(input('1º valor: '))
        n2 = int(input('2º valor: '))
    elif escolha == 5:
        break

#Ex4 fatorial
fator = int(input('Digite um número para o seu fatorial: '))
fatorial = fator
while fator != 1:
    fatorial *= (fator-1)
    fator -= 1
print(fatorial)

print('Agora com o for')
fator = int(input('Digite um número para o seu fatorial: '))
fatorial = fator
for i in range(fator-1, 0, -1):
    fatorial *= i
print(fatorial)

#Ex5 PA com até o 10º termo
primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razao
while primeiro != decimo+razao:
    print(primeiro, end=' ')
    primeiro += razao
print('\n')


#Ex6 PA com escolha de termos
primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
ntermos = primeiro
while True:
    termos = int(input('Mais quantos termos? [0 finaliza]'))
    if termos == 0:
        break
    for i in range(termos):
        print(ntermos, end=' ')
        ntermos += razao

#Ex7 Sequência de Fibonacci
n = int(input('Digite um número para ter os n 1º termos da sequência de Fibonacci: '))
Natual = 1
Nanterior = 0
print(Nanterior, Natual, end=' ')
contador = 3
while contador < n:
    termo = Natual +  Nanterior
    Nanterior = Natual
    Natual = termo
    contador += 1
    print(termo, end=' ')

#Ex8 Soma de números
n = 0
soma = 0
c = 0
while n != 999:
    n = int(input('Digite um número inteiro: [parar: 999] '))
    if n != 999:
        soma += n
        c += 1
print(f'A soma de todos os números é {soma} e foram digitados {c} números')

#Ex 9 média de valores digitados
controlador = 'S'
media = 0
n = []
while controlador in 'Ss':
    v = int(input('Digite um valor: '))
    n.append(v)
    controlador = input('Você quer continuar? [S/N] ')
max = max(n)
min = min(n)
media = sum(n) / len(n)
print(f'Maior valor {max}, menor valor {min}. A média é {media}')



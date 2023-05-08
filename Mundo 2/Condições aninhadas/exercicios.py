import datetime
import random
import time

#Ex1 Financiamento

valor = float(input("Qual o valor da casa que você deseja comprar: "))
salario = float(input("Digite seu salário: "))
anos_pagamento = int(input("Quantos anos de pagamento: "))

valor_parcelas = valor / anos_pagamento / 12

if valor_parcelas / salario > 0.3:
    print("Você não poderá financiar essa casa")
else:
    print("Seu financiamento será de R%${:.2f} por mês".format(valor_parcelas))

#Ex2 Bases numéricas
inteiro = int(input('Digite um número inteiro qualquer: '))
escolha = int(input("Convertê-lo para; (1)Binário; (2)Octal; (3)Hexadecimal: "))

if escolha == 1:
    print(bin(inteiro))
elif escolha == 2:
    print(oct(inteiro))
else:
    print(hex(inteiro))


#Ex3 Nº maior ou menor

n1 = int(input("n1: "))
n2 = int(input("n2: "))
maximo = max(n1, n2)
minimo = min(n1, n2)
if n1 == n2:
    print('Não há valor maior')
else:
    if maximo == n1:
        print(f"O primeiro valor é maior, {n1}")
    if minimo == n1:
        print(f"O primeiro valor é menor {n1}")
    if maximo == n2:
        print(f"O segundo valor é maior, {n2}")
    if minimo == n2:
        print(f"O segundo valor é o menor, {n2}")


#Ex4 alistamento militar
data = str(datetime.date.today())
ano = int(data[:4])

nascimento = int(input("Seu ano de nasciemnto: "))
if (ano - nascimento) < 18:
    print("Ainda vai se alistar")
    print('Ainda faltam', 18 - (ano - nascimento), 'anos')
elif ano - nascimento == 18:
    print("Está na hora de se alistar")
else:
    print("Já passou o tempo de alistamento")
    print('Passou', (ano - nascimento) - 18, ' anos')

#Ex5 média
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2

if media < 5.0:
    print("REPROVADO")
elif media > 5.0 and media < 7.0:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")

#Ex6 Classificação de atleta
#utiliza o mesmo ano para calcular a idade e pega o nascimento
if ano - nascimento <= 9:
    print("Atleta mirim")
elif ano - nascimento <=14:
    print("Atleta infantil")
elif ano - nascimento <=19:
    print("Atleta junior")
elif ano - nascimento <= 20:
    print("Atleta Sênior")
else:
    print('Atleta Master')

#Ex7 Tipo de triângulo

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a < b + c and a > b - c:
    print("Parabéns, você tem um triângulo")

    if a == b and a == c:
        print("Triângulo equilátero")
    elif a == b or b == c:
        print('Triângulo isósceles')
    else:
        print("Triângulo escaleno")

#Ex8 IMC
peso = float(input('Informe seu peso: '))
altura = float(input("Informe sua altura: "))

imc = peso / altura **2
if imc < 18.5:
    print("Abaixo do peso")
elif imc > 18.5 and imc < 25:
    print('Peso ideal')
elif imc > 25 and imc < 30:
    print("Sobrepeso")
elif imc > 30 and imc < 40:
    print('Obesidade')
else:
    print("Obesidade mórbida")


#Ex pagamento
preco = float(input("Digite o valor de um produto: "))
opcao = int(input("Digite a forma de pagamento: (1)à vista; (2)à vista com cartão; (3) em duas vezes; (4) três ou mais vezes: "))
if opcao == 1:
    preco *= 0.9
    print(f"Agora o preço é {preco}")
elif opcao == 2:
    preco *= 0.95
    print(f"Agora o preço é {preco}")
elif opcao == 3:
    print(f"Agora o preço é {preco}")
else:
    preco *= 1.2
    print(f"Agora o preço é {preco}")


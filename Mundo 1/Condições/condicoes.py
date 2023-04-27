from random import randint
from datetime import date

tempo = int(input("Quntos anos tem seu carro? "))
if (tempo <= 3):
    print("Carro novo")
else:
    print("Carro velho")
print("--FIM--")
#Fazer como se fosse um operador ternário;:
print("carro novo" if tempo <=3 else "carro velho")

nome = input("Digite seu nome: ").lower()
if nome == "joão":
    print("Seu nome é tão lindo")
print("Bom dia, ", nome)

n1 = float(input("Digite a sua nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2)/2
print("A sua média é {:.1f}".format(m))
if m >= 6:
    print("Sua média foi boa\n")
else:
    print("Sua média foi ruim, estude mais\n")

#-- Exercícios --

#Ex1 descobrir o número:
inteiro = randint(0, 5)
sorte = int(input("Escolha um número entre 0 e 5: "))
while sorte != inteiro:
    sorte = int(input("Errou, tente novamente: "))
if sorte == inteiro:
    print("Parabéns, você acertou!")

#Ex2 Velocidade limite
v = float(input("Digite a velocidade do carro em km/h: "))
if v > 80:
    print("Sua velocidade é maior do que o limite de 80km/h")
    print("Sua multa é de R${:.2f}".format(7 * (v - 80)))
else:
    print("Velocidade permitida")

#Ex3 Número par ou ímpar
n = int(input("Digite um número natural: "))
if n % 2 == 0:
    print("Númro digitado é par")
else:
    print("Número digitado é ímpar")

#Ex4 Viagem de ônibus
dist = float(input("Distância da viagem: "))
if dist <= 200:
    print(f"O valor a ser pago pela viagem é R${dist * 0.50}")
else:
    print(f"O valor a ser pago pela viagem é R${dist * 0.45}")

#Ex5 Ano bissexto
ano = int(input("Informe um ano, 0 pro ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")

#Ex6 O menor e o maior número
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print("O maior é ", maior)
print("O menor é ", menor)

#Ex7 aumento de salário
salario = float(input("Salário: "))
if salario > 1250:
    print("Aumento de 10%, {:.2f} ".format(salario *1.1))
else:
    print("Aumento de 15%, ", salario * 1.15)

#Ex8 triângulo
n1 = int(input("a: "))
n2 = int(input("b: "))
n3 = int(input("c: "))
if n1 < n2 + n3 and n1 > n2 - n3:
    print("Parabéns, você tem um triângulo")

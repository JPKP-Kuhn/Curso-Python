import time
from datetime import date

#Ex1 Contagem regressiva
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)
print("Fogos liberados para iluminar o céu!")

#Ex2 Nº pares de 1 a 50
for i in range(0, 52, 2):
    print(i)

#Ex3 soma entre os números ímpares múltiplos de 3 entre 1 e 500
s = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
print(f"Soma dos números: {s}")

#Ex4 Tabuada
tabuada = int(input("Digite um número para mostrar sua tabuada: "))
for i in range(0, 11):
    print(f"{tabuada} x {i} = {tabuada * i}")

#Ex5 Soma de números pares
soma = 0
for i in range(0, 6):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        soma += n
print(soma)


#Ex6 Progressão Aritmética dos 10 primeiros termos
print("Criação da PA")
n1 = int(input("Primeiro termo: "))
razao = int(input("Escreva a razão da PA: "))
An = n1 + (10 -1)*razao
An += 1

for i in range(n1, An, razao):
    print(i)

#Ex7 Detectar se é número primo
n = int(input("Digite um número: "))
contador = 0
for i in range(1, n+1):
    if n % i == 0 or n % i == 0:
        print("Divisível por {}".format(i))
        contador += 1
if n == 1:
     print("1 não é primo")
elif contador == 2:
        print(f"O número {n} é primo")
else:
     print("Não é primo")

#Ex8 palíndromo
frase = input("Digite para saber se sua frase é um palíndromo: ").strip()
frase = frase.replace(" ", "")
teste = False
for i in range(len(frase)//2): #Só a metade da frase
     if frase[i] != frase[-i-1]: #a primeira letra e compara com a última
          print("Não é um palíndromo")
          teste = False
          break
     else:
          teste = True
if teste == True:
     print("A frase é um palíndromo")


#Ex9 contador de 7 pessoas que atingiram a maior idade
maior = 0
menor = 0
for i in range(0, 8):
     nasc = int(input("Digite ano de nascimento: "))
     idade = date.today().year- nasc
     if idade >= 21: #Maior idade com 21
          maior += 1
     else:
          menor += 1
print(f"Nº de pessoas de menor: {menor} e pessoas de maior: {maior}")

#Ex10 maior e menor peso
maior = 0
menor = float('inf')
for i in range(6):
     peso = float(input("Digite o peso: "))
     if peso > maior:
          maior = peso
     elif peso < menor:
          menor = peso
print(f"Maior peso {maior}. Menor peso {menor}")


#Ex11 nome, idade, sexo de 4 pessoas
media_idade, mais_velho = 0, 0
nome_mais_velho = ""
contador = 0
for i in range(4):
     nome = input("Digite um nome: ")
     idade = int(input("Digite a idade: "))
     sexo = input("Sexo, M ou F: ")
     media_idade += idade
     if idade > mais_velho and sexo == "M":
          mais_velho = idade
          nome_mais_velho = nome
     if idade < 20 and sexo == "F":
        contador += 1
     
print(f"Media das idades é {media_idade/4}")
print(f"Nome do homem mais velho é {nome_mais_velho}, sua idade é {mais_velho}")
print(f"Há {contador} mulheres com menos de 20 anos")

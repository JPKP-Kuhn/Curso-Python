import math

#EX 01
n1 = float(input('Digite um número Real: '))
print(math.floor(n1))

#EX 02 Teorema de Pitágoras
cat1 = int(input('Digite o primeiro cateto: '))
cat2 = int(input('Digite o segundo cateto: '))
hip = cat1**2 + cat2**2
print(hip**(1/2))
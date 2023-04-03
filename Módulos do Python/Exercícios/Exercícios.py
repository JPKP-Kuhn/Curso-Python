import math
import random
from playsound import playsound

#EX 01
n1 = float(input('Digite um número Real: '))
print(f'O valor digitado foi {n1}, sua porção inteira é: ', math.floor(n1))
#também poderia utilizar o math.trunc(n1), ou sem importar colocar int(n1)

#EX 02 Teorema de Pitágoras
cat1 = int(input('Digite o primeiro cateto: '))
cat2 = int(input('Digite o segundo cateto: '))
hip = cat1**2 + cat2**2
print(hip**(1/2))
#Usando o método math - hip = math.hypot(co, ca)

#EX 03 seno, cosseno e tangente
angulo = int(input('Digite um ângulo: '))
sin = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))

print('Nesse ângulo de {}° seus valores de seno, cosseno e tangente são respectivamente {:.2}, {:.2} e {:.2}'.format(angulo, sin, cos, tg))

#EX 04 sorteio de aluno
alunos = []
alunos.append(input('Primeiro aluno: '))
alunos.append(input('Segundo aluno: '))
alunos.append(input('Terceiro aluno: '))
alunos.append(input('Quarto aluno: '))
print(random.choice(alunos))
#ou definir primeiro os alunos, inserí-los no array e daí o random.choice

#EX 05 sorteio ordem de apresentação dos alunos do EX 04
print(random.sample(alunos, k=len(alunos)))
#random.shuffle embaralha a lista, depois é só print(lista)

#EX 06 tocar arquivo .mp3
playsound('asd052_03_Brainwave_(Mike-McGuill).mp3')
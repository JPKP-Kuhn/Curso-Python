import math
import random
from playsound import playsound

#EX 01
n1 = float(input('Digite um número Real: '))
print(math.floor(n1))

#EX 02 Teorema de Pitágoras
cat1 = int(input('Digite o primeiro cateto: '))
cat2 = int(input('Digite o segundo cateto: '))
hip = cat1**2 + cat2**2
print(hip**(1/2))

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

#EX 05 sorteio ordem de apresentação dos alunos do EX 04
print(random.sample(alunos, k=len(alunos)))

#EX 06 tocar arquivo .mp3
playsound('asd052_03_Brainwave_(Mike-McGuill).mp3')
import random

frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[3:])
print(frase[1:15])
print(frase[::2])
print(frase.upper().count('o'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android')) #Não fica salvo na variável só se frase =
print('Curso' in frase)
print(frase.find('vídeo'))
dividido = frase.split() #cria listas
print(dividido[0] [3]) #primeira palavra letra 4

#Exercícios
#teste:
numero = str(random.randint(100000000, 999999999))
numero = numero[:8] + '-' + numero[8:10]
print(numero)
numero2 = str(random.randint(1000000000, 9999999999))
print(numero2)
numero2 = numero2.replace(numero2[8], '-') #3º é o count
print(numero2)

#Ex1
nome = input('Digite seu nome completo: ').strip()
print(nome.upper())
print(nome.lower())
print("Seu nome tem ", len(nome) - nome.count(' '), ' letras.')
print("Seu primeiro nome tem", nome.find(" "))

#Ex2
milhar = int(input('Digite um número: '))
print(milhar)
u = milhar // 1 % 10
d = milhar // 10 % 10
c = milhar // 100 % 10
m = milhar // 1000 % 10

print('unidade:', u)
print('dezena:', d)
print('centena:', c)
print('milhar:', m)

#Usando o while
while not 0 <= int(entrada := input("Digite um numero de 0 a 9999: ")) < 10000:
    print('Número inválido, tente novamente!')
else:
    entrada = entrada.rjust(4, '0')

milhar, centena, dezena, unidade = entrada
print(entrada)
print(f'{unidade=}, {dezena=}, {centena=}, {milhar=}')

#Ex3 tem Santo no nome?
cidade = input('Digite o nome da sua cidade: ')
print('Santo' in cidade)

#Ex4 tem Silva no nome?
sobrenome = input('Digite o seu nome: ')
print('Silva' in sobrenome)

#Ex5
texto = input("Digite uma frase qualquer: ")
print("A letra a aparece ", texto.upper().count("A"), "vezes.")
print("A primeira letra A está na posição: ", texto.upper().find('A'))
print("A última letra A está na posição: ", texto.rfind('a'))

#Ex6
nomear = input("Digite seu nome: ")
print("Primeiro nome: ", nomear.split()[0])
print("Último nome: ", nomear.split()[-1])
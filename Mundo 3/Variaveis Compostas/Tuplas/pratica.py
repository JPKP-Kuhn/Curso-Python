lanche1 = 'Hámburguer' #Variável simples
lanche = ('Hámburguer', 'Suco', 'Pizza', 'Pudim') #Variavel composta, tupla
print(lanche1)
print(lanche)
#Tuplas não precisam dos parentes e são imutáveis
#lanche[1] = 'Refrigerante' Erro
lanche = 'Hámburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche[1]) #Suco
print(lanche[-2]) #Pizza
print(lanche[1:3]) #Suco e Pizza
print(lanche[2:]) #Pizzaa e Pudim
print(lanche[:2]) #Hámburguer e Suco
print(lanche[1::2]) #Suco e Pudim
for comida in lanche:
    print(f'Vou comer {comida}')
print(len(lanche)) #4
for i in range(0, len(lanche)):
    print(f'Vou comer {lanche[i]} na posição {i}')
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')

print(sorted(lanche)) #Ordena a tupla, não alera, mas cria uma nova, como uma lista

a = (1, 2 , 3)
b =  (5, 6, 7, 8)
c = a + b
print(c) #A ordem importa
print(c.count(5)) #Quantas vezes aparece o 5
print(c.index(6)) #a posição do 6 que é 6, mas começa do 0, usa , para separar e definir de onde começa a contar
pessoa = ('Joao', 25, 'M', 85.4)
del(pessoa) #Apaga a tupla inteira
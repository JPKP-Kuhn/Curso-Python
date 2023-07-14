lanche = ['Hámburguer', 'Suco', 'Pizza', 'Pudim'] # Lista
lanche[3] = 'Picole' # Substitui o valor da posição 3
#Listas são mutáveis
lanche.append('Cookie') # Adiciona um valor no final da lista elemento 4
lanche.insert(0, 'Cachorro Quente') # Adiciona um valor na posição 0
#Refaz a numeração das chaves posteriores ao usar o insert
del lanche[3] # Deleta o valor da posição 3, a pizza
lanche.pop(2) # Deleta o valor da posição 2, o suco, sem índice é o último
print(lanche)
lanche.remove('Cookie') # Deleta o valor 'Cookie'
if 'Pizza' in lanche:
    lanche.remove('Pizza') #Verifica se está antes de remover, pois retorna erro se não estiver

valores = list(range(4, 11)) # Cria uma lista com os valores de 4 a 10, com ao todo 6 índices
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() # Ordena os valores em ordem crescente
valores.sort(reverse=True) # Ordena os valores em ordem decrescente
len(valores) # Mostra o tamanho da lista, no caso 7

#Prática
#num = (2, 5, 9, 1)
#num[2] = 3 # Erro, tuplas são imutáveis
num = [2, 5, 9, 1]
print(num)
num[2] = 3 # Substitui o valor da posição 2, o 9, pelo 3
print(num)
num.append(7) # Adiciona o valor 7 no final da lista
num.sort()
print(num)
num.insert(3, 0) # Adiciona o valor 0 na posição 3
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.pop(0)
print(num)
num.append(2)
num.remove(2) # Remove o primeiro valor 2 da lista
print(num)
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

a = [2, 3, 4, 7]
b = a # Cria uma ligação entre as listas
b[2] = 8 # Altera o valor da posição 2 de ambas as listas
c = a[:] # Cria uma cópia da lista a
c[2] = 4 # Altera o valor da posição 2 apenas da lista c
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')


##Listas compostas

dados = list()
dados.append('Joao')
dados.append(17)
print(dados[0])
print(dados[1])
dados.append('Maria')
dados.append(10)
dados.append('Pedro')
dados.append(12)
pessoas = list()
pessoas.append(dados[:]) # Cria uma cópia da lista dados
print('-='*10)
print(dados)
print(pessoas)
print('-='*10)
print(pessoas[0])
print(pessoas[0][0]) # Mostra o primeiro valor da primeira lista

print('~'*30)
pessoas = [['Joao', 17], ['Maria', 10], ['Pedro', 12]]
print(pessoas[0])
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])

teste = list()
teste.append('Joao')
teste.append(17)
galera = list()
galera.append(teste[:]) # Cria uma cópia da lista teste
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) #Sem [:] cria uma ligação entre as listas
print(teste)
print(galera)

galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])
print(galera[0][0])
print(galera[2][1])

#Sequência de Fibonnaci
fib = [0, 1]
for c in range(0, 8):
    fib.append(fib[c] + fib[c+1])
print(fib)

for p in galera:
    print(p)
    print(p[0])
    print(p[1])
    print(f'{p[0]} tem {p[1]} anos')

galera = list()
dado = list()
for c in range(3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() # Limpa a lista dado
print(galera)

totmai = totmen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')

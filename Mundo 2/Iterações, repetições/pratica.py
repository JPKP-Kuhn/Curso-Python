'''
Repetir um comando, usar um laço de intervalo para não se repetir eternamente
Situação, um boneco quer andar até chegar no bloco para pegar uma maçã que está
a 10 blocos de distância
laço c intervalo(1,10):
    passo
pega

for c in range(1,10):
    passo
pega

Agora haverá moedas no caminho para pegar e buracos para pular -

laço c no intervalo(0,3):
    se moeda:
        pega
    passo
    pula
passo
pega
'''

for i in range(0,3):
    print('OI')
print('Fim')

for i in range(4, 0, -1):
    print("De trás")
    print(i)
print("Fim")

for i in range(0, 9, 2):
    print("Pulando de dois em dois")
print("Fim")

n = int(input("Digite um número para o fim da iteração: "))
for c in range(0, n+1):
    print(c)


i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for i in range(i, f+1, p):
    print(i)
print("Fim")

s = 0
for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s += n
print(f"O somatório de todos os valores foi {s}")
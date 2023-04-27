#Exercícios:
print('Exercícios!')

#1. Sucessor e antecessor
Inteiro = int(input('Digite um número inteiro: '))
print('O número digitado é {} \n Seu sucessor é {} \n e o seu antecessor é {}'.format(Inteiro,Inteiro + 1, Inteiro - 1))
#O antecessor e o sucessor não será guardado pra depois.

#2. dobro, triplo e raiz quadrada
valor = int(input('Digite um valor inteiro: '))
print(' Seu dobro é {}, seu triplo é {} e a sua raiz quadrada é {}'.format(valor * 2, valor * 3, valor ** (1/2)))

#3. Média aritmética
media1 = float(input('Digite uma primeira nota: '))
media2 = float(input('Digite uma segunda nota: '))
nota = (media1 + media2) / 2
print('A sua nota média é: {}'.format(nota))

#4. Conversão, metros, centímetro e milímetros
metro = float(input('Distância em metros: '))
centímetro = metro * 100
milímetro = metro * 1000
decâmetro = metro * 10
kilômetro = metro / 1000
print('Seu valor representa {}m, que também é {}cm e {}mm \n Além disso equivale a {}dm e {}km'.format(metro, centímetro, milímetro, decâmetro, kilômetro ))

#5. Tabuada
tab = int(input('Digite um número inteiro para sua tabuada: '))
tabuada = 0
print('-'*12)
while tabuada <= 10:
    print(f'{tab} x {tabuada:2} = {tab * tabuada}')
    tabuada += 1
print('-'*12)
#melhor do que colocar 10 print

#6. Conversão para dólar
carteira = float(input('Digite um valor que você tem em R$ na carteira: '))
print('Com R${:.2f} você pode comprar U${:.2f} dólares'.format(carteira, carteira / 5.2))   

#7. área
print('Você quer pintar uma parede, 1L de tinta pinta 2m²')
largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
área = largura * altura
tinta = área / 2
print(f'A área da parede tem {área}m² e você precisará de {tinta} litros de tinta para pintar essa parede')

#8. preço com desconto
print('Desncoto de 5% num produto')
preço = float(input('Digite o preço do produto: '))
print('O produto custa {} R$, com 5% de desconto passa a valer {:.2f} R$'.format(preço, preço * 0.95)) #também pode ser 5/100

#9. Aumento de salário
salário = float(input('Digite seu salário: '))
print('Com 15% de aumento, seu salário de {} passa a valer {:.2f}'.format(salário, salário * 1.15))

#10. Conversor de temperaturas ºC pra ºF
c = float(input('A temperatura em ºC é: '))
f = 9 * c / 5 + 32
print('A temperatua de {}ºC é {}ºF'.format(c, f))

#11. Aluguel de carros
dias = int(input('Por quantos dias o carro foi alugado? '))
kmrodados = float(input('Quantos km rodados? '))
total = 60 * dias + 0.15 * kmrodados
print('O total a pagar é {}'.format(total))

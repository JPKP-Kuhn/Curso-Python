import random, time

#Ex5 Jogar pedra papel tesoura
print("Vamos jogar pedra, papel e tesoura")
jogadas_pc = ['pedra', 'papel', 'tesoura']
jogada = random.choice(jogadas_pc)

sua_jogada = input("pedra, papel tesoura: " )
time.sleep(1)
print('-='*10)
time.sleep(1)
print(sua_jogada)
print(jogada)

if sua_jogada.lower() == 'pedra' and jogada == 'tesoura':
    print('Parabéns, você me venceu')
if sua_jogada.lower() == 'pedra' and jogada == 'papel':
    print('Eba, eu venci!')
if sua_jogada.lower() == 'tesoura' and jogada == 'papel':
    print('Parabéns, você me venceu')
if sua_jogada.lower() == 'tesoura' and jogada == 'pedra':
    print('Eba, eu venci!')
if sua_jogada.lower() == 'papel' and jogada == 'pedra':
    print('Parabéns, você me venceu')
if sua_jogada.lower() == 'papel' and jogada == ' tesoura':
    print("Eba, eu venci!")


while (sua_jogada == jogada):
    jogada = random.choice(jogadas_pc)
    sua_jogada = input("Realize uma nova jogada: ")
    time.sleep(1)
    print('-='*10)
    time.sleep(1)
    print(sua_jogada)
    print(jogada)
    if sua_jogada.lower() == 'pedra' and jogada == 'tesoura':
        print('Parabéns, você me venceu')
    if sua_jogada.lower() == 'pedra' and jogada == 'papel':
        print('Eba, eu venci!')
    if sua_jogada.lower() == 'tesoura' and jogada == 'papel':
        print('Parabéns, você me venceu')
    if sua_jogada.lower() == 'tesoura' and jogada == 'pedra':
        print('Eba, eu venci!')
    if sua_jogada.lower() == 'papel' and jogada == 'pedra':
        print('Parabéns, você me venceu')
    if sua_jogada.lower() == 'papel' and jogada == ' tesoura':
        print("Eba, eu venci!")

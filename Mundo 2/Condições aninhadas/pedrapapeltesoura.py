import random, time

#Ex5 Jogar pedra papel tesoura
print("Vamos jogar pedra, papel e tesoura")
jogadas_pc = ['pedra', 'papel', 'tesoura']
jogada = random.choice(jogadas_pc)

sua_jogada = input("pedra, papel tesoura: " )

for i in range(5):
    print('-=',flush=True,end='')
    time.sleep(1)

print(f"\nSua jogada:  {sua_jogada}")
time.sleep(2)
print(f"Jogada do computador: {jogada}")
time.sleep(2)

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
    if( sua_jogada == jogada):
        print("Quem diria! Fizemos a mesma jogada")
    jogada = random.choice(jogadas_pc)
    sua_jogada = input("Realize uma nova jogada: ")
    print(sua_jogada)
    time.sleep(2)
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

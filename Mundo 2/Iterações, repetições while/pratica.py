'''
Usar while pra quando não se sabe o limite, funciona como o for, mas só para
com uma condição específica
'''
for c in range(1, 10):
    print(c)
print('FIM')

i = 1
while(i < 10):
    print(i)
    i += 1
print('FIM')


n = 1
while n != 0: #Condição de parada
    n = int(input("Digite um valor: "))
print("Fim")

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = input('Quer continuar? [S/N] ').upper()
print('Fim')

num = 1
par, impar = 0
while num != 0:
    num = int(input('Digite um número: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Você digitou {par} números pares e {impar} números ímpares")

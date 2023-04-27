#Lembando o desafio 3:
n1 = int(input('Digite um número: ')) #o input funciona com string
n2 = int(input('Digite outro número: '))
print(type(n1))
s = n1 + n2

#print('A soma vale', s)

print('A soma vale {}'.format(s))
#print('A soma entre', n1, 'e', n2, 'vale:', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

#Tipos primitivos no python:
#int, Nº inteiro 7, -4, 0, 9875
#float, Nº Real(com ponto flutuante) 4.5 , 0.076 , -15.223 , 7.0
#bool, True, False
#str, 'olá' , '7.5' . ''
''' + - * / ** //divisor inteiro %
Esses são operadores binários, ou seja, que utilizam dois operandos
'''
5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 == 25
pow(5, 2) == 25 #pow == função interna de potência, mas perde a ordem de precedência
5 // 2 == 2
5 % 2 == 1
81 ** (1/2) == 9 #Raízes
'='*5 == '====='

#Posso escrever a operação direto no .format sem precisar de outra variável
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}, o produto vale {} e a divisão é {:.3f}'.format(n1 + n2, n1 * n2, n1 / n2), end=' ')
print('Divisão inteira {} e potência {}'.format(n1 // n2, n1 ** n2))

#A ordem de procedência é a mesma na matemática
3 + 5 * 2 == 11
3 * 5 + 4 ** 2 == 31
3 * (5 + 4) ** 2 == 243

#Concatenar
'Oi' + 'Olá' == 'OiOlá'
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome)) #:20 faz a variável ocupar 20 caracteres, além disso > alinha a direita, < alinha a esquerda, ^ centraliza.

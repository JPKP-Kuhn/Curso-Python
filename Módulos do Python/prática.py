from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num) #sem import math isso não funciona
print(f'A raiz de {num} é igual a {raiz}') #com ceil daria pra arredondar
# se colocar import math, então coloca-se math.sqrt
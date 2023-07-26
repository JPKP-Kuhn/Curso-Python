#Numeros
from pacote import numeros
#from uteis import* Antes com módulo
#Ou immport uteis, mas teria que usar uteis.nome_da_função

#Modularização ajuda na organização e manutenção do codigo

num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')
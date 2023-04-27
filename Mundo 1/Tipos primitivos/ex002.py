#Ex 3
n1 = float(input('Escreva um número real: '))
n2 = float(input('Ecreva outro número real: '))
print(n1 + n2)

#Ex 4
texto = input('Digite algo (absolutamente qualquer coisa): ') #input só retorna str
print('O tipo primitivo desse valor é:', type(texto))
print('É um número?', texto.isnumeric())
print('É uma letra?', texto.isalpha())
print('É totalmente em maiúsculas', texto.isupper())
print('É todo em minúsculo?', texto.islower())
print('É alfanumérico?', texto.isalnum())
print('Tem espaço?', texto.isspace())
print('Está capitalizada (com letras miúsculas e minúsculas)?', texto.istitle())
#texto é um objeto, o .método() é um método e vem com parentesis
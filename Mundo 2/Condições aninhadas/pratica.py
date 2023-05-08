nome = str(input('Qual é seu nome? '))
if nome.lower() == 'joão' or nome.lower() == 'joao':
    print("Que nome bonito!")
elif nome.lower() == 'pedro' or nome.lower() == 'maria' or nome.lower() == 'paulo':
    print("Seu nome é bem popular no Brasil")
elif nome.lower() in 'ana claudia jessica juliana':
    print("Belo nome feminino")
else:
    print('Seu nome é normal')
print(f'Tenha um bom dia, {nome}!')

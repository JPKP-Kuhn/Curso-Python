#Utilizar índices literais com dicionários
dados = dict() #ou dados = {}
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M' #Adiciona a chave 'sexo' com o valor 'M'
print(dados)
del dados['idade'] #Deleta a chave 'idade'
print(dados)
filme = {'titulo': 'Star Wars',
         'ano': 1977,
        'diretor': 'George Lucas'
}
print(filme.values()) #Mostra os valores
print(filme.keys()) #Mostra as chaves
print(filme.items()) #Mostra os itens

for k, v in filme.items():
    print(f'O {k} é {v}')

filme1 = {'titulo': 'Matrix',
        'ano': 1999,
        'diretor': 'Wachowski'
}
filme2 = {'titulo': 'Avengers',
        'ano': 2012,
        'diretor': 'Joss Whedon'
}
locadora = []
locadora.append(filme)
locadora.append(filme1)
locadora.append(filme2)
print(locadora[0]['ano']) #Mostra o ano do filme 0
print(locadora[2]['titulo']) #Mostra o título do filme 2

pessoas = {'nome': 'Joao', 
           'sexo': 'M',
           'idade': 17}
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
print('-='*30)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
pessoas['peso'] = 85.4
pessoas['nome'] = 'Maria'
for k, v in pessoas.items():
    print(f'{k} = {v}')

estado = {'uf': 'Santa Catarina',
          'sigla': 'SC'
}
estado1 = {'uf': 'Rio Grande do Sul',
           'sigla': 'RS'
}
brasil = []
brasil.append(estado)
brasil.append(estado1)
print(brasil)
print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range(3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado:')
    brasil.append(estado.copy()) #Copia o dicionário estado para a lista brasil
print(brasil)
for i in brasil:
    for k, v in i.items():
        print(f'O campo {k} tem valor {v}')

for i in brasil:
    for v in i.values():
        print(v, end=' ')
    print()



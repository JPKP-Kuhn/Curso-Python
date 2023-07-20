#Ex1 informações de aluno

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

#Ex2 jogar dados, ordernar um dicionário e mostrar o ranking
from random import randint
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f' {k} tirou {v} no dado.')
print('Ranking dos jogadores:')
for k, v in enumerate(sorted(jogadores, key=jogadores.get, reverse=True)):
    print(f' {k+1}º lugar: {v} com {jogadores[v]}')

#Ex3 cadastro de pessoa e carteira de trabalho
from datetime import datetime
pessoa = {'nome': input('Nome: '),
          'idade': datetime.now().year - int(input('Ano de nascimento: ')),
          'ctps': int(input('Carteira de Trabalho (0 não tem): '))}
if pessoa['ctps'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['idade'] + ((pessoa['Ano de contratação'] + 35) - datetime.now().year)
print('-='*30)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')

#Ex4 aproveitamento de jogador de futebol
jogador = {'nome': input('Nome do jogador: '),
           'gols': [],
           'total': 0}
jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
for i in range(jogos):
    jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogador['total'] += jogador['gols'][i]
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas.')
print(jogador['gols'])
for i in enumerate(jogador['gols']):
    print(f'    => Na partida {i[0]+1}, fez {i[1]} gols.')

#Ex5 grupo de pessoas
pessoa = dict()
grupo = list()
mulheres = list()
acimamedia = list()
soma = media = 0
resp = 'S'
while resp == 'S':
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa.copy())
    grupo.append(pessoa.copy())
    resp = input('Quer continuar? [S/N] ').upper()[0]
media = soma / len(grupo)
print('-='*30)
print(f'Foram cadastradas {len(grupo)} pessoas.')
print(f'A média de idade do grupe é de {media:.2f} anos.')
print(mulheres)
print(f'As pessoas com idade acima da média são: ')
for i in grupo:
    if i['idade'] > media:
        print(f'    => {i["nome"]} com {i["idade"]} anos.')

#Ex6 vários jogadores de futebol
jogador = dict()
time = list()
resp = 'S'
while resp == 'S':
    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    jogador['total'] = 0
    for i in range(partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
        jogador['total'] += jogador['gols'][i]
    time.append(jogador.copy())
    resp = input('Quer continuar? [S/N] ').upper()[0]
print('-='*30)
print('cod nome    gols   total')
for v, i in enumerate(time):
    print(f'{v} {i["nome"]:<10}{str(i["gols"]):<10}{i["total"]:<10}')

while True:
    c = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if c == 999: break
    if c >= len(time):
        print(f'ERRO! Não existe jogador com código {c}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[c]["nome"]}:')
        for i in time[c]['gols']:
            print(f' No jogo {time[c]["gols"].index(i)+1} fez {i} gols.')


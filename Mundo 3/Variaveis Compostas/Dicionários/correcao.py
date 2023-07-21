#Ex1
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')

#Ex2
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f' {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

#Ex3
from datetime import datetime
dados = dict()
dados['nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário']  = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')

#Ex4
jogador = dict()
partidas = list()
jogador['nome'] = input('Nome do jogador: ')
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador)} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

#Ex5
pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'S':
        break
print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

#Ex6
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-'*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:^3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*30)
while True:
    bus = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if bus == 999:
        break
    if bus >= len(time):
        print(f'ERRO! Não existe jogador com código {bus}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[bus]["nome"]}:')
        for i, g in enumerate(time[bus]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*30)
print('<< VOLTE SEMPRE >>')
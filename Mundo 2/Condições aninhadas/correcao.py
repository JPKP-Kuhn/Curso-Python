from datetime import date

#Ex1
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Qantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30/100
print('Para pagar uma casa  de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao, minimo))
if prestacao <= minimo:
    print('Empréstimo pode ser concedido')
else:
    print('Empréstimo negado')

#Ex2
num = int(input('Digite um número inteiro: '))
print('''Escolha das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
match opcao:
        case 1:
            print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
        case 2:
            print('{} convertido para OCATAL é igual a {}'.format(num, oct(num)[2:]))
        case 3:
            print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

#Ex3
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')

#Ex4
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade 
    print('Faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {} ano'.format(ano))

#Ex5
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('O aluno está em recuperação.')
elif media < 5:
    print('O aluno está reprovado')
else:
    print('Aluno aprovado')

#Ex6
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade < 9:
    print('Classificação: MIRIM')
elif idade <=14:
    print('Classificaçõa: INFANTIL')
elif idade <=19:
    print('Classificaçõa: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

#Ex7
n1 = int(input("a: "))
n2 = int(input("b: "))
n3 = int(input("c: "))
if n1 < n2 + n3 and n1 > n2 - n3:
    print("Parabéns, você tem um triângulo ",end='')
    if n1 == n2 == n3:
        print('Equilátero')
    elif n1 != n2 != n3 != n1:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Os segmentos não podem formar um triângulo')

#Ex8
peso = float(input('Qual é seu peso?(kg) '))
altura = float(input('Qual é a sua altura?(m) '))
imc = peso / altura ** 2
print(f'O imc dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('Você está na faixa de peso normal')
elif 25 <= imc < 30:
    print('Você está em sobrepeso')
elif 30 <= imc < 40:
    print('Você está em obesidade, cuidado')
elif imc >= 40:
    print('Você está em obesidade mórbida!')

#Ex9
print('{:-=40}'.format(' LOJAS KUHN '))
preco = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção? '))
if opcao == 1:
    total = preco  - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totparc, parcela))
else:
    print('Opção inválida de pagamento, tente novamnete')
    total = preco
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))

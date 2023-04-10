#coding: utf-8
import contaBancaria as cB
import chequeEspecial as cE

if __name__ == "__main__":
    #conta = cB.contaBancaria() Herança
    cheque = cE.chequeEspecial()

    print('Vamos abrir sua conta bancária!')
    nome = input('\nEntre com seu nome completo: ')
    renda = float(input('\n Informe sua renda mensal: '))

    cheque._set_correntista(nome, 0)
    cheque._set_renda(renda)

    correntista_info = cheque._get_correntista()

    print(f'Seja bem vindo {correntista_info["Nome"]}! A data de criação da sua conta é {correntista_info["Data de abertura"]}')

    print(f'Seu número da conta é {correntista_info["Numero Conta"]}')
    print(f'Seu saldo atual é {cheque._get_saldo()}' )

    while True:
        chamada = input('O que você deseja fazer? \nVer dados do correntista(1), Fazer Depósito(2), Fazer Saque(3), Ver Histórico de Extrato(4), Ver saldo Médio(5) Fechar(6): ')
        if(chamada == '1'):
            correntista_info = cheque._get_correntista()
            saldo = cheque._get_saldo()
            print(correntista_info, f'Saldo: {saldo}')
            print(f'Sua renda mensal é: {renda}')
            print(f'Seu limite de cheque especial é {cheque._get_limite()}')

        if(chamada == '2'):
            valor = float(input('Qual o valor que você quer depositar: ').replace(',', '.'))
            deposito = cheque.deposito(valor)
            print(f'Seu saldo agora é: {deposito:.2f}')

        if(chamada == '3'):
            valor = float(input('Qual valor você quer sacar: ').replace(',', '.'))
            saque = cheque.retirada(valor)
            print(f'Seu saldo agora é {saque:.2f}')

        if(chamada == '4'):
            extrato = cheque._get_extrato()
            print(extrato)

        if(chamada == '5'):
            periodo = int(input('Digite até que dia você quer ver: '))
            print(f'Saldo Médio é: {cheque._set_saldo_medio(periodo)}')

        if(chamada == '6'):
            break

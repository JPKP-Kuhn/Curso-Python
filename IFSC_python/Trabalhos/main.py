#coding: utf-8
import contaBancaria as cB

if __name__ == "__main__":
    conta = cB.contaBancaria()
    print('Vamos abrir sua conta bancária!')
    nome = input('\nEntre com seu nome completo: ')
    conta._set_correntista(nome, 0)
    correntista_info = conta._get_correntista()

    print(f'Seja bem vindo {correntista_info["Nome"]}! A data de criação da sua conta é {correntista_info["Data de abertura"]}')

    print(f'Seu número da conta é {correntista_info["Numero Conta"]}')
    print(f'Seu saldo atual é {conta._get_saldo()}' )

    while True:
        chamada = input('O que você deseja fazer? \nVer dados do correntista(1), Fazer Depósito(2), Fazer Saque(3), Ver Histórico de Extrato(4): ')
        if(chamada == '1'):
            correntista_info = conta._get_correntista()
            saldo = conta._get_saldo()
            print(correntista_info, f'Saldo: {saldo}')

        if(chamada == '2'):
            valor = float(input('Qual o valor que você quer depositar: ').replace(',', '.'))
            deposito = conta.deposito(valor)
            print(f'Seu saldo agora é: {deposito:.2f}')

        if(chamada == '3'):
            valor = float(input('Qual valor você quer sacar: ').replace(',', '.'))
            saque = conta.retirada(valor)
            print(f'Seu saldo agora é {saque:.2f}')

        if(chamada == '4'):
            extrato = conta._get_extrato()
            print(extrato)

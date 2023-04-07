#coding: utf-8
import contaBancaria as cB

if __name__ == "__main__":
    conta = cB.contaBancaria()
    print('Vamos abrir sua conta bancária!')
    nome = input('\nEntre com seu nome completo: ')
    conta._set_correntista(nome, 0)
    correntista_info = conta._get_correntista()
    print(f'Seja bem vindo {correntista_info["Nome"]}! Seu saldo é {correntista_info["Saldo"]}. A data de criação da sua conta é {correntista_info["Data de abertura"]}')
    print(f'Seu número da conta é {correntista_info["Numero Conta"]}')
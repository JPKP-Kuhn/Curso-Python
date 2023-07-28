#Ex1 função leiaInt

def leiaInt(msg):
    ok = True
    while ok:
        try:
            num = int(input(msg))
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        else:
            ok = False
            return num
        
def leiaFloat(msg):
    ok = True
    while ok:
        try:
            num = float(input(msg))
        except:
            print('\033[0;31mERRO! Digite um número real válido!\033[m')
        else:
            ok = False
            return num

num = leiaInt('Digite um número: ')
real = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número {num} e {real}')

#Ex2 Acessando o site pudim
import webbrowser
webbrowser.open('http://pudim.com.br/')
webbrowser.open_new_tab('https://lichess.org/')

#Ex3 sistema modularizado



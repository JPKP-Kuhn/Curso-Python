#Ex1 função leiaInt

def leiaInt(msg):
    #ok = True
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO! O usuário não informou os dados!\033[m')
            return 0
        else:
            #ok = False
            return num
        
def leiaFloat(msg):
    #ok = True
    while True:
        try:
            num = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO! O usuário não informou os dados!\033[m')
            return 0
        else:
            #ok = False
            return num

num = leiaInt('Digite um número: ')
real = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número {num} e {real}')

#Ex2 Acessando o site pudim
import webbrowser, urllib, urllib.request
webbrowser.open('http://pudim.com.br/')
webbrowser.open_new_tab('https://lichess.org/')

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())


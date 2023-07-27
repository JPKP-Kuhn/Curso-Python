#Erros de sintaxe
# SyntaxError: invalid syntax 
while True: #precisa ter essa organização
    print('Hello world')
    break
#primt('Olá, Mundo!')
#print(x) x is not defined NameError exceção
#Erros de semântica
print('Olá' * 5)
# print(7 + '4')
TypeError #can only concatenate str (not "int") to str
ZeroDivisionError #division by zero
ValueError  #invalid literal for int() with base 10: 'a'
TypeError #unsupported operand type(s) for +: 'int' and 'str' 2 + '2'
lst = [1, 2, 3]
# print(lst[3]) IndexError: list index out of range key error
#import uteis 
ModuleNotFoundError #No module named 'uteis'

#Tratamento de erros e exceções
try: #Tentar
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: #Se der erro, pode ter vários except pra cada exceção que eu quiser
    print(f'Problema encontrado foi {erro.__class__}')
else: #Se não der erro
    print(f'O resultado é {r:.1f}')
finally: #Sempre independente se certo ou erro
    print('Volte sempre! Muito obrigado!')

###################################
print('=-'*30)
try: #Tentar
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): #Se der erro, pode ter vários except pra cada exceção que eu quiser
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError: #Se der erro, pode ter vários except pra cada exceção que eu quiser
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt: 
    print('O usuário preferiu não informar os dados!')
except Exception as erro: 
    print(f'O erro encontrado foi {erro.__cause__}')
else: #Se não der erro
    print(f'O resultado é {r:.1f}')
finally: #Sempre independente se certo ou erro
    print('Volte sempre! Muito obrigado!')
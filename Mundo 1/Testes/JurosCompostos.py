#Cálculo de Juros composotos

# M = C*(1+i)**t Fórmula do Juros Composto
# J = M -C Fórmula do valor do Juros

C = float(input('Valor do capital: '))
i = float(input('Taxa: '))
t = float(input('Tempo: ')) #decimal    

M = C*(1+i)**t
print(M)
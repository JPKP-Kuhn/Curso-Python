from Pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)

#p1.nome = 'Luiz'
#p2.nome = 'João'
print(p1.nome)
print(p2.nome)
p1.falar('saudações') #como se o argumento self fosse p1
p2.falar('agradecimentos') #como se o argumento self fosse p2
p1.anos()
p1.comer('Maçã')
p1.comer('Maçã') #já está comendo
p1.parar_comer()
p1.parar_comer() #não está comendo

p1.falar('Python')
p1.parar_comer()

p1.falar('Python')
p1.parar_falar()

p2.comer('Pão')
p2.falar('Python')

print(Pessoa.ano_atual)

print(p1.get_anos_nascimento())

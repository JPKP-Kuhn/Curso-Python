import pandas as pd

#dataframe = pd.DataFrame() cria uma tabela de dados vazia

venda = {'data': ['15/02/2021', '16/02/2021'], 
         'valor': [100, 200],
         'produto': ['feijao', 'arroz'],
         'quantidade': [50, 70]}

venda_df = pd.DataFrame(venda) #df só pra dizer que é uma tabela de dados
print(venda_df)
print()
vendas_df = pd.read_excel("Vendas.xlsx") #sep é o separador de colunas
#print(vendas_df)

#Visualização de dados simples
print(vendas_df.head(6)) #mostra as 6 primeiras linhas
print(vendas_df.tail()) #mostra as 5 ultimas linhas
print(vendas_df.dtypes) #mostra os tipos de dados de cada coluna

print(vendas_df.shape) #mostra a quantidade de linhas e colunas
print(vendas_df.describe()) #mostra dados estatisticos da tabela

produto = vendas_df['Produto'] #seleciona uma coluna, é uma serie, não um dataframe
print(produto)

#dataframe é um atabela em que cada columa é uma série
produto = vendas_df[['Produto', 'ID Loja']]
print(produto) #Com duas series vira um dataframe

#pegar uma linha
print('Primeira linha: ', vendas_df.loc[0]) #loc é para localizar, pega a linha 0
print(vendas_df.loc[1:3]) #pega as linhas de 1 a 3

#pegar linhas que correspondem a uma condição
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping'] #pega as linhas que tem ID Loja = Norte Shopping

#pegar várias linhas e colunas usando loc[linhas, colunas]
print(vendas_df.loc[vendas_norteshopping_df.index, ['ID Loja', 'Produto', 'Quantidade']])

#pegar um valor específico
print(vendas_df.loc[1, 'Produto']) #pega o produto da linha 1

#Adicionar uma coluna
#a partir de uma coluna existente
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
print(vendas_df.head())

vendas_dez_df = pd.read_excel("Vendas - Dez.xlsx")

#concatena vendas_dez_df no vendas_df
vendas_df = pd.concat([vendas_df, vendas_dez_df], ignore_index=True) #concatena as linhas, se tiverem as mesmas colunas
#A coluna que tinha sido criada antes vai tá vizia pro vendas_dez_df

print(vendas_df.tail())

vendas_df = vendas_df.drop('Comissão', axis=1) #apaga a coluna Comissão
print(vendas_df.tail())
vendas_df = vendas_df.drop(0, axis=0) #apaga a linha 0
print(vendas_df.head())

#deletar linhas e colunas com base em condições
vendas_df = vendas_df.dropna(how='all', axis=1) #apaga as colunas que estão todas vazias

#deletar linhas que possuem pelo menos um valor vazio
vendas_df = vendas_df.dropna()

#preencher com valores vazios
vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean()) #preenche com a média dos valores da coluna Comissão

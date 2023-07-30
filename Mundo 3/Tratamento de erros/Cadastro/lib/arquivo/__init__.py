from Cadastro.lib.interface import *

endereco = '/home/joaopedrokuhn/Área de Trabalho/Estudo/Cursos-online/Curso-Python/Mundo 3/Tratamento de erros/'

def arquivoExiste(arq):
    try:
        a = open(f'{endereco}{arq}', 'rt') # rt = read text
        a.close()
    except FileNotFoundError:
        return False

    else:
        return True
    
def criarArquivo(arq):

    try:
        a = open(f'{endereco}{arq}', 'wt+') # wt+ = write text, if not exist create
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {arq} criado com sucesso!')

def lerArquivo(arq):
    try:
        a = open(f'{endereco}{arq}', 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(f'{endereco}{arq}', 'at') # at = append text
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
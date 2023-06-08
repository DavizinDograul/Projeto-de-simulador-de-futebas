import os
import random
import numpy as np

# acessa as pastas que contém os arquivos de nomes e sobrenomes
def acessa_pasta(nome_pasta):
    conteudos = {}  # dicionário para armazenar os conteúdos dos arquivos
    caminho_pasta = os.path.abspath(nome_pasta)  # obtém o caminho absoluto da pasta a partir do nome
    
    for nome_arquivo in os.listdir(caminho_pasta):  # para cada arquivo na pasta
        
        # obtém o caminho absoluto do arquivo
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
        
        # abre o arquivo
        with open(caminho_arquivo, encoding='utf-8') as arquivo:
            
            # obtém o conteúdo do arquivo
            conteudo = arquivo.read()
            
            # separa o conteúdo por "," e salva como uma lista
            lista_separada = conteudo.split(', ')
            
            # salva a lista como valor de um dicionário que tem como chave o nome do arquivo (sem a extensão)
            conteudos.setdefault(os.path.splitext(nome_arquivo)[0], lista_separada)

    return conteudos

modelo = {
    'nome' : '',
    'idade' : 0,
    'posição' : '',
    'altura' : 0,
    'Habilidades' : {
    'Velocidade': 0, 'Aceleração': 0, 'Agilidade': 0,
    'Cabeceio': 0, 'Finalização': 0, 'Chute de Longe': 0,
    'Marcação': 0, 'Bote': 0, 'Carrinho': 0,
    'Passe curto': 0, 'Lançamento': 0, 'Visão': 0,
    'Força': 0, 'Fôlego': 0, 'Impulsão': 0,
    'Posicionamento': 0, 'Controle corporal': 0,
    'Controle bola' : 0, 'Drible' : 0}
    
}


# dicionário com os nomes dos países e suas respectivas siglas
nomes = {'Brasil': 'BRA', 'Argentina': 'ARG', 'Chile': 'CHI', 'Colômbia': 'COL', 'Equador': 'EQU', 'Paraguai': 'PAR', 'Peru': 'PER', 'Uruguai': 'URU', 'Venezuela': 'VEN'}

# dicionário com as posições dos jogadores e seus respectivos números
posicoes = {'Goleiro': 1, 'Zagueiro': 2, 'Lateral': 3, 'Meio-Campo': 4, 'Atacante': 5}

# lista com as posições e seus respectivos números de jogadores na formação 4-3-3
posi_nu = [('Goleiro', 1), ('Zagueiro', 2), ('Zagueiro', 2), ('Lateral', 3), ('Lateral', 3), ('Meio-Campo', 4), ('Meio-Campo', 4), ('Meio-Campo', 4), ('Atacante', 5), ('Atacante', 5), ('Atacante', 5)]

# leitura dos arquivos com os nomes e sobrenomes
def acessa_pasta(nome_pasta):
    # dicionario onde ficara o conteudo dos arquivos
    conteudos = {}
    #
    #obtem o caminho absoluto da pasta a partir do nome
    caminho_pasta = os.path.abspath(nome_pasta)

    #para cada arquivo na pasta
    for nome_arquivo in os.listdir(caminho_pasta):

        #obter o caminho e gerar o caminho absoluto
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

        #abrir o arquivo
        with open(caminho_arquivo, encoding='utf-8') as arquivo:

            #obter o conteudo da arquivo
            conteudo = arquivo.read()

            #separa o conteudo por "," e salva como uma list
            lista_separada = conteudo.split(', ')

            #salva a list como valor  de um dicionario que tem como chave o nome do arquivo
            conteudos.setdefault(os.path.splitext(nome_arquivo)[0], lista_separada)

    return conteudos


# acesso aos arquivos com os nomes e sobrenomes dos jogadores
nomes = acessa_pasta('./nomes')
sobrenomes = acessa_pasta('./sobrenomes')

#gerador de nome aleatório a partir de um dicionario
def gerador_aleatorio_nome(pais):
    r1 = random.randint(0, 49)
    r2 = random.randint(0, 49)

    return f"{nomes[pais][r1]} {sobrenomes[pais][r2]}"

#gerador de habilidades aleatórias
def gerador_hab():
    habili = modelo['Habilidades']
    r1 = numero_aleatorio(65)
    for hab in habili:
        habili[hab] = numero_aleatorio(r1)

    return habili

#gerador de habilidades para um jogador
def criar_hab(g, pee):
    hab = {}
    for key in modelo['Habilidades'].keys():
        if key == 'CHU' or key == 'DES':
            hab[key] = round(numero_aleatorio(g+10), 0)
        elif key == 'VELOCIDADE':
            if pee == 'GOL':
                hab[key] = round(numero_aleatorio(g-10), 0)
            else:
                hab[key] = round(numero_aleatorio(g+10), 0)
        else:
            hab[key] = round(numero_aleatorio(g), 0)
    return hab

jogadores = []
    
def numero_aleatorio(media):
    desvio_padrao = 10
    while True:
        numero = np.random.normal(media, desvio_padrao)
        if 40 <= numero <= 100:
            return round(numero, 0)
        
def ciclo():      
    while True:
        comando = input('Insira comando: ')

        if comando == 'mostrar jogadores':
            print(jogadores)
        elif comando == 'criar':
                pais = input(f'Selecione o país do jogador criado (opções: {nomes.keys()}): ')
                jogador = criar_jogador(pais, numero_aleatorio(70))
                jogadores.append(jogador)
        elif comando == 'sair':
            break
        else:
            print('Comando inválido.')
            
ciclo()

def gerador_posicao (r):
    return posicoes[r]

def criar_jogador (Pais, g):
    jogador = modelo.copy()
    jogador['nome'] = gerador_aleatorio_nome(Pais)
    jogador['idade'] = random.randint(16, 40)
    
    r1 = random.randint(0, 7)
    
    jogador['posição'] = gerador_posicao(r1)
    jogador['altura'] = random.randint(155, 200)
    
    pee, *r = posi_nu[r1]
    
    jogador['Habilidades'] = criar_hab(g, pee)
    
    return jogador
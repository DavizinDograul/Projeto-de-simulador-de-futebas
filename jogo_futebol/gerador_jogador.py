import os
import random


def acessa_pasta (nome_pasta):
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
            lista_separada = list(set(conteudo.split(', ')))
            
            #salva a list como valor  de um dicionario que tem como chave o nome do arquivo
            conteudos.setdefault(os.path.splitext(nome_arquivo)[0], lista_separada)
#            conteudos.setdefault(, lista_separada)

    return conteudos
            
      

nomes = acessa_pasta('./nomes')
sobrenomes = acessa_pasta('./sobrenomes')

#gerador de nome aleatório a partir de um dicionario
def gerador_aleatorio_nome (pais):
    r1 = random.randint(0, 49)
    r2 = random.randint(0, 49)

    return f"{random.choice(nomes[pais])} {random.choice(sobrenomes[pais])}"

print(gerador_aleatorio_nome('finlandia'))
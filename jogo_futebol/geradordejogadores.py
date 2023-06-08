import os

def acessa_txt (nome_arq):
    caminho  = os.path.abspath(nome_arq)
    texto = open(caminho)
    print(texto)
    conteudo = texto.read()

    return conteudo.split(", ")

nomes_italianos = acessa_txt('nomes/italianomes.txt')

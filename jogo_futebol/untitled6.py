import random
"""
Created on Wed Jun  7 22:28:16 2023

@author: david
"""


class país:
    def __init__(self, nome_pais, pais_proximo1, pais_proximo2, pais_proximo3, pais_proximo4):
        self.nome = nome_pais
        self.proximo = pais_proximo1
        self.proximo2 = pais_proximo2
        self.proximo3 = pais_proximo3
        self.proximo4 = pais_proximo4



finlandia = país('finlandia', 'noruega', 'dinamarca', 'holanda', 'inglaterra')

def escolha_nacionalidade(p):
    n_de_possibilidade = 0
    
    pais_principal = [p.nome, 15]
    escolha1 = [p.proximo, 20]
    escolha2 = [p.proximo2, 25]
    escolha3 = [p.proximo3, 27]
    escolha4 = [p.proximo4, 29]
    
    n_ale = random.choice(range(1, 30))
    
    if n_ale <= 15:
        return pais_principal
    elif n_ale <= 20:
        return escolha1
    elif n_ale <= 25:
        return escolha2
    elif n_ale <= 27:
        return escolha3
    elif n_ale <= 29:
        return escolha4


        
print(escolha_nacionalidade(finlandia))        
        
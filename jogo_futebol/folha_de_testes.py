# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 12:17:24 2023

@author: david
"""

def habilidades_para_geral(mo):
    habilidades = mo.copy()
    geral_atual = 80
    geral_desejado = 85

    while abs(geral_atual - geral_desejado) > 0.1:  # critério de parada
        habilidades['Aceleração'] = random.uniform(0, 100)
        habilidades['Velocidade'] = random.uniform(0, 100)
        habilidades['Agilidade'] = random.uniform(0, 100)
        habilidades['Cabeceio'] = random.uniform(0, 100)
        habilidades['Finalização'] = random.uniform(0, 100)
        habilidades['Chute de Longe'] = random.uniform(0, 100)
        habilidades['Marcação'] = random.uniform(0, 100)
        habilidades['Bote'] = random.uniform(0, 100)
        habilidades['Carrinho'] = random.uniform(0, 100)
        habilidades['Passe curto'] = random.uniform(0, 100)
        habilidades['Lançamento'] = random.uniform(0, 100)
        habilidades['Visão'] = random.uniform(0, 100)
        habilidades['Força'] = random.uniform(0, 100)
        habilidades['Fôlego'] = random.uniform(0, 100)
        habilidades['Impulsão'] = random.uniform(0, 100)
        habilidades['Posicionamento'] = random.uniform(0, 100)
        habilidades['Controle corporal'] = random.uniform(0, 100)
        
        print(habilidades['Controle corporal'])

        geral_atual = ld(habilidades)
        
def ger_posicao (n, altu, peso):
    
    posi = list(range(len(posicoes)))
    
    if  altu < 1.70:
        posicoes[0] = 10 #ld
        posicoes[1] = 0 #zag
        posicoes[2] = 20 #le
        posicoes[3] = 30 #ald
        posicoes[4] = 32 #vol
        posicoes[5] = 42 #ale
        posicoes[6] = 52 #md
        posicoes[7] = 57 #mc
        posicoes[8] = 67 #me
        posicoes[9] = 76 #ma
        posicoes[10] = 86 #pd
        posicoes[11] = 88 #sa
        posicoes[12] = 98 #pe
        posicoes[13] = 100 #ata
    elif altu < 1.75:
        posicoes[0] = 8 #ld
        posicoes[1] = 0 #zag
        posicoes[2] = 16 #le
        posicoes[3] = 24 #ald
        posicoes[4] = 30 #vol
        posicoes[5] = 38 #ale
        posicoes[6] = 47 #md
        posicoes[7] = 55 #mc
        posicoes[8] =  #me
        posicoes[9] = 67 #ma
        posicoes[10] = 74 #pd
        posicoes[11] = 80 #sa
        posicoes[12] = 89 #pe
        posicoes[13] = 88 #ata
        
        
    return posicoes[n]
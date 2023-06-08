# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 12:44:35 2023

@author: david
"""

"""for jogador_ in jogadores:
    #salva o atributo "posição" do jogador q esta sendo iterado
    posicao_j = jogador_.posicao
    #acessa o peso usado para calcular os atributos do jogador usando a posição
    #como chave de acesso
    peso_posicao = posi_nu[posicao_j]
    #salva o atributo "habilidades" do "jogador_" iterado
    habilidades_i = jogador_.habilidades
    print(habilidades_i)
    
    
    #soma dos pesos de cada uma das habilidases
    soma_pesos_habili = 0
    #soma do produto da multiplicação dos pesos pelos valores da propriedade habilidades 
    soma_produto_mult = 0
    
    for hab, peso in peso_posicao.items():
        soma_pesos_habili += peso
        soma_produto_mult += peso * habilidades_i[hab]
        
    print(soma_produto_mult / soma_pesos_habili)"""
        
'''Jogadores_pos_MCs = []
papa  = []

for jogador in jogadores:
    if jogador.posicao == 'MC':
        Jogadores_pos_MCs.append([jogador.classificacao_geral, jogador.codigo])
        
        
Jogadores_pos_MCs

maiores = sorted(Jogadores_pos_MCs, reverse= True)

for overall, cod in maiores:
    for jo in jogadores:
        if jo.codigo == cod:
            print(vars(jo))'''
            
''' # gera um ciclo de de criação de jogadores       
def ciclo():      
    while True:
        comando = input('Insira comando: ')

        if comando == 'mostrar jogadores':
            print(jogadores)
        elif comando == 'criar':
            pais = input(f'Selecione o país do jogador criado (opções: {nomes.keys()}): ')
            for i in range(40):
                
                jogador = criar_jogador(pais, numero_aleatorio(75))

                jogadores.append(jogador)
        elif comando == 'sair':
            break
        elif comando == 'mostrar jogadores por times':
            mt = input('Qual time:')
            for j in jogadores:
                if j['time'] == mt:
                    print(j)
        
        
        else:
            print('Comando inválido.')'''

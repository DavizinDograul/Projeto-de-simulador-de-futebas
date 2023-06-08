# -*- coding: utf-8 -*-
import numpy as np
import random 

def numero_aleatorio(media):
    desvio_padrao = 10
    
    while True:
        numero = np.random.normal(media, desvio_padrao)
        if 40 <= numero <= 100:
            return round(numero, 0)

#            1     2      3     4      5      6      7     8     9    10    11   12    13    14
posicoes= ['LD', 'ZAG', 'LE', "VOL", 'ALD', 'ALE', 'MD', 'MC', 'ME', 'MA', 'PE','SA', 'PD', 'ATA']
modelo = {
    'nome' : '',
    'idade' : 0,
    'posição' : '',
    'altura' : 0,
    'time' : '',
    'Habilidades' : {
    'Velocidade': 0, 'Aceleração': 0, 'Agilidade': 0,
    'Cabeceio': 0, 'Finalização': 0, 'Chute de Longe': 0,
    'Marcação': 0, 'Bote': 0, 'Carrinho': 0,
    'Passe curto': 0, 'Lançamento': 0, 'Visão': 0,
    'Força': 0, 'Fôlego': 0, 'Impulsão': 0,
    'Posicionamento': 0, 'Controle corporal': 0,
    'Controle bola' : 0, 'Drible' : 0}
    
}

'''desenvolvimento = {
    17 : 85, 67,
    18 : 86, 69
    19 : 88, 73
    20 : 91,75
    21 : 91,77
    22 : 92,82
    23 : 93,83
    24 : 94,87
    25 : 94,88
    26 : 93,88
    27 : 92,89
    28 : 91,90
    29 : 91,90
    30 : 89,89
    31 : 88,88
    32 : 86,88
    33: 85,87
    34 : 82,85
    35 : 79,81
    36 : 78,77
    37 : 77, 75
    
    }'''

pesos_ld = {
    'Aceleração': 6,
    'Velocidade': 6,
    'Agilidade': 3,
    'Cabeceio': 2,
    'Finalização': 1,
    'Chute de Longe': 1,
    'Marcação': 6,
    'Bote': 6,
    'Carrinho': 5,
    'Passe curto': 4,
    'Lançamento': 3,
    'Visão': 3,
    'Força': 3,
    'Fôlego': 6,
    'Impulsão': 2,
    'Posicionamento': 2,
    'Controle corporal': 4,
    'Controle bola': 4,
    'Drible': 3
}

pesos_zg = {
    'Aceleração': 3,
    'Velocidade': 3,
    'Agilidade': 1,
    'Cabeceio': 6,
    'Finalização': 1,
    'Chute de Longe': 1,
    'Marcação': 6,
    'Bote': 6,
    'Carrinho': 6,
    'Passe curto': 4,
    'Lançamento': 3,
    'Visão': 2,
    'Força': 6,
    'Fôlego': 5,
    'Impulsão': 5 ,
    'Posicionamento': 1,
    'Controle corporal': 6,
    'Controle bola': 4,
    'Drible': 1
}

pesos_vol = {
    'Aceleração': 3,
    'Velocidade': 3,
    'Agilidade': 1,
    'Cabeceio': 5,
    'Finalização': 1,
    'Chute de Longe': 2,
    'Marcação': 6,
    'Bote': 5,
    'Carrinho': 4,
    'Passe curto': 5,
    'Lançamento': 4,
    'Visão': 3,
    'Força': 6,
    'Fôlego': 5,
    'Impulsão': 3,
    'Posicionamento': 2,
    'Controle corporal': 6,
    'Controle bola': 4,
    'Drible': 1
}

pesos_ma = {
    'Aceleração': 5,
    'Velocidade': 5,
    'Agilidade': 5,
    'Cabeceio': 2,
    'Finalização': 4,
    'Chute de Longe': 4,
    'Marcação': 1,
    'Bote': 0.7,
    'Carrinho': 0.6,
    'Passe curto':6,
    'Lançamento': 4,
    'Visão': 5,
    'Força': 2,
    'Fôlego': 4,
    'Impulsão': 2,
    'Posicionamento': 5,
    'Controle corporal': 2,
    'Controle bola': 6,
    'Drible': 6
}

pesos_sa = {
    'Aceleração': 5,
    'Velocidade': 5,
    'Agilidade': 5,
    'Cabeceio': 3,
    'Finalização': 6,
    'Chute de Longe': 5,
    'Marcação': 0.5,
    'Bote': 0.5,
    'Carrinho': 0.5,
    'Passe curto': 5,
    'Lançamento': 2,
    'Visão': 5,
    'Força': 2,
    'Fôlego': 3,
    'Impulsão': 2,
    'Posicionamento': 6,
    'Controle corporal': 1,
    'Controle bola': 6,
    'Drible': 6
}

pesos_ata = {
    'Aceleração': 4,
    'Velocidade': 4,
    'Agilidade': 4,
    'Cabeceio': 5,
    'Finalização': 6,
    'Chute de Longe': 5,
    'Marcação': 0.5,
    'Bote': 0.5,
    'Carrinho': 0.5,
    'Passe curto': 3,
    'Lançamento': 1,
    'Visão': 3,
    'Força': 5,
    'Fôlego': 3,
    'Impulsão': 5,
    'Posicionamento': 6,
    'Controle corporal': 1,
    'Controle bola': 5,
    'Drible': 4
}



pesos_ponta = {
    'Aceleração': 6,
    'Velocidade': 6,
    'Agilidade': 5,
    'Cabeceio': 2,
    'Finalização': 4,
    'Chute de Longe': 4,
    'Marcação': 0.5,
    'Bote': 0.5,
    'Carrinho': 0.5,
    'Passe curto': 4,
    'Lançamento': 2,
    'Visão': 4,
    'Força': 2,
    'Fôlego': 4,
    'Impulsão': 2 ,
    'Posicionamento': 4,
    'Controle corporal': 6,
    'Controle bola': 6,
    'Drible': 6
}

pesos_meia_central = {
    'Aceleração': 3,
    'Velocidade': 3,
    'Agilidade': 3,
    'Cabeceio': 1,
    'Finalização': 2,
    'Chute de Longe': 3,
    'Marcação': 3,
    'Bote': 3,
    'Carrinho': 3,
    'Passe curto': 6,
    'Lançamento': 6,
    'Visão': 6,
    'Força': 2,
    'Fôlego': 5,
    'Impulsão': 1,
    'Posicionamento': 5,
    'Controle corporal': 4,
    'Controle bola': 6,
    'Drible': 5
}
pesos_ala = {
    'Aceleração': 6,
    'Velocidade': 6,
    'Agilidade': 3,
    'Cabeceio': 1,
    'Finalização': 2,
    'Chute de Longe': 2,
    'Marcação':4,
    'Bote': 4,
    'Carrinho': 3,
    'Passe curto': 5,
    'Lançamento': 4,
    'Visão': 3,
    'Força': 3,
    'Fôlego': 7,
    'Impulsão': 3,
    'Posicionamento': 4,
    'Controle corporal': 3,
    'Controle bola': 5,
    'Drible': 3
}
pesos_ml = {
    'Aceleração': 6,
    'Velocidade': 6,
    'Agilidade': 4,
    'Cabeceio': 1,
    'Finalização': 2,
    'Chute de Longe': 2,
    'Marcação':2,
    'Bote': 1,
    'Carrinho': 1,
    'Passe curto': 5.5,
    'Lançamento': 5,
    'Visão': 5,
    'Força': 1,
    'Fôlego': 6,
    'Impulsão': 1,
    'Posicionamento': 4,
    'Controle corporal': 3,
    'Controle bola': 6,
    'Drible': 5.5
}
posi_nu = {}
posi_nu.setdefault('LD', pesos_ld.copy())
posi_nu.setdefault('ZAG', pesos_zg.copy())
posi_nu.setdefault('LE', pesos_ld.copy())
posi_nu.setdefault('ALD', pesos_ala.copy())
posi_nu.setdefault('VOL', pesos_vol.copy())
posi_nu.setdefault('ALE', pesos_ala.copy())
posi_nu.setdefault('MD', pesos_ml.copy())
posi_nu.setdefault('MC', pesos_meia_central.copy())
posi_nu.setdefault('ME', pesos_ml.copy())
posi_nu.setdefault('MA', pesos_ma.copy())
posi_nu.setdefault('PD', pesos_ponta.copy())
posi_nu.setdefault('SA', pesos_sa.copy())
posi_nu.setdefault('PE', pesos_ponta.copy())
posi_nu.setdefault('ATA', pesos_ata.copy())

   
joga = modelo['Habilidades'].copy()
#for hab in joga:
#   joga[hab]= numero_aleatorio(80)

def gerador_hab(g, p):
    pesos_t = 70
    pe = 100 / pesos_t * p
    
    total_geral = g * pesos_t
    ponderado = (total_geral * pe) / 100
    atributo_cru = ponderado / 50 * 10
    atributo_real = (atributo_cru + (g * 2)) / 3
    
    return atributo_real

def criar_hab(g, pesos_pos):
    jogado = modelo['Habilidades'].copy()
    for hab, va in jogado.items():
        p = pesos_pos[hab]        
        num_ge = gerador_hab(g, p)
        aleatorio = 0
        if num_ge < 60:
            aleatorio = random.randint(-8, 14)
        elif num_ge < 70:
            aleatorio = random.randint(-10, 10)
        elif num_ge < 80:
            aleatorio = random.randint(-8, 8 )
        elif num_ge < 85:
            aleatorio = random.randint(-7, 7)
        elif num_ge < 90:
            aleatorio = random.randint(-5, 5)
        elif num_ge < 95:
            aleatorio = random.randint(-3, 3)
        elif num_ge <= 100:
            aleatorio = random.randint(-4, 1)
            
        jogado[hab] = int (num_ge + aleatorio)
        
    return jogado



def conta(peso):
    soma = 0
    for it in peso.items():
        chave, valor = it
        
        soma = soma + valor
        
    return soma
 
        
        





    
    

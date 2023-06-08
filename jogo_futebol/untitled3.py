import random

posicoes= ['LD', 'ZAG', 'LE', 'ALD', "VOL", 'ALE', 'MD', 'MC', 'ME', 'MA', 'PD','SA', 'PE', 'ATA']


def ger_pos():
    r1 = random.randint(0, 13)
    return posicoes[r1]


def gerador_alt (pos):
    media = 1.77
    minima = 1.55
    maxima = 2.05
    n1 = random.uniform(minima, maxima)
    n2 = random.uniform(minima, maxima)
    n3 = random.uniform(minima, maxima)
    n4 = random.uniform(minima, maxima)
    n5 = random.uniform(minima, maxima)
    
    if pos == posicoes[0]:
        altura = ((n1 + n2 + n3 + n4) + (minima)) / 5
        
    elif pos == posicoes[1]:
        altura = (n1 + n2 + n3 + n4 + maxima + maxima) / 6
    elif pos == posicoes[2]:
        altura = ((n1 + n2 + n3 + n4) + (minima )) / 5
        
    elif pos == posicoes[3]:
        altura = ((n1 + n2 + n3 + n4) + (minima )) / 5
        
    elif pos == posicoes[4]:
        altura = (n1 + n2 + n3 + n4 + maxima) / 5
        
    elif pos == posicoes[5]:
        altura = ((n1 + n2 + n3 + n4) + (minima)) / 5
        
    elif pos == posicoes[6]:
        altura = ((n1 + n2 + n3 + n4) + (1.70 * 2)) / 6     
        
    elif pos == posicoes[7]:
        altura = (n1 + n2 + 1.7) / 3     
        
    elif pos == posicoes[8]:
        altura = ((n1 + n2 + n3 + n4) + (1.70 * 2)) / 6
              
    elif pos == posicoes[9]:
        altura = (n1 + n2 + 1.7) / 3
                  
    elif pos == posicoes[10]:
        altura = (n1 + n2 + n3) / 3
        
        altura = ((n1 + n2 + n3 + n4) + 1.65) / 5 
    elif pos == posicoes[11]:
        altura = ((n1 + n2 + n3 + n4) + 1.70) / 5
        
    elif pos == posicoes[12]:
        altura = ((n1 + n2 + n3 + n4) + 1.65) / 5
        
    elif pos == posicoes[13]:
        altura = (n1 + n2 + n3 + n4 + n5 + maxima + media + media) / 8
        
    return round(altura, 2)

print(gerador_alt('ATA'))
print(ger_pos())
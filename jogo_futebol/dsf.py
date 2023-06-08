campo = []
comprimento = 105
largura = 68
for i in range(comprimento):
    campo.append([])
    for j in range(largura):
        campo[i].append(0)

print(campo)

def criar_jogador (Pais, g):
    jogador = modelo.copy()
    jogador['nome'] = gerador_aleatorio_nome(Pais)
    jogador['idade'] = random.randint(16, 40)
    
    r1 = random.randint(0, 7)
    
    jogador['posição'] = ger_pos()
       
    jogador['Habilidades'] = criar_hab(g, posi_nu[jogador['posição']])
    
    jogador['altura'] = gerador_alt(jogador['posição'])
    varia_agili = (1.85 - jogador['altura']) * 100
    agili_cru = jogador['Habilidades']['Agilidade']
    
    jogador['Habilidades']['Agilidade'] = int(agili_cru + varia_agili)
    jogador['time'] = times[random.randint(0, 22)]
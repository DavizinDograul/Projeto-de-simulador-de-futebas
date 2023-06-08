import random
from gerador_jogador import *
from untitled1 import *
import numpy as np
from collections import Counter 

"""modelo = {
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
    'Posicionamento': 0, 'Controle corporal': 0}
    
}"""




# posiçõe
posicoes= ['LD', 'ZAG', 'LE', 'ALD', "VOL", 'ALE', 'MD', 'MC', 'ME', 'MA', 'PD','SA', 'PE', 'ATA']
#posicoes= ['LD', 'ZAG', 'LE', 'ALD', 'ALE', 'MD', 'MC', 'ME', 'PE', 'PD']


posicoes_ataque = ['MA', 'PD', 'SA', 'PE', 'ATA']
posicoes_meio = ['VOL', 'MD', 'MC', 'ME', 'MA']
posicoes_defesa = ['LD', 'ZAG', 'LE', 'ALD', 'VOL', 'ALE']


#jogadores = []

paises = list(nomes.keys())



idades_probabilidade = {
    16: 6,
    17: 23,
    18: 32,
    19: 30,
    20: 29,
    21: 35,
    22: 40,
    23: 37,
    24: 40,
    25: 41,
    26: 39,
    27: 39,
    28: 40,
    29: 39,
    30: 29,
    31: 19,
    32: 19,
    33: 17,
    34: 12,
    35: 10,
    36: 8,
    37: 3,
    38: 2
}

def gerador_overal(num_jogadores):
    jogadores = []
    
    # Classe 's' (+90)
    jogadores += random.choices(range(91, 95), k=10)
    
    # Classe 'a' (+85)
    jogadores += random.choices(range(86, 91), k=50)
    print(jogadores)
    
    # Classe 'b' (+80)
    jogadores += random.choices(range(81, 86), k=180)
    
    # Classe 'c' (+75)
    jogadores += random.choices(range(76, 81), k=760)
    
    # Classe 'd' (+70)
    jogadores += random.choices(range(71, 76), k=2440)
    
    # Classe 'e' (+65 a +69)
    jogadores += random.choices(range(65, 71), k=3660)
    
    # Classe 'f' (+60 a +64)
    jogadores += random.choices(range(61, 65), k=4500)
    
    # Classe 'g' (abaixo de +60)
    jogadores += random.choices(range(56, 61), k=2500)
    
    random.shuffle(jogadores)  # Embaralhar a lista
    
    return jogadores[:num_jogadores]



idades = list(idades_probabilidade.keys())
probabilidades = list(idades_probabilidade.values())

#função para gerar idade quase q aleatoriamente ultilizando pesos
def gerar_idade():
    idade = random.choices(idades, weights=probabilidades)[0]
    return idade

#função para gerar posição de forma aleatória
def ger_pos():
    r1 = random.randint(0, 13)
    return posicoes[r1]

#função para gerar altura levando em consideraação a posição
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


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def nome_aleatorio (numero_silabas):
    vogais = ['a', 'e', 'i', 'o', "u", 'ão']
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    palavra = ''
    
    for _ in range(numero_silabas):
        silaba = random.choice(consoantes) + random.choice(vogais)
        palavra += silaba


    p = palavra[0].upper()
    r = palavra[1:]
    

    return p + r

#-------------------------------Classes----------------------------------------  



class país:
    def __init__(self, nome_pais, pais_proximo1, pais_proximo2, pais_proximo3, pais_proximo4):
        self.nome = nome_pais
        self.proximo = pais_proximo1
        self.proximo2 = pais_proximo2
        self.proximo3 = pais_proximo3
        self.proximo4 = pais_proximo4



finlandia = país('finlandia', 'noruega', 'dinamarca', 'holanda', 'inglaterra')
espanha = país('espanha', 'portugal', 'italia', 'brasil', 'inglaterra')
inglaterra = país('inglaterra', 'usa', 'espanha', 'dinamarca', 'italia')
usa = país('usa', 'inglaterra', 'argentina', 'brasil', 'colombia')
argentina = país('argentina', 'brasil', 'colombia', 'usa', 'espanha')
noruega = país('noruega', 'finlandia', 'dinamarca', 'inglaterra', 'holanda')
dinamarca = país('dinamarca', 'noruega', 'finlandia', 'inglaterra', 'noruega')
holanda = país('holanda','noruega', 'dinamarca', 'finlandia', 'espanha')
brasil = país('brasil', 'argentina', 'colombia', 'portugal', 'usa')
portugal = país('portugal', 'espanha', 'inglaterra', 'italia', 'brasil')
italia = país('italia', 'holanda', 'espanha', 'dinamarca', 'noruega')
colombia = país('colombia', 'brasil', 'argentina', 'usa', 'espanha')

paise_g = {
    'finlandia': finlandia,
    'espanha': espanha,
    'inglaterra': inglaterra,
    'usa': usa,
    'argentina': argentina,
    'noruega': noruega,
    'dinamarca': dinamarca,
    'holanda': holanda,
    'brasil': brasil,
    'portugal': portugal,
    'italia': italia,
    'colombia': colombia
    }

def escolha_nacionalidade(p):
    n_de_possibilidade = 0
    
    pais_principal = [p.nome, 15]
    escolha1 = [p.proximo, 20]
    escolha2 = [p.proximo2, 25]
    escolha3 = [p.proximo3, 27]
    escolha4 = [p.proximo4, 29]
    
    n_ale = random.choice(range(1, 30))
    
    if n_ale <= 15:
        return pais_principal[0]
    elif n_ale <= 20:
        return escolha1[0]
    elif n_ale <= 25:
        return escolha2[0]
    elif n_ale <= 27:
        return escolha3[0]
    elif n_ale <= 29:
        return escolha4[0]


    
# definição de classe para criar objetos "Jogadores"
class Ujogador:
    n = 0
    
    def __init__(self, p, g, clube_pertencente, posic = None):
        
        
        pais = p.lower()
        
        
        self.nome = gerador_aleatorio_nome(pais)
        self.idade = gerar_idade()
        self.posicao = ger_pos() if posic == None else posic
        self.altura = gerador_alt(self.posicao)
        self.habilidades = criar_hab(g, posi_nu[self.posicao])
        self.codigo = '{:0>5}'.format(Ujogador.n)
        self.pais = pais
        Ujogador.n += 1
        
        #armagena a soma os valores dos pesos de cada habilidade
        soma_pesos = 0
        #armagena a soma do produto da multiplicação do valor da habilidade pelo seu respectivo peso
        soma_vhabili = 0
        #dicionario q contem a propriedade "habilidades" e os seus valores
        habilidades_j = self.habilidades
        
        
        for hab, peso in posi_nu[self.posicao].items():
            soma_pesos += peso
            soma_vhabili += peso * habilidades_j[hab]
        
        self.classificacao_geral = (soma_vhabili / soma_pesos) + 6
        self.time = clube_pertencente.nome
        
        
            
            
    
        
# definição de classe para criar objetos "Time"        
        
class Time:
    
    pesos_paises = {}
    
    for pa in paises:
        pesos_paises.setdefault(pa, 0)
    
    co= 0
    p = {
        'brasil':1,
        'espanha':1,
        'italia':-1,
        'inglaterra':0,
        'colombia':-5,
        'nigeria':-8,
        'croacia':-3,
        'usa':-10,
        'argentina':1,
        'noruega':0,
        'finlandia':0,
        'holanda':0,
        'dinamarca':0,
        'portugal':0
        }
    
    def __init__(self, nome, formacao, pais_do_time):
        def calculo_o_ataque(area):
            i = 0
            s = 0
            for j in self.escalacao:
                if j.posicao in area:
                    s += j.classificacao_geral
                    i += 1
            return s/i
        
        def calculo_de_atributo (atributo):
            i = 0
            s = 0
            for j in self.escalacao:
                s += j.habilidades[atributo]
                i += 1
            return s/i
        
        
        
        
        self.nome = nome
        
        
        self.pais = pais_do_time
        
        
        
        
        
        
        
        self.jogadores = []    
        self.formacao = ge_escalacao(formacao)
        
        for i in self.formacao:
            for n in range(3):
                a, *_ = gerador_overal(1)
                pa = escolha_nacionalidade(paise_g[pais_do_time])
                print(pa)
                j = Ujogador(pa, numero_aleatorio(int(a) - 7 + Time.p[pa]), self, i)
                self.jogadores.append(j)
                 
        self.escalacao = gerador_de_escalacao(formacao, self.jogadores)
        self.melhor_jogador = (sorted(self.jogadores, key = lambda x: x.classificacao_geral, reverse=True))[0]
        self.ataque = calculo_o_ataque(posicoes_ataque)
        self.defesa = calculo_o_ataque(posicoes_defesa)
        self.meio_campo = calculo_o_ataque(posicoes_defesa)
        self.geral = (self.meio_campo + self.ataque + self.defesa) / 3
        self.codigo = '{:0>5}'.format(Time.co)
        
        Time.co += 1
        
        
class Selecao:
    
    def __init__(self, jogadores, nome, formacao):
        
        def calculo_o_ataque(area):
            i = 0
            s = 0
            for j in self.escalacao:
                if j.posicao in area:
                    s += j.classificacao_geral
                    i += 1
            return s/i
        
        def calculo_de_atributo (atributo):
            i = 0
            s = 0
            for j in self.escalacao:
                s += j.habilidades[atributo]
                i += 1
            return s/i
        
        
        self.jogadores = jogadores
        self.nome = nome
        self.formacao = ge_escalacao(formacao)
        self.escalacao = gerador_de_escalacao(formacao, self.jogadores)
        self.melhor_jogador = (sorted(self.jogadores, key = lambda x: x.classificacao_geral, reverse=True))[0]
        self.ataque = calculo_o_ataque(posicoes_ataque)
        self.defesa = calculo_o_ataque(posicoes_defesa)
        self.meio_campo = calculo_o_ataque(posicoes_defesa)
        self.geral = (self.meio_campo + self.ataque + self.defesa) / 3     
        
        
class liga:
    def __init__(self, pais, numero_times):
        self.times = []
        for i in range(numero_times):
            time = Time(nome_aleatorio(random.randint(2, 5)), random.choice(escalacoes),pais)
            self.times.append(time)
        
        self.pais = pais
        



#------------------------------------------------------------------------------


#-----------------------------Funções------------------------------------------



def escalaca(jogadores, formacao):
    esquema = ge_escalacao(formacao)
    
    for posicao in esquema:
        for jogador in jogadores:
            if jogador.posicao == posicao:
                print(jogador.posicao, posicao)
    


#função para gerar numers aleatórios entre 40 e 100, tem como parametro "media" q serve como uma tendência,
#fazendo com q o número gerado tenha maior probabilidade de ser próximo da "media"    
def numero_aleatorio(media):
    desvio_padrao = 6
    
    while True:
        numero = np.random.normal(media, desvio_padrao)
        if 40 <= numero <= 100:
            return round(numero, 0)

#------------------------------------------------------------------------------    
 

#cria jogadores       
def criar_joaga(n):
    jogadore= []
    for i in range(n):
        
        jo = Ujogador(paises[random.randint(0, 6)], 77)
        jogadore.append(jo)
        
    return jogadore
    
#------------------------------------------------------------------------------   
      

posi_campo = [['LD', 'ZAG','ZAG','ZAG','LE'],
             ['ALD', 'VOL', 'VOL', 'VOL', 'ALE'],
             ['MD', 'MC', 'MC', 'MC', 'ME'],
             ['MAD', 'MA', 'MA', 'MA', 'MAE'],
             ['PD', 'SA', 'SA', 'SA', 'PE'],
             ['ATA', 'ATA', 'ATA']]

escala433= [0, 1, 3, 4,'p', 2, 'p', 1, 3, 'p', 'p', 0, 4, 'p', 1]
escala442 = [0, 1, 3, 4, 'p', 'p', 0, 1, 3, 4, 'p', 'p', 'p', 0, 2 ]
escala5311 = [1, 2, 3, 'p', 0, 4, 'p', 1, 3,'p', 'p', 2, 'p', 1]
escala4213 = [0, 1, 3, 4, 'p', 1, 3, 'p', 'p', 2, 'p', 0, 4, 'p', 1]
escalacoes = [escala433, escala442, escala5311, escala4213]

        
def ge_escalacao(escala):
    con_num = 0
    posicoes_escala = []

    for item in escala:
        if item == 'p':
            con_num = con_num + 1
        else:
            posicoes_escala.append(posi_campo[con_num][item])
    
    return posicoes_escala


#------------------------------------------------------------------------------
def mostrar():
    while True:
        comando = input('Qual vai ser a sua açõa? (procurar, encerrar)')
        if comando == 'procurar' or comando == 'encerrar':
            if comando == 'procurar':
                jjj = vars(jogad)
                print('Caracteristicas disponiveis:')
                for prop, val in jjj.items():
                    print(prop)
                    
                parametro_pesquisa = input('Qual Caracteristica deseja saber?')
                    
                if parametro_pesquisa in jjj:
                    valor = getattr(jogad, parametro_pesquisa)
                    print(valor)
                    
                else:
                    print('Caracteristica não encontrada')
                        
                    
            else:
                print('Encerrando...')
                break
        
        else: 
            print('Ação não reconhecida. Tente novamente.')
            continue
#------------------------------------------------------------------------------    

#------------------------------------------------------------------------------            

#função para encontrar jogadores usando como paramentro uma propriedade (ex: 'posicao') e o
# valor da propriedade (ex: 'MC'), assim, retornando uma lista do jogadores que atendem
# por esse parametros e ordenados pelo atributo 'classificação_geral'        
def encontrar_jogadores_por_propriedade(propriedade, valor_propriedade, jogadores):
    #lista de jogadores q atendem os parametros
    jogadores_encontrados = []
    
    #para cada 'jogador'
    for jogador in jogadores:
    #verifica se atende os parametros definidos        
        if getattr(jogador, propriedade) == valor_propriedade:
            #adciona a lista os jogadores q atendem as listas
            jogadores_encontrados.append(jogador)
    
    #ordena os jogadores na lista pelo atributo 'classificacao_geral' do maior para o menor
    jogadores_ordenados = sorted(jogadores_encontrados, key = lambda x: x.classificacao_geral, reverse = True)
    
    
    return jogadores_ordenados

#------------------------------------------------------------------------------
 
def gerador_de_escalacao(escala, jogadores):                
    tatico = ge_escalacao(escala)
    tatico_d = Counter(tatico)
    e_tatico = []

    for pos, vzs in tatico_d.items():
        for i in range(vzs):
            lp = encontrar_jogadores_por_propriedade('posicao', pos, jogadores)
            # as vezes da errado pq quando a funcao  e chamada por uma classe
            # selecao, pode dar erado, pq pode n ter a quantidade o sufucientes 
            # de jogadores para as suas respectivas funcoes
            e_tatico.append(lp[i])
            
    return e_tatico

#-----------------------------------------------------------------------------
'''times=[]

for n in range(400):
    time= Time(nome_aleatorio(random.randint(2, 5)), random.choice(escalacoes))
    times.append(time)

ordn = []
ordn = sorted(times, key= lambda x: x.geral, reverse = True)

todos_jogadores = []
for t in times:
    for j in t.jogadores:
        todos_jogadores.append(j)
        
jopo = sorted(todos_jogadores, key= lambda j: j.classificacao_geral, reverse= True)


'''
#------------------------------------------------------------------------------
            
def confronto(time1, time2):
    def calcular_resultado(time):
        # Calculando o desempenho geral de cada time
        ataque = time.ataque
        defesa = time.defesa
        meio_campo = time.meio_campo
        geral = time.geral

        # Gerando um fator aleatório para simular a variabilidade do jogo
        variabilidade = random.uniform(0.9, 1.1)

        # Calculando o desempenho final do time
        desempenho = (ataque + defesa + meio_campo + geral) * variabilidade

        return desempenho

    # Simulando o desempenho de cada time
    desempenho_time1 = calcular_resultado(time1)
    desempenho_time2 = calcular_resultado(time2)

    # Determinando o vencedor com base no desempenho
    if desempenho_time1 > desempenho_time2:
        return time1.nome
    elif desempenho_time2 > desempenho_time1:
        return time2.nome
    else:
        return None  # Empate

#------------------------------------------------------------------------------

def campeonato (times):
    pontua = {}
    
    for i in times:
        pontua.setdefault(i, 0)
    
    for c in times:
        p = 0
        for v in times:
            if c.nome != v.nome:
                con = confronto(c, v)
                if con == c.nome:
                    pontua[c] += 3
                elif con == v.nome:
                    pontua[v] += 3
                else:
                    pontua[c] += 1 
                    pontua[v] += 1
                    
    lista_times = []
    
    for nome, p in pontua.items():
        lista_times.append([nome, p])
    
    
        
                    
    orde = sorted(lista_times, key= lambda x : x[1], reverse= True)
                    
    
    retorno = ''
    for n, con in enumerate(orde):
        texto = f'posição:  {n+1} | Time:  {con[0].nome} | Pontuação:  {con[1]} | Media dos jogadores: {con[0].geral} \n'
        retorno += texto
        
        
    return retorno






'''selecoes_elenco = {}

for i in paises:
    seleca = []
    for j in jopo:
        if i == j.pais:
            seleca.append(j)
    selecoes_elenco.setdefault(i, seleca)


selecao = {}            

for k in selecoes_elenco.keys():
    seleca = Selecao(selecoes_elenco[k], k, random.choice(escalacoes))
    selecao.setdefault(k, seleca)
    
'''

ligas = []

for i, fd in paise_g.items():
    ligaa = liga(i, 20)
    ligas.append(ligaa)

for i in ligas:
    print(i.pais)
    print(campeonato(i.times))



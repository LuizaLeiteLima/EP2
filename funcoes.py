from random import*
from math import*

def cria_pecas ():

    pecas = []

 
    for numero in range(0,7):
        for numero2 in range(0,7):
            if [numero,numero2] not in pecas and [numero2,numero] not in pecas:
                pecas.append([numero,numero2])

    shuffle(pecas)
    return pecas

def inicia_jogo (jogadores,tabuleiro):

    resto = {'jogadores':{},
             'monte':'',
             'mesa': []
             }
    
    pecas = 7

    for jogador in range(0, jogadores):
        if jogador not in resto['jogadores']:
            resto['jogadores'][jogador] = []


    for jogador in resto['jogadores']:
        for lista in tabuleiro[:]:
            if pecas > len(resto['jogadores'][jogador]):
                resto['jogadores'][jogador].append(lista)
                tabuleiro.remove(lista)
                
    resto['monte'] = tabuleiro
    return resto



def verifica_ganhador(jogadores):
    for jogador, pecas in jogadores.items():
        if len(pecas) == 0:
            return jogador
    #teste  
    return -1

def conta_pontos(lista_pecas):
    soma = 0
    for lista_pontos in lista_pecas:
        for i in range(len(lista_pontos)):
            soma+=lista_pontos[i]
    return soma

def posicoes_possiveis(estado_mesa,lista_pecas):
    lista_ind = [] 
    for i in range(len(lista_pecas)):
        if len(estado_mesa)==0:
            lista_ind.append(i)
        else:
            esq = estado_mesa[0][0]
            dir = estado_mesa[-1][1]
            if lista_pecas[i][0]==dir or lista_pecas[i][1]==dir or lista_pecas[i][0]==esq or lista_pecas[i][1]==esq:
                lista_ind.append(i)
    return lista_ind

def adiciona_na_mesa(peca_col,lista_pecas):
    saida = []
    if len(lista_pecas)==0:
        return saida.append(peca_col)
    
    esq = lista_pecas[0][0]
    dir = lista_pecas[-1][1]
    esq_peca = peca_col[0]
    dir_peca = peca_col[1]


    if esq_peca == lista_pecas[0][0]:
        peca_col = peca_col[::-1]
        saida = [peca_col, *lista_pecas]
    elif esq_peca == lista_pecas[-1][1]:
        saida = lista_pecas
        saida = saida.append(peca_col)
    elif dir_peca == lista_pecas[0][0]:
        saida = [peca_col, *lista_pecas]
    elif dir_peca == lista_pecas[-1][1]:
        peca_col = peca_col[::-1]
        saida = lista_pecas
        saida = saida.append(peca_col)
    return saida


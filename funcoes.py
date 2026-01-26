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
        if pecas == 0:
            return jogador
        
    return -1




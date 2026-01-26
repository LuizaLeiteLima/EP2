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

    for lista in tabuleiro[:]:
        if pecas > len(resto['jogadores'][jogador]):
            resto['jogadores'][jogador].append(lista)
            tabuleiro.remove(lista)
                
    resto['monte'] = tabuleiro
    return resto



jogadores = 2

tabuleiro = [
    [1,3],[0,1],[4,6],[0,3],[0,4],[6,6],[0,6],
    [1,1],[1,2],[0,0],[1,4],[1,5],[1,6],[2,2],
    [3,6],[2,4],[2,5],[2,6],[3,3],[3,4],[2,3],
    [3,5],[4,4],[4,5],[0,2],[5,5],[5,6],[0,5]
]


resultado = inicia_jogo(jogadores, tabuleiro)

print(resultado)




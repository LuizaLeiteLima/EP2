from random import*
from math import*

def cria_pecas ():

    pecas = []

 
    for numero in range(0,7):
        for numero2 in range(0,7):
            pecas.append([numero,numero2])

    random.shuffle(pecas)
    return pecas




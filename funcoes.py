def cria_pecas ():

    pecas = []

    while len(pecas) < 28:
        adiciona = []
        for numero in range(0,6):
            if len(adiciona) < 2:
                adiciona.append(numero)
            if len(adiciona) == 2:
                if adiciona not in pecas:
                    pecas.append(adiciona)

    return pecas




from funcoes import *


jogar = "sim"
while jogar == "sim":
    
    
    pecas_do_tabuleiro = cria_pecas()
    quantidade_jogadores = int(input("Quantos jogadores vão joga (2-4)? "))
    

    estado_do_jogo = inicia_jogo(quantidade_jogadores, pecas_do_tabuleiro)
    
    lista_jogadores = estado_do_jogo['jogadores']
    monte = estado_do_jogo['monte']
    mesa = estado_do_jogo['mesa']
    
    vencedor = -1
    quem_joga= 0
    trava_jogo = 0 
    
   
    while vencedor == -1 and trava_jogo < quantidade_jogadores:
            
            print("\nvez do jogador", quem_joga, "")
            print("Mesa atual:", mesa)
            
            minhas_pecas = lista_jogadores[quem_joga]
            
            opcoes = posicoes_possiveis(mesa, minhas_pecas)
            
            while len(opcoes) == 0 and len(monte) > 0:
                print("nao tem peca, pegue uma do monte")
                peca_nova = monte[0]
                minhas_pecas.append(peca_nova)
                monte.remove(peca_nova)
                opcoes = posicoes_possiveis(mesa, minhas_pecas)

    if len(opcoes) > 0:
            trava_jogo = 0
            
            if quem_joga == 0:
                print("suas pecas sao:", minhas_pecas)
                print("indices das pecas que voce pode jogar:", opcoes)
                
                escolha = int(input("qual o indice da peca que voce quer jogar? "))
                
                while escolha not in opcoes:
                    print("essa peca nao serve na mesa")
                    escolha = int(input("escolha um indice valido: "))
                
                peca_escolhida = minhas_pecas[escolha]
                minhas_pecas.remove(peca_escolhida)
                mesa = adiciona_na_mesa(peca_escolhida, mesa)
            else:
                indice_pc = opcoes[0]
                peca_pc = minhas_pecas[indice_pc]
                minhas_pecas.remove(peca_pc)
                mesa = adiciona_na_mesa(peca_pc, mesa)
                print("o computador jogou a peca:", peca_pc)
                
    else:
        print("o jogador", quem_joga, "nao tem o que jogar e passou a vez")
        trava_jogo = trava_jogo + 1
        
    vencedor = verifica_ganhador(lista_jogadores)

    quem_joga = quem_joga + 1
    if quem_joga >= quantidade_jogadores:
        quem_joga = 0

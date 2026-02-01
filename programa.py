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
            
            print("\n--- VEZ DO JOGADOR", quem_joga, "---")
            print("Mesa atual:", mesa)
            
            minhas_pecas = lista_jogadores[quem_joga]
            
            opcoes = posicoes_possiveis(mesa, minhas_pecas)
            
            while len(opcoes) == 0 and len(monte) > 0:
                print("Voce nao tem peca! Pegando uma no monte...")
                peca_nova = monte[0]
                minhas_pecas.append(peca_nova)
                monte.remove(peca_nova)
                opcoes = posicoes_possiveis(mesa, minhas_pecas)

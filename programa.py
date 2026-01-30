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
    
   
   
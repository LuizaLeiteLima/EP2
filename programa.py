from funcoes import *


jogar = "sim"
while jogar == "sim":
    
    
    pecas_do_tabuleiro = cria_pecas()
    quantidade_jogadores = int(input("Quantos jogadores vão joga (2-4)? "))
    

    estado = inicia_jogo(quantidade_jogadores, pecas_do_tabuleiro)
    
    lista_jogadores = estado['jogadores']
    monte = estado['monte']
    mesa = estado['mesa']
    
    vencedor = -1
    quem_joga= 0
    trava_jogo = 0 
    
   
   
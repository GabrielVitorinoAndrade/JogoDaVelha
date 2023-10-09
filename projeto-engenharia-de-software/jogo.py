import subprocess
import pygame
import sys
import json
from EstruturaJogo import EstruturaJogo
from Desenhar import Colors
from Desenhar import Desenhar
from IA import IA

pygame.init()

Cor = Colors()
Desenha = Desenhar()
Jogo = EstruturaJogo()
Jogo.textosLingua()
Inteligence = IA()

quemComecouJogando = 1

# Setup do tamanho da tela do Jogo
largura = 1200
altura = 600

window = pygame.display.set_mode((largura, altura))
window.fill(Cor.preto)

pygame.display.set_caption("Jogo da Velha")

fonteParaOutrasCoisas = pygame.font.Font(None, 32)
fontePlacar = pygame.font.Font(None, 50)

texto = fonteParaOutrasCoisas.render(Jogo.textos[0], True, Cor.branco)
texto2 = fontePlacar.render(Jogo.textos[1], True, Cor.branco)
texto3 = fontePlacar.render("0 x 0", True, Cor.branco)

texto_rect = texto.get_rect()
texto2_rect = texto2.get_rect()
texto3_rect = texto3.get_rect()

texto_rect.center = (largura // 2, altura // 6)
texto2_rect.center = (1050, 50)
texto3_rect.center = (1050, 100)

Desenha.pintarTabuleiro(window)

window.blit(texto, texto_rect)
window.blit(texto2, texto2_rect)
window.blit(texto3, texto3_rect)

with open("dados.json", "r") as arquivo_json:
    # Use json.load() para carregar o conteúdo em uma estrutura de dados Python
    dados = json.load(arquivo_json)

pygame.draw.line(window, Cor.vermelho, (955, 75), (1005, 125), 10)
pygame.draw.line(window, Cor.vermelho, (1005, 75), (955, 125), 10)

pygame.draw.circle(window, Cor.azul, (1125, 100), 25)
pygame.draw.circle(window, Cor.preto, (1125, 100), 15)


####################################################################################################################################


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            subprocess.call(["python", "telaInicial.py"])
            sys.exit() 
    
    Jogo.pintarSimboloDaVez(window)  

    if(dados["gameMode"] == "PVP"): Jogo.verificaSeSelecionouBloco(window)
    elif(dados["gameMode"] == "IA"):
        if Jogo.simboloQueVaiJogar == 1:
            Jogo.verificaSeSelecionouBloco(window)
        else:
            if(Inteligence.getComputerMove(Jogo.matrizJogo, 2) == -1): pass
            else: Jogo.colocarJogadaNoTabuleiro(Inteligence.getComputerMove(Jogo.matrizJogo, 2) , 2, window)

    Jogo.verificarVitoria(window)

    # Declarando mouse
    mouse = pygame.mouse.get_pos()      # POSIÇÃO DO MOUSE
    # Declarando click do mouse
    click = pygame.mouse.get_pressed()  # CLICKES DO MOUSE 

    if ((0 <= mouse[0] <= 600 and click[2] == 1 and Jogo.fim == 1) or
        ((Jogo.verificarSeHaEspacosVazios()) and click[2] == 1)
    ):
        Desenha.apagarFiguras(window)
        Desenha.pintarTabuleiro(window)
        Jogo.limparMatriz()
        quemComecouJogando = Jogo.simboloQueVaiJogar
        Jogo.fim = 0

    pygame.display.update()
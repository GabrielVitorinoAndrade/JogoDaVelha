import subprocess
from EstruturaJogo import EstruturaJogo
import pygame
import sys

pygame.init()

Jogo = EstruturaJogo()
Jogo.textosLingua()

# Cores do Jogo
preto = (32, 33, 36)
branco = (255, 255, 255)
verde = (58, 171, 87)
vermelho = (234,67,53)
azul = (26,115,232) 

# Setup da tela do Jogo
largura = 1200
altura = 600

window = pygame.display.set_mode((largura, altura))
window.fill(preto)

pygame.display.set_caption("Jogo da Velha")

fonteParaOutrasCoisas = pygame.font.Font(None, 32)
fontePlacar = pygame.font.Font(None, 50)

texto = fonteParaOutrasCoisas.render(Jogo.textos[0], True, branco)
texto2 = fontePlacar.render(Jogo.textos[1], True, branco)
texto3 = fontePlacar.render("0 x 0", True, branco)

texto_rect = texto.get_rect()
texto2_rect = texto2.get_rect()
texto3_rect = texto3.get_rect()

texto_rect.center = (largura // 2, altura // 6)
texto2_rect.center = (1050, 50)
texto3_rect.center = (1050, 100)

# Grade do tabuleiro
pygame.draw.line(window, branco, (205, 50), (205, 521), 10)
pygame.draw.line(window, branco, (365, 50), (365, 521), 10)
pygame.draw.line(window, branco, (50, 205), (521, 205), 10)
pygame.draw.line(window, branco, (50, 365), (521, 365), 10)

window.blit(texto, texto_rect)
window.blit(texto2, texto2_rect)
window.blit(texto3, texto3_rect)





pygame.draw.line(window, vermelho, (955, 75), (1005, 125), 10)
pygame.draw.line(window, vermelho, (1005, 75), (955, 125), 10)

pygame.draw.circle(window, azul, (1125, 100), 25)
pygame.draw.circle(window, preto, (1125, 100), 15)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            subprocess.call(["python", "telaInicial.py"])
            sys.exit()
            
    
    Jogo.pintarSimboloDaVez(window)


    # Declarando mouse
    mouse = pygame.mouse.get_pos()# POSICAO DO MOUSE

    # Declarando click do mouse
    click = pygame.mouse.get_pressed()# CLICKES DO MOUSE
    

    # Blocos de Seleção - Linha 1 - Coluna 1
    if 50 <= mouse[0] <= 200 and 50 <= mouse[1] <= 200:
        if click[0] == 1 and Jogo.matrizJogo[0][0] == 0:
            Jogo.colocarJogadaNoTabuleiro(1, Jogo.simboloQueVaiJogar, window)
            

    # Blocos de Seleção - Linha 1 - Coluna 2
    if 211 <= mouse[0] <= 360 and 50 <= mouse[1] <= 200:
        if click[0] == 1 and Jogo.matrizJogo[0][1] == 0:
            Jogo.colocarJogadaNoTabuleiro(2, Jogo.simboloQueVaiJogar, window)
            

    # Blocos de Seleção - Linha 1 - Coluna 3
    if 371 <= mouse[0] <= 520 and 50 <= mouse[1] <= 200:
        if click[0] == 1 and Jogo.matrizJogo[0][2] == 0:
            Jogo.colocarJogadaNoTabuleiro(3, Jogo.simboloQueVaiJogar, window)
            

    # Blocos de Seleção - Linha 2 - Coluna 1
    if 50 <= mouse[0] <= 200 and 211 <= mouse[1] <= 361:
        if click[0] == 1 and Jogo.matrizJogo[1][0] == 0:
            Jogo.colocarJogadaNoTabuleiro(4, Jogo.simboloQueVaiJogar, window)
            

    # Blocos de Seleção - Linha 2 - Coluna 2
    if 211 <= mouse[0] <= 360 and 211 <= mouse[1] <= 361:
        if click[0] == 1 and Jogo.matrizJogo[1][1] == 0:
            Jogo.colocarJogadaNoTabuleiro(5, Jogo.simboloQueVaiJogar, window)
            

    # Blocos de Seleção - Linha 2 - Coluna 3
    if 371 <= mouse[0] <= 520 and 211 <= mouse[1] <= 361:
        if click[0] == 1 and Jogo.matrizJogo[1][2] == 0:
            Jogo.colocarJogadaNoTabuleiro(6, Jogo.simboloQueVaiJogar, window)
            

    # Blocos de Seleção - Linha 3 - Coluna 1
    if 50 <= mouse[0] <= 200 and 371 <= mouse[1] <= 521:
        if click[0] == 1 and Jogo.matrizJogo[2][0] == 0:
            Jogo.colocarJogadaNoTabuleiro(7, Jogo.simboloQueVaiJogar, window)
            

    # Blocos de Seleção - Linha 3 - Coluna 2
    if 211 <= mouse[0] <= 360 and 371 <= mouse[1] <= 521:
        if click[0] == 1 and Jogo.matrizJogo[2][1] == 0:
            Jogo.colocarJogadaNoTabuleiro(8, Jogo.simboloQueVaiJogar, window)
            

    # Blocos de Seleção - Linha 3 - Coluna 3
    if 371 <= mouse[0] <= 520 and 371 <= mouse[1] <= 521:
        if click[0] == 1 and Jogo.matrizJogo[2][2] == 0:
            Jogo.colocarJogadaNoTabuleiro(9, Jogo.simboloQueVaiJogar, window)
            

    # Traço final
    # Linha 1
    if (
        Jogo.matrizJogo[0][0] == 1
        and Jogo.matrizJogo[0][1] == 1
        and Jogo.matrizJogo[0][2] == 1
        and Jogo.fim == 0
        or Jogo.matrizJogo[0][0] == 2
        and Jogo.matrizJogo[0][1] == 2
        and Jogo.matrizJogo[0][2] == 2
        and Jogo.fim == 0
    ):
        pygame.draw.line(window, verde, (100, 125), (470, 125), 10)
        Jogo.fim = 1
        Jogo.matrizJogo[0][0] = 3
        Jogo.matrizJogo[0][1] = 3
        Jogo.matrizJogo[0][2] = 3
        Jogo.matrizJogo[1][0] = 3
        Jogo.matrizJogo[1][1] = 3
        Jogo.matrizJogo[1][2] = 3
        Jogo.matrizJogo[2][0] = 3
        Jogo.matrizJogo[2][1] = 3
        Jogo.matrizJogo[2][2] = 3
    # Linha 2
    elif (
        Jogo.matrizJogo[1][0] == 1
        and Jogo.matrizJogo[1][1] == 1
        and Jogo.matrizJogo[1][2] == 1
        and Jogo.fim == 0
        or Jogo.matrizJogo[1][0] == 2
        and Jogo.matrizJogo[1][1] == 2
        and Jogo.matrizJogo[1][2] == 2
        and Jogo.fim == 0
    ):
        pygame.draw.line(window, verde, (100, 286), (470, 286), 10)
        Jogo.fim = 1
        Jogo.matrizJogo[0][0] = 3
        Jogo.matrizJogo[0][1] = 3
        Jogo.matrizJogo[0][2] = 3
        Jogo.matrizJogo[1][0] = 3
        Jogo.matrizJogo[1][1] = 3
        Jogo.matrizJogo[1][2] = 3
        Jogo.matrizJogo[2][0] = 3
        Jogo.matrizJogo[2][1] = 3
        Jogo.matrizJogo[2][2] = 3
    # Linha 3
    elif (
        Jogo.matrizJogo[2][0] == 1
        and Jogo.matrizJogo[2][1] == 1
        and Jogo.matrizJogo[2][2] == 1
        and Jogo.fim == 0
        or Jogo.matrizJogo[2][0] == 2
        and Jogo.matrizJogo[2][1] == 2
        and Jogo.matrizJogo[2][2] == 2
        and Jogo.fim == 0
    ):
        pygame.draw.line(window, verde, (100, 447), (470, 447), 10)
        Jogo.fim = 1
        Jogo.matrizJogo[0][0] = 3
        Jogo.matrizJogo[0][1] = 3
        Jogo.matrizJogo[0][2] = 3
        Jogo.matrizJogo[1][0] = 3
        Jogo.matrizJogo[1][1] = 3
        Jogo.matrizJogo[1][2] = 3
        Jogo.matrizJogo[2][0] = 3
        Jogo.matrizJogo[2][1] = 3
        Jogo.matrizJogo[2][2] = 3
    # Coluna 1
    elif (
        Jogo.matrizJogo[0][0] == 1
        and Jogo.matrizJogo[1][0] == 1
        and Jogo.matrizJogo[2][0] == 1
        and Jogo.fim == 0
        or Jogo.matrizJogo[0][0] == 2
        and Jogo.matrizJogo[1][0] == 2
        and Jogo.matrizJogo[2][0] == 2
        and Jogo.fim == 0
    ):
        pygame.draw.line(window, verde, (125, 100), (125, 472), 10)
        Jogo.fim = 1
        Jogo.matrizJogo[0][0] = 3
        Jogo.matrizJogo[0][1] = 3
        Jogo.matrizJogo[0][2] = 3
        Jogo.matrizJogo[1][0] = 3
        Jogo.matrizJogo[1][1] = 3
        Jogo.matrizJogo[1][2] = 3
        Jogo.matrizJogo[2][0] = 3
        Jogo.matrizJogo[2][1] = 3
        Jogo.matrizJogo[2][2] = 3
    # Coluna 2
    elif (
        Jogo.matrizJogo[0][1] == 1
        and Jogo.matrizJogo[1][1] == 1
        and Jogo.matrizJogo[2][1] == 1
        and Jogo.fim == 0
        or Jogo.matrizJogo[0][1] == 2
        and Jogo.matrizJogo[1][1] == 2
        and Jogo.matrizJogo[2][1] == 2
        and Jogo.fim == 0
    ):
        pygame.draw.line(window, verde, (286, 100), (286, 472), 10)
        Jogo.fim = 1
        Jogo.matrizJogo[0][0] = 3
        Jogo.matrizJogo[0][1] = 3
        Jogo.matrizJogo[0][2] = 3
        Jogo.matrizJogo[1][0] = 3
        Jogo.matrizJogo[1][1] = 3
        Jogo.matrizJogo[1][2] = 3
        Jogo.matrizJogo[2][0] = 3
        Jogo.matrizJogo[2][1] = 3
        Jogo.matrizJogo[2][2] = 3
    # Coluna 3
    elif (
        Jogo.matrizJogo[0][2] == 1
        and Jogo.matrizJogo[1][2] == 1
        and Jogo.matrizJogo[2][2] == 1
        and Jogo.fim == 0
        or Jogo.matrizJogo[0][2] == 2
        and Jogo.matrizJogo[1][2] == 2
        and Jogo.matrizJogo[2][2] == 2
        and Jogo.fim == 0
    ):
        pygame.draw.line(window, verde, (446, 100), (446, 472), 10)
        Jogo.fim = 1
        Jogo.matrizJogo[0][0] = 3
        Jogo.matrizJogo[0][1] = 3
        Jogo.matrizJogo[0][2] = 3
        Jogo.matrizJogo[1][0] = 3
        Jogo.matrizJogo[1][1] = 3
        Jogo.matrizJogo[1][2] = 3
        Jogo.matrizJogo[2][0] = 3
        Jogo.matrizJogo[2][1] = 3
        Jogo.matrizJogo[2][2] = 3
    # Diagonal 1
    elif (
        Jogo.matrizJogo[0][0] == 1
        and Jogo.matrizJogo[1][1] == 1
        and Jogo.matrizJogo[2][2] == 1
        and Jogo.fim == 0
        or Jogo.matrizJogo[0][2] == 2
        and Jogo.matrizJogo[1][1] == 2
        and Jogo.matrizJogo[2][2] == 2
        and Jogo.fim == 0
    ):
        pygame.draw.line(window, verde, (100, 100), (471, 472), 10)
        Jogo.fim = 1
        Jogo.matrizJogo[0][0] = 3
        Jogo.matrizJogo[0][1] = 3
        Jogo.matrizJogo[0][2] = 3
        Jogo.matrizJogo[1][0] = 3
        Jogo.matrizJogo[1][1] = 3
        Jogo.matrizJogo[1][2] = 3
        Jogo.matrizJogo[2][0] = 3
        Jogo.matrizJogo[2][1] = 3
        Jogo.matrizJogo[2][2] = 3
    # Diagonal 2
    elif (
        Jogo.matrizJogo[2][0] == 1
        and Jogo.matrizJogo[1][1] == 1
        and Jogo.matrizJogo[0][2] == 1
        and Jogo.fim == 0
        or Jogo.matrizJogo[2][0] == 2
        and Jogo.matrizJogo[1][1] == 2
        and Jogo.matrizJogo[0][2] == 2
        and Jogo.fim == 0
    ):
        pygame.draw.line(window, verde, (100, 472), (471, 100), 10)
        Jogo.fim = 1
        Jogo.matrizJogo[0][0] = 3
        Jogo.matrizJogo[0][1] = 3
        Jogo.matrizJogo[0][2] = 3
        Jogo.matrizJogo[1][0] = 3
        Jogo.matrizJogo[1][1] = 3
        Jogo.matrizJogo[1][2] = 3
        Jogo.matrizJogo[2][0] = 3
        Jogo.matrizJogo[2][1] = 3
        Jogo.matrizJogo[2][2] = 3

    if 0 <= mouse[0] <= 600 and click[2] == 1 and Jogo.fim == 1:
        # Blocos de Seleção - Linha 1 - Coluna 1
        pygame.draw.rect(window, preto, (50, 50, 150, 150))
        # Blocos de Seleção - Linha 1 - Coluna 2
        pygame.draw.rect(window, preto, (211, 50, 150, 150))
        # Blocos de Seleção - Linha 1 - Coluna 3
        pygame.draw.rect(window, preto, (371, 50, 150, 150))
        # Blocos de Seleção - Linha 2 - Coluna 1
        pygame.draw.rect(window, preto, (50, 211, 150, 150))
        # Blocos de Seleção - Linha 2 - Coluna 2
        pygame.draw.rect(window, preto, (211, 211, 150, 150))
        # Blocos de Seleção - Linha 2 - Coluna 3
        pygame.draw.rect(window, preto, (371, 211, 150, 150))
        # Blocos de Seleção - Linha 3 - Coluna 1
        pygame.draw.rect(window, preto, (50, 371, 150, 150))
        # Blocos de Seleção - Linha 3 - Coluna 2
        pygame.draw.rect(window, preto, (211, 371, 150, 150))
        # Blocos de Seleção - Linha 3 - Coluna 3
        pygame.draw.rect(window, preto, (371, 371, 150, 150))
        # Grade do tabuleiro
        pygame.draw.line(window, branco, (205, 50), (205, 521), 10)
        pygame.draw.line(window, branco, (365, 50), (365, 521), 10)
        pygame.draw.line(window, branco, (50, 205), (521, 205), 10)
        pygame.draw.line(window, branco, (50, 365), (521, 365), 10)
        Jogo.matrizJogo[0][0] = 0
        Jogo.matrizJogo[0][1] = 0
        Jogo.matrizJogo[0][2] = 0
        Jogo.matrizJogo[1][0] = 0
        Jogo.matrizJogo[1][1] = 0
        Jogo.matrizJogo[1][2] = 0
        Jogo.matrizJogo[2][0] = 0
        Jogo.matrizJogo[2][1] = 0
        Jogo.matrizJogo[2][2] = 0
        Jogo.simboloQueVaiJogar = 1
        Jogo.fim = 0

    elif (Jogo.verificarVitoria(window) == "EMPATE") and click[2] == 1:
        # Blocos de Seleção - Linha 1 - Coluna 1
        pygame.draw.rect(window, preto, (50, 50, 150, 150))
        # Blocos de Seleção - Linha 1 - Coluna 2
        pygame.draw.rect(window, preto, (211, 50, 150, 150))
        # Blocos de Seleção - Linha 1 - Coluna 3
        pygame.draw.rect(window, preto, (371, 50, 150, 150))
        # Blocos de Seleção - Linha 2 - Coluna 1
        pygame.draw.rect(window, preto, (50, 211, 150, 150))
        # Blocos de Seleção - Linha 2 - Coluna 2
        pygame.draw.rect(window, preto, (211, 211, 150, 150))
        # Blocos de Seleção - Linha 2 - Coluna 3
        pygame.draw.rect(window, preto, (371, 211, 150, 150))
        # Blocos de Seleção - Linha 3 - Coluna 1
        pygame.draw.rect(window, preto, (50, 371, 150, 150))
        # Blocos de Seleção - Linha 3 - Coluna 2
        pygame.draw.rect(window, preto, (211, 371, 150, 150))
        # Blocos de Seleção - Linha 3 - Coluna 3
        pygame.draw.rect(window, preto, (371, 371, 150, 150))
        # Grade do tabuleiro
        pygame.draw.line(window, branco, (205, 50), (205, 521), 10)
        pygame.draw.line(window, branco, (365, 50), (365, 521), 10)
        pygame.draw.line(window, branco, (50, 205), (521, 205), 10)
        pygame.draw.line(window, branco, (50, 365), (521, 365), 10)
        Jogo.matrizJogo[0][0] = 0
        Jogo.matrizJogo[0][1] = 0
        Jogo.matrizJogo[0][2] = 0
        Jogo.matrizJogo[1][0] = 0
        Jogo.matrizJogo[1][1] = 0
        Jogo.matrizJogo[1][2] = 0
        Jogo.matrizJogo[2][0] = 0
        Jogo.matrizJogo[2][1] = 0
        Jogo.matrizJogo[2][2] = 0
        Jogo.simboloQueVaiJogar = 1
        Jogo.fim = 0

    pygame.display.update()

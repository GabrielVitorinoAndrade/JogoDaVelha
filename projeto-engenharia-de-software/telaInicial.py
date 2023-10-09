import pygame
import sys
import subprocess
import json
import os
from Desenhar import Colors

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da janela
largura = pygame.display.Info().current_w
altura = pygame.display.Info().current_h - 60
janela = pygame.display.set_mode((largura, altura))

# Definir o nome que ficará em cima da janela
pygame.display.set_caption("Jogo da Velha")

# Definir as cores
Cor = Colors()
corBotaoPVP, corBotaoBotVP, corLingua = Cor.azul

# Criar um objeto de fonte
fontTitulo = pygame.font.Font(None, 72)  # Você pode escolher uma fonte e um tamanho aqui
fonteParaOutrasCoisas = pygame.font.Font(None, 32)  # Você pode escolher uma fonte e um tamanho aqui

# Definir o estado e modo de jogo padrão
estado = "menu-pt"
modo = "PVP"

botaoJogadorJogador_rect = pygame.Rect( (largura - 300) // 2 , (altura - 100) // 2, 300, 100)
botaoJogadorComputador_rect = pygame.Rect( (largura - 300) // 2 , (altura + 150) // 2, 300, 100)
botaoLingua_rect = pygame.Rect(largura - 200, 0, 200, 36)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            if botaoJogadorJogador_rect.collidepoint(event.pos): corBotaoPVP = Cor.vermelho
            else: corBotaoPVP = Cor.azul

            if botaoLingua_rect.collidepoint(event.pos): corLingua = Cor.vermelho
            else: corLingua = Cor.azul

            if botaoJogadorComputador_rect.collidepoint(event.pos): corBotaoBotVP = Cor.vermelho
            else: corBotaoBotVP = Cor.azul

        elif event.type == pygame.MOUSEBUTTONDOWN and estado != "jogo":
            if (botaoJogadorJogador_rect.collidepoint(event.pos) or botaoJogadorComputador_rect.collidepoint(event.pos)):
                nome_arquivo = "dados.json"
                caminho_pasta = ""
                caminho_completo = os.path.join(caminho_pasta, nome_arquivo)

                estado = "jogo"
                if(botaoJogadorJogador_rect.collidepoint(event.pos)): modo = "PVP"
                elif(botaoJogadorComputador_rect.collidepoint(event.pos)): modo = "IA"

                dados = {
                    "lingua": estado,
                    "gameMode": modo,
                }

                with open(caminho_completo, "w") as arquivo_json:
                    json.dump(dados, arquivo_json)

                pygame.quit()
                subprocess.call(["python", "jogo.py"])
                sys.exit()

            if botaoLingua_rect.collidepoint(event.pos):
                estado = ("menu-pt" if estado == "menu-en" else "menu-en")

    # Lógica de renderização de acordo com o estado atual
    if estado == "menu-pt":
        texto = fontTitulo.render("Seja muito bem-vindo ao Jogo da Velha!", True, Cor.texto)
        texto1 = fonteParaOutrasCoisas.render("Mudar lingua", True, Cor.branco)
        texto2 = fonteParaOutrasCoisas.render("Jogador x Jogador ", True, Cor.branco)
        texto3 = fonteParaOutrasCoisas.render("Jogador x Computador", True, Cor.branco)
    elif estado == "menu-en":
        texto = fontTitulo.render("Welcome to Tic Tac Toe!", True, Cor.texto)
        texto1 = fonteParaOutrasCoisas.render("Change Language", True, Cor.branco)
        texto2 = fonteParaOutrasCoisas.render("Player vs Player", True, Cor.branco)
        texto3 = fonteParaOutrasCoisas.render("Player vs Computer", True, Cor.branco)

    if estado[:4] == "menu":        
        janela.fill(Cor.preto)

        pygame.draw.rect(janela, corBotaoPVP, botaoJogadorJogador_rect)
        pygame.draw.rect(janela, corBotaoBotVP, botaoJogadorComputador_rect)
        pygame.draw.rect(janela, corLingua, botaoLingua_rect)

        texto_rect = texto.get_rect()
        texto_rect1 = texto1.get_rect()
        texto_rect2 = texto2.get_rect()
        texto_rect3 = texto3.get_rect()

        texto_rect.center = (largura // 2, altura // 6)
        texto_rect1.center = (largura - 100, 20)
        texto_rect2.center = ((largura - 200) // 2 + 100.5 , ((altura - 100) + (100 - 32)) // 2 + 10)
        texto_rect3.center = ((largura - 200) // 2 + 100.5 , ((altura + 150) + (100 - 32)) // 2 + 10)
    
        janela.blit(texto, texto_rect)
        janela.blit(texto1, texto_rect1)
        janela.blit(texto2, texto_rect2)
        janela.blit(texto3, texto_rect3)
    

    pygame.display.flip()
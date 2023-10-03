import pygame
import sys
import subprocess
import json
import os

# Inicialize o Pygame
pygame.init()

largura = pygame.display.Info().current_w
altura = pygame.display.Info().current_h - 60

# Defina as dimensões da janela
janela = pygame.display.set_mode((largura, altura))

#Estou definindo o nome que ficará em cima da janela
pygame.display.set_caption("Jogo da Velha")

# Defina as cores
cor_texto = (255,192,8)
branco = (255, 255, 255)
vermelho = (234,67,53)
azul = (26,115,232)
corBotaoPrincipal = azul
corLingua = azul

# Crie um objeto de fonte
fontTitulo = pygame.font.Font(None, 72)  # Você pode escolher uma fonte e um tamanho aqui
fonteParaOutrasCoisas = pygame.font.Font(None, 32)  # Você pode escolher uma fonte e um tamanho aqui

# Defina o estado inicial do jogo
estado = "menu-pt"

botaoJogadorJogador_rect = pygame.Rect( (largura - 300) // 2 , (altura - 100) // 2, 300, 100)
botaoJogadorComputador_rect = pygame.Rect( (largura - 300) // 2 , (altura - 100) // 2, 300, 100)
botaoLingua_rect = pygame.Rect(largura - 200, 0, 200, 36)

while True:
    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEMOTION:
            if botaoJogadorJogador_rect.collidepoint(event.pos):
                corBotaoPrincipal = vermelho
            else:
                corBotaoPrincipal = azul

            if botaoLingua_rect.collidepoint(event.pos):
                corLingua = vermelho
            else:
                corLingua = azul

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and estado != "jogo":

            if botaoJogadorJogador_rect.collidepoint(event.pos):
                dados = {
                            "lingua": estado,
                }
                nome_arquivo = "dados.json"
                caminho_pasta = ""
                caminho_completo = os.path.join(caminho_pasta, nome_arquivo)
                estado = "jogo"
                with open(caminho_completo, "w") as arquivo_json:
                    json.dump(dados, arquivo_json)
                print(caminho_completo)
                pygame.quit()
                subprocess.call(["python", "jogo.py"])
                sys.exit()

            if botaoLingua_rect.collidepoint(event.pos):
                estado = ("menu-pt" if estado == "menu-en" else "menu-en")

    # Lógica de renderização de acordo com o estado atual
    if estado == "menu-pt":
        texto = fontTitulo.render("Seja muito bem-vindo ao Jogo da Velha!", True, cor_texto)
        texto1 = fonteParaOutrasCoisas.render("Mudar lingua", True, branco)
        texto2 = fonteParaOutrasCoisas.render("Jogador contra Jogador", True, branco)
        texto3 = fonteParaOutrasCoisas.render("Jogador contra Computador", True, branco)
    elif estado == "menu-en":
        texto = fontTitulo.render("Welcome to Tic Tac Toe!", True, cor_texto)
        texto1 = fonteParaOutrasCoisas.render("Change Language", True, branco)
        texto2 = fonteParaOutrasCoisas.render("Player vs Player", True, branco)
        texto2 = fonteParaOutrasCoisas.render("Player vs Computer", True, branco)


    if estado[:4] == "menu":
        
        janela.fill((32,33,36))

        pygame.draw.rect(janela, corBotaoPrincipal, botaoJogadorJogador_rect)
        pygame.draw.rect(janela, corLingua, botaoLingua_rect)

        texto_rect = texto.get_rect()
        texto_rect1 = texto1.get_rect()
        texto_rect2 = texto2.get_rect()

        texto_rect.center = (largura // 2, altura // 6)
        texto_rect1.center = (largura - 100, 20)
        texto_rect2.center = ((largura - 200) // 2 + 100.5 , ((altura - 100) + (100 - 32)) // 2 + 10)
    
        janela.blit(texto, texto_rect)
        janela.blit(texto1, texto_rect1)
        janela.blit(texto2, texto_rect2)
    
    
    elif estado == "jogo":
        
        janela.fill((32,33,36))
        # Renderize a janela do jogo aqui



    pygame.display.flip()

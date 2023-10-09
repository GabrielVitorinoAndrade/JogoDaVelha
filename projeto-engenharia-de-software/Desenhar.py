import pygame

class Colors:
    def __init__(self):
        self.preto = (32, 33, 36)
        self.branco = (255, 255, 255)
        self.verde = (58, 171, 87)
        self.vermelho = (234,67,53)
        self.azul = (26,115,232) 
        self.texto = (255,192,8)

Cor = Colors()

class Desenhar:
    def __init__(self):
        self.larguraFiguras = 10

    
    # Pinta um X de tamanho 50 e largura 10, a partir de uma coordenada dada
    def pintarX(self, coordenadaX, coordenadaY, window):
        pygame.draw.line(window, Cor.vermelho, (coordenadaX, coordenadaY), (coordenadaX + 50, coordenadaY + 50), self.larguraFiguras)
        pygame.draw.line(window, Cor.vermelho, (coordenadaX + 50, coordenadaY), (coordenadaX, coordenadaY + 50), self.larguraFiguras)


    # Pinta um O (Coroa circular), círculo de raio 25 e coroa de largura 10, centrado em uma coordenada dada
    def pintarO(self, coordenadaX, coordenadaY, window):
        pygame.draw.circle(window, Cor.azul, (coordenadaX, coordenadaY), 25)
        pygame.draw.circle(window, Cor.preto, (coordenadaX, coordenadaY), 25 - self.larguraFiguras)



    # Pinta a grade do tabuleiro
    def pintarTabuleiro(self, window):
        pygame.draw.line(window, Cor.branco, (205, 50), (205, 521), 10)
        pygame.draw.line(window, Cor.branco, (365, 50), (365, 521), 10)
        pygame.draw.line(window, Cor.branco, (50, 205), (521, 205), 10)
        pygame.draw.line(window, Cor.branco, (50, 365), (521, 365), 10)


    # Limpa as figuras do tabuleiro
    def apagarFiguras(self, window):
        # Blocos de Seleção - Linha 1 - Coluna 1
        pygame.draw.rect(window, Cor.preto, (50, 50, 150, 150))
        # Blocos de Seleção - Linha 1 - Coluna 2
        pygame.draw.rect(window, Cor.preto, (211, 50, 150, 150))
        # Blocos de Seleção - Linha 1 - Coluna 3
        pygame.draw.rect(window, Cor.preto, (371, 50, 150, 150))
        # Blocos de Seleção - Linha 2 - Coluna 1
        pygame.draw.rect(window, Cor.preto, (50, 211, 150, 150))
        # Blocos de Seleção - Linha 2 - Coluna 2
        pygame.draw.rect(window, Cor.preto, (211, 211, 150, 150))
        # Blocos de Seleção - Linha 2 - Coluna 3
        pygame.draw.rect(window, Cor.preto, (371, 211, 150, 150))
        # Blocos de Seleção - Linha 3 - Coluna 1
        pygame.draw.rect(window, Cor.preto, (50, 371, 150, 150))
        # Blocos de Seleção - Linha 3 - Coluna 2
        pygame.draw.rect(window, Cor.preto, (211, 371, 150, 150))
        # Blocos de Seleção - Linha 3 - Coluna 3
        pygame.draw.rect(window, Cor.preto, (371, 371, 150, 150))


    # # Pinta um traço verde ao final para mostrar como o jogador ganhou
    # def pintarRetaFinal(self):
        
    #     # Ainda falta o resto aqui, calma
import pygame
import json
import random
from Desenhar import Colors
from Desenhar import Desenhar

Cor = Colors()
Desenho = Desenhar()

class EstruturaJogo:

    # Método construtor da classe
    def __init__(self):
        self.matrizJogo = [[0,0,0], [0,0,0], [0,0,0]]
        self.arrayPlacar = [0, 0, 0]
        self.simboloQueVaiJogar = 1
        self.fim = 0
        self.textos = []

        with open('dados.json', 'r') as arquivo:
            dados = json.load(arquivo)

        self.language = dados["lingua"]


    def colocarJogadaNoTabuleiro(self, posicao, simbolo, window):
        if posicao == 1: self.matrizJogo[0][0] = simbolo
        elif posicao == 2: self.matrizJogo[0][1] = simbolo
        elif posicao == 3: self.matrizJogo[0][2] = simbolo
        elif posicao == 4: self.matrizJogo[1][0] = simbolo
        elif posicao == 5: self.matrizJogo[1][1] = simbolo
        elif posicao == 6: self.matrizJogo[1][2] = simbolo
        elif posicao == 7: self.matrizJogo[2][0] = simbolo
        elif posicao == 8: self.matrizJogo[2][1] = simbolo
        elif posicao == 9: self.matrizJogo[2][2] = simbolo
        
        self.pintarQuadrado(simbolo, posicao, window)

        #resultado = self.verificarVitoria(window)
        #print(resultado)

        self.simboloQueVaiJogar = self.trocaSimbolo()

    
    def limparMatriz(self): self.matrizJogo = [[0,0,0], [0,0,0], [0,0,0]]


    def bloquearTabuleiro(self): self.matrizJogo = [[3,3,3], [3,3,3], [3,3,3]]

    
    def trocaSimbolo(self):
        if (self.simboloQueVaiJogar == 1): return 2
        elif (self.simboloQueVaiJogar == 2): return 1
        

    def incrementarPlacarAtual(self, quemVenceu, window):
        if quemVenceu == 1:
            self.arrayPlacar[1] = self.arrayPlacar[1] + 1
            self.mudarPlacar(window)
        elif quemVenceu == 2:
            self.arrayPlacar[2] = self.arrayPlacar[2] + 1
            self.mudarPlacar(window)     


    def verificarSeHaEspacosVazios(self):
        veredito = True

        for linha in self.matrizJogo:
            for elemento in linha:
                if elemento == 0:
                    veredito = False
                    break
            if veredito == False:
                break

        return veredito
    
    
    def verificarVitoria(self, window):
        aux = 0
            #Linha 1
        if (self.matrizJogo[0][0] == 1 and self.matrizJogo[0][1] == 1 and self.matrizJogo[0][2] == 1 and self.fim == 0 
            or self.matrizJogo[0][0] == 2 and self.matrizJogo[0][1] == 2 and self.matrizJogo[0][2] == 2 and self.fim == 0
        ):
            pygame.draw.line(window, Cor.verde, (100, 125), (470, 125), 10)
            aux = 1
        
            #Linha 2
        elif (self.matrizJogo[1][0] == 1 and self.matrizJogo[1][1] == 1 and self.matrizJogo[1][2] == 1 and self.fim == 0
            or self.matrizJogo[1][0] == 2 and self.matrizJogo[1][1] == 2 and self.matrizJogo[1][2] == 2 and self.fim == 0
        ):
            pygame.draw.line(window, Cor.verde, (100, 286), (470, 286), 10)
            aux = 1
        
            #Linha 3
        elif (self.matrizJogo[2][0] == 1 and self.matrizJogo[2][1] == 1 and self.matrizJogo[2][2] == 1 and self.fim == 0
            or self.matrizJogo[2][0] == 2 and self.matrizJogo[2][1] == 2 and self.matrizJogo[2][2] == 2 and self.fim == 0
        ):
            pygame.draw.line(window, Cor.verde, (100, 447), (470, 447), 10)
            aux = 1       
        
            #Coluna 1 
        elif (self.matrizJogo[0][0] == 1 and self.matrizJogo[1][0] == 1 and self.matrizJogo[2][0] == 1 and self.fim == 0
            or self.matrizJogo[0][0] == 2 and self.matrizJogo[1][0] == 2 and self.matrizJogo[2][0] == 2 and self.fim == 0
        ):
            pygame.draw.line(window, Cor.verde, (125, 100), (125, 472), 10)
            aux = 1

            #Coluna 2
        elif (self.matrizJogo[0][1] == 1 and self.matrizJogo[1][1] == 1 and self.matrizJogo[2][1] == 1 and self.fim == 0
            or self.matrizJogo[0][1] == 2 and self.matrizJogo[1][1] == 2 and self.matrizJogo[2][1] == 2 and self.fim == 0
        ):
            pygame.draw.line(window, Cor.verde, (286, 100), (286, 472), 10)
            aux = 1
            
            #Coluna 3
        elif (self.matrizJogo[0][2] == 1 and self.matrizJogo[1][2] == 1 and self.matrizJogo[2][2] == 1 and self.fim == 0
            or self.matrizJogo[0][2] == 2 and self.matrizJogo[1][2] == 2 and self.matrizJogo[2][2] == 2 and self.fim == 0
        ):
            pygame.draw.line(window, Cor.verde, (446, 100), (446, 472), 10)
            aux = 1
        
            #Diagonal 1
        elif (self.matrizJogo[0][0] == 1 and self.matrizJogo[1][1] == 1 and self.matrizJogo[2][2] == 1 and self.fim == 0
            or self.matrizJogo[0][0] == 2 and self.matrizJogo[1][1] == 2 and self.matrizJogo[2][2] == 2 and self.fim == 0
        ):    
            pygame.draw.line(window, Cor.verde, (100, 100), (471, 472), 10)
            aux = 1
        
            #Diagonal 2
        elif (self.matrizJogo[2][0] == 1 and self.matrizJogo[1][1] == 1 and self.matrizJogo[0][2] == 1 and self.fim == 0
            or self.matrizJogo[2][0] == 2 and self.matrizJogo[1][1] == 2 and self.matrizJogo[0][2] == 2 and self.fim == 0
        ):   
            pygame.draw.line(window, Cor.verde, (100, 472), (471, 100), 10)
            aux = 1
      
        elif self.verificarSeHaEspacosVazios(): self.fim = 1

        if (aux == 1):
            if self.quemGanhou() == 1: 
                self.incrementarPlacarAtual(1, window)
                self.simboloQueVaiJogar = 1
            else: 
                self.incrementarPlacarAtual(2, window)
                self.simboloQueVaiJogar = 2
            self.fim = 1
            self.bloquearTabuleiro()
           
    
    def pintarQuadrado(self, simbolo, numero, window):
        if simbolo == 1:
            if numero == 1: Desenho.pintarX(100, 100, window)
            elif numero == 2: Desenho.pintarX(261, 100, window)
            elif numero == 3: Desenho.pintarX(421, 100, window)             
            elif numero == 4: Desenho.pintarX(100, 261, window)
            elif numero == 5: Desenho.pintarX(261, 261, window)
            elif numero == 6: Desenho.pintarX(421, 261, window)
            elif numero == 7: Desenho.pintarX(100, 422, window)
            elif numero == 8: Desenho.pintarX(261, 422, window)
            elif numero == 9: Desenho.pintarX(421, 422, window)
        elif simbolo == 2:
            if numero == 1: Desenho.pintarO(125, 125, window)
            elif numero == 2: Desenho.pintarO(286, 125, window)
            elif numero == 3: Desenho.pintarO(446, 125, window)
            elif numero == 4: Desenho.pintarO(125, 286, window)
            elif numero == 5: Desenho.pintarO(286, 286, window)
            elif numero == 6: Desenho.pintarO(446, 286, window)
            elif numero == 7: Desenho.pintarO(125, 447, window)
            elif numero == 8: Desenho.pintarO(286, 447, window)
            elif numero == 9: Desenho.pintarO(446, 447, window)


    def pintarSimboloDaVez(self, window):
        if self.simboloQueVaiJogar == 1 and self.fim == 0:
            pygame.draw.rect(window, Cor.preto, (645, 72, 70, 60))
            pygame.draw.line(window, Cor.vermelho, (650, 75), (700, 125), 10)
            pygame.draw.line(window, Cor.vermelho, (700, 75), (650, 125), 10)
        elif self.simboloQueVaiJogar == 2 and self.fim == 0:
            pygame.draw.rect(window, Cor.preto, (645, 72, 70, 60))
            pygame.draw.circle(window, Cor.azul, (675, 100), 25)
            pygame.draw.circle(window, Cor.preto, (675, 100), 15)
        elif self.fim == 1:
            pygame.draw.rect(window, Cor.preto, (645, 72, 70, 60))


    def mudarPlacar(self, window):    
        fontePlacar = pygame.font.Font(None, 50)
        pygame.draw.rect(window, Cor.preto, (1012, 72, 84, 60))##############
        texto3 = fontePlacar.render(f"{self.arrayPlacar[1]} x {self.arrayPlacar[2]}", True, Cor.branco)
        texto3_rect = texto3.get_rect()
        texto3_rect.center = (1050, 100)
        window.blit(texto3, texto3_rect)

    
    def textosLingua(self):
        if self.language == "menu-en":
            self.textos = ["  TURN: ", "SCOREBOARD"]
        else:
            self.textos = ["VEZ DO: ", "PLACAR"]


    def quemGanhou(self):
        # Linha 1 com X
        if (self.matrizJogo[0][0] == 1 and self.matrizJogo[0][1] == 1 and self.matrizJogo[0][2] == 1): return 1

        # Linha 1 com O
        elif (self.matrizJogo[0][0] == 2 and self.matrizJogo[0][1] == 2 and self.matrizJogo[0][2] == 2): return 2

        # Linha 2 com X
        elif (self.matrizJogo[1][0] == 1 and self.matrizJogo[1][1] == 1 and self.matrizJogo[1][2] == 1): return 1

        # Linha 2 com O
        elif (self.matrizJogo[1][0] == 2 and self.matrizJogo[1][1] == 2 and self.matrizJogo[1][2] == 2): return 2

        # Linha 3 com X
        elif (self.matrizJogo[2][0] == 1 and self.matrizJogo[2][1] == 1 and self.matrizJogo[2][2] == 1): return 1

        # Linha 3 com O
        elif (self.matrizJogo[2][0] == 2 and self.matrizJogo[2][1] == 2 and self.matrizJogo[2][2] == 2): return 2

        # Coluna 1 com X
        elif (self.matrizJogo[0][0] == 1 and self.matrizJogo[1][0] == 1 and self.matrizJogo[2][0] == 1): return 1

        # Coluna 1 com O
        elif (self.matrizJogo[0][0] == 2 and self.matrizJogo[1][0] == 2 and self.matrizJogo[2][0] == 2): return 2

        # Coluna 2 com X
        elif (self.matrizJogo[0][1] == 1 and self.matrizJogo[1][1] == 1 and self.matrizJogo[2][1] == 1): return 1

        # Coluna 2 com O
        elif (self.matrizJogo[0][1] == 2 and self.matrizJogo[1][1] == 2 and self.matrizJogo[2][1] == 2): return 2

        # Coluna 3 com X
        elif (self.matrizJogo[0][2] == 1 and self.matrizJogo[1][2] == 1 and self.matrizJogo[2][2] == 1): return 1

        # Coluna 3 com O
        elif (self.matrizJogo[0][2] == 2 and self.matrizJogo[1][2] == 2 and self.matrizJogo[2][2] == 2): return 2

        # Diagonal 1 com X
        elif (self.matrizJogo[0][0] == 1 and self.matrizJogo[1][1] == 1 and self.matrizJogo[2][2] == 1):return 1

        # Diagonal 1 com O
        elif (self.matrizJogo[0][0] == 2 and self.matrizJogo[1][1] == 2 and self.matrizJogo[2][2] == 2): return 2

        # Diagonal 2 com X
        elif (self.matrizJogo[2][0] == 1 and self.matrizJogo[1][1] == 1 and self.matrizJogo[0][2] == 1): return 1
        
        # Diagonal 2 com O
        elif (self.matrizJogo[2][0] == 2 and self.matrizJogo[1][1] == 2 and self.matrizJogo[0][2] == 2): return 2
        

    def verificaSeSelecionouBloco(self, window):
        # Declarando mouse
        mouse = pygame.mouse.get_pos()      # POSIÇÃO DO MOUSE
        # Declarando click do mouse
        click = pygame.mouse.get_pressed()  # CLICKES DO MOUSE   

        # Blocos de Seleção - Linha 1 - Coluna 1
        if 50 <= mouse[0] <= 200 and 50 <= mouse[1] <= 200:
            if click[0] == 1 and self.matrizJogo[0][0] == 0:
                self.colocarJogadaNoTabuleiro(1, self.simboloQueVaiJogar, window)

        # Blocos de Seleção - Linha 1 - Coluna 2
        if 211 <= mouse[0] <= 360 and 50 <= mouse[1] <= 200:
            if click[0] == 1 and self.matrizJogo[0][1] == 0:
                self.colocarJogadaNoTabuleiro(2, self.simboloQueVaiJogar, window)                

        # Blocos de Seleção - Linha 1 - Coluna 3
        if 371 <= mouse[0] <= 520 and 50 <= mouse[1] <= 200:
            if click[0] == 1 and self.matrizJogo[0][2] == 0:
                self.colocarJogadaNoTabuleiro(3, self.simboloQueVaiJogar, window)                

        # Blocos de Seleção - Linha 2 - Coluna 1
        if 50 <= mouse[0] <= 200 and 211 <= mouse[1] <= 361:
            if click[0] == 1 and self.matrizJogo[1][0] == 0:
                self.colocarJogadaNoTabuleiro(4, self.simboloQueVaiJogar, window)                

        # Blocos de Seleção - Linha 2 - Coluna 2
        if 211 <= mouse[0] <= 360 and 211 <= mouse[1] <= 361:
            if click[0] == 1 and self.matrizJogo[1][1] == 0:
                self.colocarJogadaNoTabuleiro(5, self.simboloQueVaiJogar, window)                

        # Blocos de Seleção - Linha 2 - Coluna 3
        if 371 <= mouse[0] <= 520 and 211 <= mouse[1] <= 361:
            if click[0] == 1 and self.matrizJogo[1][2] == 0:
                self.colocarJogadaNoTabuleiro(6, self.simboloQueVaiJogar, window)                

        # Blocos de Seleção - Linha 3 - Coluna 1
        if 50 <= mouse[0] <= 200 and 371 <= mouse[1] <= 521:
            if click[0] == 1 and self.matrizJogo[2][0] == 0:
                self.colocarJogadaNoTabuleiro(7, self.simboloQueVaiJogar, window)                

        # Blocos de Seleção - Linha 3 - Coluna 2
        if 211 <= mouse[0] <= 360 and 371 <= mouse[1] <= 521:
            if click[0] == 1 and self.matrizJogo[2][1] == 0:
                self.colocarJogadaNoTabuleiro(8, self.simboloQueVaiJogar, window)                

        # Blocos de Seleção - Linha 3 - Coluna 3
        if 371 <= mouse[0] <= 520 and 371 <= mouse[1] <= 521:
            if click[0] == 1 and self.matrizJogo[2][2] == 0:
                self.colocarJogadaNoTabuleiro(9, self.simboloQueVaiJogar, window)
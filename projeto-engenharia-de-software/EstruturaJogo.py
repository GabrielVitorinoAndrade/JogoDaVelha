import pygame
import json

preto = (32,33,36)
vermelho = (234,67,53)
azul = (26,115,232)
branco = (255, 255, 255)

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
        if posicao == 1:
            self.matrizJogo[0][0] = simbolo
        elif posicao == 2:
            self.matrizJogo[0][1] = simbolo
        elif posicao == 3:
            self.matrizJogo[0][2] = simbolo
        elif posicao == 4:
            self.matrizJogo[1][0] = simbolo
        elif posicao == 5:
            self.matrizJogo[1][1] = simbolo
        elif posicao == 6:
            self.matrizJogo[1][2] = simbolo
        elif posicao == 7:
            self.matrizJogo[2][0] = simbolo
        elif posicao == 8:
            self.matrizJogo[2][1] = simbolo
        elif posicao == 9:
            self.matrizJogo[2][2] = simbolo
        
        self.pintarQuadrado(simbolo, posicao, window)

        resultado = self.verificarVitoria(window)
        print(resultado)

        self.simboloQueVaiJogar == self.simboloDaVez(self.simboloQueVaiJogar) ##Indo para o 2 caso seja 1, Indo para 1 caso seja 2
    
    def limparTabuleiro(self):
        self.matrizJogo = [[0,0,0], [0,0,0], [0,0,0]]
    
    def simboloDaVez(self, simbolo):
        self.simboloQueVaiJogar = (1 if simbolo == 2 else 2)

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
        
            #Coluna 1 
        if (self.matrizJogo[0][0] == 1 and self.matrizJogo[1][0] == 1 and self.matrizJogo[2][0] == 1) or (self.matrizJogo[0][0] == 2 and self.matrizJogo[1][0] == 2 and self.matrizJogo[2][0] == 2):
            if self.matrizJogo[0][0] == 1:
                self.incrementarPlacarAtual(1, window)
            else:
                self.incrementarPlacarAtual(2, window)
            return "VITORIA"

            #Coluna 2
        if (self.matrizJogo[0][1] == 1 and self.matrizJogo[1][1] == 1 and self.matrizJogo[2][1] == 1) or (self.matrizJogo[0][1] == 2 and self.matrizJogo[1][1] == 2 and self.matrizJogo[2][1] == 2):
            if self.matrizJogo[0][1] == 1:
                self.incrementarPlacarAtual(1, window)
            else:
                self.incrementarPlacarAtual(2, window)
            return "VITORIA"    
            
            #Coluna 3
        if (self.matrizJogo[0][2] == 1 and self.matrizJogo[1][2] == 1 and self.matrizJogo[2][2] == 1) or (self.matrizJogo[0][2] == 2 and self.matrizJogo[1][2] == 2 and self.matrizJogo[2][2] == 2):
            if self.matrizJogo[0][2] == 1:
                self.incrementarPlacarAtual(1, window)
            else:
                self.incrementarPlacarAtual(2, window)
            return "VITORIA"
            #Linha 1
        if (self.matrizJogo[0][0] == 1 and self.matrizJogo[0][1] == 1 and self.matrizJogo[0][2] == 1) or (self.matrizJogo[0][0] == 2 and self.matrizJogo[0][1] == 2 and self.matrizJogo[0][2] == 2):
            if self.matrizJogo[0][0] == 1:
                self.incrementarPlacarAtual(1, window)
            else:
                self.incrementarPlacarAtual(2, window)
            return "VITORIA"
            #Linha 2
        if (self.matrizJogo[1][0] == 1 and self.matrizJogo[1][1] == 1 and self.matrizJogo[1][2] == 1) or (self.matrizJogo[1][0] == 2 and self.matrizJogo[1][1] == 2 and self.matrizJogo[1][2] == 2):
            if self.matrizJogo[1][0] == 1:
                self.incrementarPlacarAtual(1, window)
            else:
                self.incrementarPlacarAtual(2, window)
            return "VITORIA"
            #Linha 3
        if (self.matrizJogo[2][0] == 1 and self.matrizJogo[2][1] == 1 and self.matrizJogo[2][2] == 1) or (self.matrizJogo[2][0] == 2 and self.matrizJogo[2][1] == 2 and self.matrizJogo[2][2] == 2):
            if self.matrizJogo[2][0] == 1:
                self.incrementarPlacarAtual(1, window)
            else:
                self.incrementarPlacarAtual(2, window)
            return "VITORIA"
            #Diagonal 1
        if (self.matrizJogo[0][0] == 1 and self.matrizJogo[1][1] == 1 and self.matrizJogo[2][2] == 1) or (self.matrizJogo[0][0] == 2 and self.matrizJogo[1][1] == 2 and self.matrizJogo[2][2] == 2):
            if self.matrizJogo[0][0] == 1:
                self.incrementarPlacarAtual(1, window)
            else:
                self.incrementarPlacarAtual(2, window)
            return "VITORIA"
            #Diagonal 2
        if (self.matrizJogo[2][0] == 1 and self.matrizJogo[1][1] == 1 and self.matrizJogo[0][2] == 1) or (self.matrizJogo[2][0] == 2 and self.matrizJogo[1][1] == 2 and self.matrizJogo[0][2] == 2):
            if self.matrizJogo[2][0] == 1:
                self.incrementarPlacarAtual(1, window)
            else:
                self.incrementarPlacarAtual(2, window)
            return "VITORIA"
      
        if self.verificarSeHaEspacosVazios():
            self.fim = 1
            # self.limparTabuleiro()
            return "EMPATE"
        
        return "CONTINUA"
           
    
    def pintarQuadrado(self, simbolo, numero, window):

        preto = (32,33,36)
        vermelho = (234,67,53)
        azul = (26,115,232) 

        if simbolo == 1:
            if numero == 1:
                pygame.draw.line(window, vermelho, (100, 100), (150, 150), 10)
                pygame.draw.line(window, vermelho, (150, 100), (100, 150), 10)
            elif numero == 2:
                pygame.draw.line(window, vermelho, (261, 100), (311, 150), 10)
                pygame.draw.line(window, vermelho, (311, 100), (261, 150), 10)
            elif numero == 3:
                pygame.draw.line(window, vermelho, (421, 100), (471, 150), 10)
                pygame.draw.line(window, vermelho, (471, 100), (421, 150), 10)                
            elif numero == 4:
                pygame.draw.line(window, vermelho, (100, 311), (150, 261), 10)
                pygame.draw.line(window, vermelho, (150, 311), (100, 261), 10)
            elif numero == 5:
                pygame.draw.line(window, vermelho, (261, 311), (311, 261), 10)
                pygame.draw.line(window, vermelho, (311, 311), (261, 261), 10)
            elif numero == 6:
                pygame.draw.line(window, vermelho, (421, 311), (471, 261), 10)
                pygame.draw.line(window, vermelho, (471, 311), (421, 261), 10)
            elif numero == 7:
                pygame.draw.line(window, vermelho, (100, 472), (150, 422), 10)
                pygame.draw.line(window, vermelho, (150, 472), (100, 422), 10)
            elif numero == 8:
                pygame.draw.line(window, vermelho, (261, 472), (311, 422), 10)
                pygame.draw.line(window, vermelho, (311, 472), (261, 422), 10)
            elif numero == 9:
                pygame.draw.line(window, vermelho, (421, 472), (471, 422), 10)
                pygame.draw.line(window, vermelho, (471, 472), (421, 422), 10)
        elif simbolo == 2:
            if numero == 1:
                pygame.draw.circle(window, azul, (125, 125), 25)
                pygame.draw.circle(window, preto, (125, 125), 15)
            elif numero == 2:
                pygame.draw.circle(window, azul, (286, 125), 25)
                pygame.draw.circle(window, preto, (286, 125), 15)
            elif numero == 3:
                pygame.draw.circle(window, azul, (446, 125), 25)
                pygame.draw.circle(window, preto, (446, 125), 15)
            elif numero == 4:
                pygame.draw.circle(window, azul, (125, 286), 25)
                pygame.draw.circle(window, preto, (125, 286), 15)
            elif numero == 5:
                pygame.draw.circle(window, azul, (286, 286), 25)
                pygame.draw.circle(window, preto, (286, 286), 15)
            elif numero == 6:
                pygame.draw.circle(window, azul, (446, 286), 25)
                pygame.draw.circle(window, preto, (446, 286), 15)
            elif numero == 7:
                pygame.draw.circle(window, azul, (125, 447), 25)
                pygame.draw.circle(window, preto, (125, 447), 15)
            elif numero == 8:
                pygame.draw.circle(window, azul, (286, 447), 25)
                pygame.draw.circle(window, preto, (286, 447), 15)
            elif numero == 9:
                pygame.draw.circle(window, azul, (446, 447), 25)
                pygame.draw.circle(window, preto, (446, 447), 15)

    def pintarSimboloDaVez(self, window):
        if self.simboloQueVaiJogar == 1 and self.fim == 0:
            pygame.draw.rect(window, preto, (645, 72, 70, 60))
            pygame.draw.line(window, vermelho, (650, 75), (700, 125), 10)
            pygame.draw.line(window, vermelho, (700, 75), (650, 125), 10)
        elif self.simboloQueVaiJogar == 2 and self.fim == 0:
            pygame.draw.rect(window, preto, (645, 72, 70, 60))
            pygame.draw.circle(window, azul, (675, 100), 25)
            pygame.draw.circle(window, preto, (675, 100), 15)
        elif self.fim == 1:
            pygame.draw.rect(window, preto, (645, 72, 70, 60))

    def mudarPlacar(self, window):
    
        fontePlacar = pygame.font.Font(None, 50)
        pygame.draw.rect(window, preto, (1012, 72, 84, 60))##############
        texto3 = fontePlacar.render(f"{self.arrayPlacar[1]} x {self.arrayPlacar[2]}", True, branco)
        texto3_rect = texto3.get_rect()
        texto3_rect.center = (1050, 100)
        window.blit(texto3, texto3_rect)
    
    def textosLingua(self):
        if self.language == "menu-en":
            self.textos = ["  TURN: ", "SCOREBOARD"]
        else:
            self.textos = ["VEZ DO: ", "PLACAR"]

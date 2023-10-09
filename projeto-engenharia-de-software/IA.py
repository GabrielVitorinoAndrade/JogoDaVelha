import pygame
import json
import random
from Desenhar import Colors
from Desenhar import Desenhar
from EstruturaJogo import EstruturaJogo

Cor = Colors()
Desenho = Desenhar()

class IA:
    def __init__(self):
        self.teste = 0


    def getBoardCopy(self, board):
        #Faz uma copia do quadro e retrona esta copia
        dupeBoard = [row[:] for row in board]
        return dupeBoard


    def isSpaceFree(self, board, move):
        #Retorna true se o espaco solicitado esta livre no quadro
        x = (int)((move - 1) / 3)
        y = (int)((move - 1) % 3)

        #print(x, "x")
        #print(y, "y")

        if(board[x][y] == 0): return True
        else: return False
        

    def makeMove(self, board, letter, move):
        #Faz o movimento do computador ou do jogador a depender do letter no quadro
        x = (int)((move - 1) / 3)
        y = (int)((move - 1) % 3)

        board[x][y] = letter


    def isWinner(self, brd, let):
        #Dado um quadro e uma letra, esta funcao retorna True se a letra passada vence o jogo
        return((brd[0][0] == let and brd[0][1] == let and brd[0][2] == let) or #linha de cima
            (brd[1][0] == let and brd[1][1] == let and brd[1][2] == let) or #linha do meio
            (brd[2][0] == let and brd[2][1] == let and brd[2][2] == let) or #linha de baixo
            (brd[0][0] == let and brd[1][0] == let and brd[2][0] == let) or #coluna da esquerda
            (brd[0][1] == let and brd[1][1] == let and brd[2][1] == let) or #coluna do meio
            (brd[0][2] == let and brd[1][2] == let and brd[2][2] == let) or #coluna da direita
            (brd[0][0] == let and brd[1][1] == let and brd[2][2] == let) or #diagonal principal
            (brd[0][2] == let and brd[1][1] == let and brd[2][0] == let)) #diagonal secundaria
    

    def possiveisOpcoes(self, board):
        #Retorna uma lista com todos os espacos no quadro que estao disponiveis
        opcoes = []

        for i in range(1, 10):
            if self.isSpaceFree(board, i):
                opcoes.append(i)

        return opcoes
    

    def isBoardFull(self, board):
        #Retorna True se todos os espacos do quadro estao indisponiveis
        for i in range(1, 10):
            if self.isSpaceFree(board, i):
                return False
        return True
    

    def finishGame(self, board, computerLetter):
        #Verifica se o jogo chegou ao final
        #Retorna -1 se o jogador ganha
        #Retorna 1 se o computador ganha
        #Retorna 0 se o jogo termina empatado
        #Retorna None se o jogo nao terminou

        if computerLetter == 1: playerLetter = 0
        else: playerLetter = 1

        if(self.isWinner(board, computerLetter)): return 1
        elif(self.isWinner(board, playerLetter)): return -1
        elif(self.isBoardFull(board)): return 0
        else: return None
    

    def alphabeta(self, board, computerLetter, turn, alpha, beta):
        #Fazemos aqui a poda alphabeta

        if computerLetter == 1: playerLetter = 0
        else: playerLetter = 1

        if turn == computerLetter: nextTurn = playerLetter
        else: nextTurn = computerLetter

        finish = self.finishGame(board, computerLetter)

        if (finish != None): return finish

        possiveis = self.possiveisOpcoes(board)

        if turn == computerLetter:
            for move in possiveis:
                self.makeMove(board, turn, move)
                val = self.alphabeta(board, computerLetter, nextTurn, alpha, beta)
                self.makeMove(board, 0, move)
                if val > alpha:
                    alpha = val

                if alpha >= beta:
                    return alpha
            return alpha

        else:
            for move in possiveis:
                self.makeMove(board, turn, move)
                val = self.alphabeta(board, computerLetter, nextTurn, alpha, beta)
                self.makeMove(board, 0, move)
                if val < beta:
                    beta = val

                if alpha >= beta:
                    return beta
            return beta




    def getComputerMove(self, board, computerLetter):
        #Definimos aqui qual sera o movimento do computador

        a = -2
        opcoes = []

        if computerLetter == 1: playerLetter = 2
        else: playerLetter = 1


        #Comecamos aqui o MiniMax
        #Primeiro chechamos se podemos ganhar no proximo movimento
        for i in range(1, 10):
            copy = self.getBoardCopy(board)
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, computerLetter, i)
                if self.isWinner(copy, computerLetter):
                    return i

        #Checa se o jogador pode vencer no proximo movimento e bloqueia
        for i in range(1, 10):
            copy = self.getBoardCopy(board)
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, playerLetter, i)
                if self.isWinner(copy, playerLetter):
                    return i

        possiveisOpcoesOn = self.possiveisOpcoes(board)

        for move in possiveisOpcoesOn:

            self.makeMove(board, computerLetter, move)
            val = self.alphabeta(board, computerLetter, playerLetter, -2, 2)		
            self.makeMove(board, 0, move)

            if val > a:
                a = val
                opcoes = [move]

            elif val == a:
                opcoes.append(move)

        if (opcoes == []): return -1
        else: return random.choice(opcoes)

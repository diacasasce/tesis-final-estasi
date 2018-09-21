# Motor de ajedrez toma de deciciones
import numpy as np
import chess
from stockfish import Stockfish

class Brain:
    def __init__(self):
        self.sf = Stockfish()
        self.ucim=[]
        self.tablero = chess.Board()
        print(self.tablero)
    def legal(self,mv):
        mov=self.to_move(mv)
        return (mov in self.tablero.legal_moves)
    def legal(self,mv):
        try:
##        lm=str(self.tablero.legal_moves).split(')>')[0].split('(')[1].split(', ')
##        print(lm)
            mm=self.tablero.parse_san(mv)
            rs=True
            print('valido')
        except ValueError:
            print('error')
            rs=False
        return rs
    def mover_uci(self,mv):
        self.ucim.append(mv)
        self.sf.set_position(self.ucim)
        self.tablero.push_uci(mv)
##        print(self.tablero)
    def mover_san(self,san):
        mv=str(self.tablero.parse_san(san))
        self.ucim.append(mv)
        self.sf.set_position(self.ucim)
        self.tablero.push_uci(mv)
##        print(self.tablero)
    def auto(self):
        mv=self.sf.get_best_move()  
##        print(mv)
        return(mv)
    def to_move(self,mv):
        return chess.Move.from_uci(mv)
    def is_over(self):
        return self.tablero.is_game_over()
    def capturo(self,mv):
        if self.tablero.is_capture(mv):
            if self.tablero.is_en_passant(mv):
                return (True,True)
            else:
                return (True,False)
        else:
            return (False,False)
        return 
    def enroque(self,mv):
        if self.tablero.is_kingside_castling(mv):
            return(True,True)
        elif self.tablero.is_queenside_castling(mv):
            return(True,False)
        else:
            return(False,False)
    def fen2board(self):
        fen=self.tablero.fen().split(' ')[0].split('/')
        tab=[]
        brd=[]
        cbrd=[]
        for line in fen:
            ln=[]
            cln=[]
##            print(line)
            tab.append(line)
            for piece in line:
##                print((type(piece),piece))
##                input()
                if piece.isupper():
                    col=1
                else:
                    col=0
                if piece.upper()=='P':
                    ln.append(1)
                    cln.append(col)
                elif piece.upper()=='R':
                    ln.append(2)
                    cln.append(col)
                elif piece.upper()=='N':
                    ln.append(3)
                    cln.append(col)
                elif piece.upper()=='B':
                    ln.append(4)
                    cln.append(col)
                elif piece.upper()=='Q':
                    ln.append(5)
                    cln.append(col)
                elif piece.upper()=='K':
                    ln.append(6)
                    cln.append(col)
                else:
                    for i in range(int(piece)):
                        ln.append(0)
                        cln.append(5)
##            print(ln)
            brd.append(ln)
            cbrd.append(cln)
##        print(brd)
        brd=np.asarray(brd)
        cbrd=np.asarray(cbrd)
        board=brd.copy()
        cboard=cbrd.copy()
        for i in range(0,8):
            board[7-i]=brd[i]
            cboard[7-i]=cbrd[i]
        return (board,cboard)   
        
    
##tablero = chess.Board()
##print(tablero)

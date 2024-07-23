# File: Project2.py
# Student: Diya Sharma 
# UT EID: das5954
# Course Name: CS303E
# 
# Date: 11.07.22 
# Description of Program: Play a game of tictactoe with a computer! Uses a series of functions to generate moves for computer and takes in inputs for user moves. 

import random

HUMAN   = 0
MACHINE = 1

YOU_WON  = "Congratulations! You won!\n"
YOU_LOST = "Sorry! You lost!"
WELCOME = "Welcome to our Tic-Tac-Toe game! \nPlease begin playing."
YOU_TIED = "Looks like a tie.  Better luck next time!" 

def initialBoard():
    return  [ [" ", " ", " "], \
              [" ", " ", " "], \
              [" ", " ", " "] ]

class TicTacToe:
    def __init__(self):
        # Initialize the game with the board and current player
        self._board=initialBoard()
        self._player = HUMAN

    def __str__(self):
        #Return a string representation of the board.
        return self._board[0][0] + "|" + self._board[0][1] + "|" + self._board[0][2] + "\n-----\n" + self._board[1][0] + "|" + self._board[1][1] + "|" + self._board[1][2] + "\n-----\n" + self._board[2][0] + "|" + self._board[2][1] + "|" + self._board[2][2]


    def getPlayer( self ):
        # Return the current player.
        return self._player

    def isWin( self ):
        # See if the board represents a win for the current
        # player. A win is three of the current player's tokens
        # in a single row, column, or either diagonal.
        board = self._board
        token = self._player
        if isWin(board,token):
            return True
        else: return False
    def swapPlayers( self ):
        # Change the current player from HUMAN to MACHINE or
        # vice versa.
        if self._player == HUMAN:
            self._player = MACHINE
        elif self._player == MACHINE:
            self._player = HUMAN
        
    def humanMove( self ):
        # Takes in inputs for human moves and verifies them
        print("Your turn:")
        while True:
            move = input("  Specify a move r, c:")
            move = move.strip()
            if len(move) != 3:
                print("Response should be r, c. Try again!")
                continue
            elif "," in move:
                row,column = move.replace(",", "", 1)
                row = int(row)
                column = int(column)
            else:
                print("Response should be r, c. Try again!")
                continue
            if row>=0 and row<=2 and column>=0 and column<=2:
                if self._board[row][column] == " ":
                    self._board[row][column] = "X"
                    break
                else:
                    print("Illegal move specified.  Try again!")
                    continue
            else:
                print("Illegal move specified.  Try again!")
                continue
            

    def machineMove( self ):
        # This is the MACHINE's move.  It picks squares randomly
        # until it finds an empty one. Update the board appropriately.
        # Note: this is a really dumb way to play tic-tac-toe.  
        print("Machine's turn:")
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            if self._board[r][c] == " ":
                print("  Machine chooses: ", r, ", ", c, sep="")
                self._board[r][c] = "O"
                return

def isRowWin(board,token):
    if board[0][0]+board[0][1]+board[0][2] == "XXX" or board[0][0]+board[0][1]+board[0][2] == "OOO":
        return True
    elif board[1][0]+board[1][1]+board[1][2] == "XXX" or board[1][0]+board[1][1]+board[1][2] == "OOO":
        return True
    elif board[2][0]+board[2][1]+board[2][2] == "XXX" or board[2][0]+board[2][1]+board[2][2] == "OOO":
        return True
    else: return False

def isColumnWin(board,token):
    if board[0][0]+board[1][0]+board[2][0] == "XXX" or board[0][0]+board[1][0]+board[2][0] == "OOO":
        return True
    elif board[0][1]+board[1][1]+board[2][1] == "XXX" or board[0][1]+board[1][1]+board[2][1] == "OOO":
        return True
    elif board[0][2]+board[1][2]+board[2][2] == "XXX" or board[0][2]+board[1][2]+board[2][2] == "OOO":
        return True
    else: return False

def isDiagonalWin(board,token):
    if board[0][0]+board[1][1]+board[2][2] == "XXX" or board[0][0]+board[1][1]+board[2][2] == "OOO":
        return True
    elif board[0][2]+board[1][1]+board[2][0] == "XXX" or board[0][2]+board[1][1]+board[2][0] == "OOO":
        return True
    else: return False

def isWin( board, token ):
    #Combines the above three functions
    if isRowWin( board, token ) or isColumnWin( board, token ) or isDiagonalWin( board, token):
        return True
    else: return False

def driver( ):
    """ This plays tic-tac-toe in a pretty simple-minded
    fashion.  The human player goes first with token "X" and
    alternates with the machine using token "O".  We print
    the board before the first move and after each move. """

    # Print the welcome message
    print( WELCOME )

    # Initialize the board and current player
    ttt = TicTacToe()
    print( ttt )

    # There are up to 9 moves in tic-tac-toe.
    for move in range(9):
        # Whether player is human
        if ttt.getPlayer() == HUMAN:
            # If HUMAN, take a move, print the board,
            # and see if it's a win.
            ttt.humanMove()
            print(ttt)
            if ttt.isWin():
                print( YOU_WON )
                return
        else:
            # Else MACHINE takes a move.  Print the
            # board and see if the machine won.
            ttt.machineMove()
            print(ttt)
            if ttt.isWin():
                print( YOU_LOST )
                return
        # Swap players.
        ttt.swapPlayers()

    # After nine moves with no winner, it's a tie.
    print( YOU_TIED )
    
driver()

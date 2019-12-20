#board[x][y] means x,y coordinate on the board
victoryRed = 1 #assuming red player not winning is 1, winning is 2 
Red = 1 #assuming red player uses number 1 
victoryBlue =3 #assuming blue player not winning is 3, winning is 4
Blue = 2 #assuming blue player uses number 2
victory = 0 # 2 means Red wins, 4 means Blue wins, 5 means draw
def check_victory (board,rows,coloumns,turns):
    for rownum in range (0,6): #for 6 rows in the board 
        for colonum in range (0,7): #for 7 coloumns in the board
            for x in range (0,4):
                if board[rownum+x][colonum] == Red : #searching for victory for 4 red pieces in a row horizontally
                    victoryRed = 2
                                
                elif board[rownum][colonum+x] == Red: #searching for victory for 4 red pieces in a row vertically
                    victoryRed = 2
                    
                elif board[rownum+x][colonum+x] == Red: #searching for victory for 4 red pieces diagonally right
                    victoryRed = 2
                    
                elif board[rownum-x][colonum+x] == Red: #searching for victory for 4 red pieces diagonally left
                    victoryRed = 2
                    
                else : #if no victory conditions found, victory = false.
                    victoryRed = 1
                
            for x in range (0,4):
                if board[rownum+x][colonum] == Blue : #searching for victory for 4 Blue pieces in a row horizontally
                    victoryBlue = 4
                                
                elif board[rownum][colonum+x] == Blue: #searching for victory for 4 Blue pieces in a row vertically
                    victoryBlue = 4
                    
                elif board[rownum+x][colonum+x] == Blue: #searching for victory for 4 Blue pieces diagonally right
                    victoryBlue = 4
                    
                elif board[rownum-x][colonum+x] == Blue: #searching for victory for 4 Blue pieces diagonally left
                    victoryBlue = 4
                    
                else : #if no victory conditions found, victory = false.
                    victoryBlue = 3
    
    if victoryRed == 2 and victoryBlue == 3:
        victory = 2#red player wins
    if victoryRed == 3 and victoryBlue == 4:
        victory = 4#blue player wins    
    if turns == 42 and victoryRed == 1 and victoryBlue == 3 :
        victory = 5 #draw
    return victory
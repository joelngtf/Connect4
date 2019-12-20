  # perfect
import numpy as np
from random import randint 


class Game:
    mat = np.zeros((6, 7))
    rows = 6
    cols = 7
    turn = 1
    wins = 4


my_game = Game()


# The first error check ensures that the input is an integer and that it is within the preset minimum and maximum value. Otherwise, an error message is printed.
def check(a,b):
    x = (input('What column do you want to make your move?'))
    while not x.isdigit() :
      x = (input('What column do you want to make your move?'))
    x = int(x)
    while x not in range(a, b + 1):
        print('Error. The input should be in range of',a, 'and' ,b)
        x = input('What column do you want to make your move?-----')
        x=int(x)
    return x

# The second error check ensures that the input is not an integer and that it is the exact input required. Otherwise, an error message is printed.
def DorP(a, b):
    x = input('POPOUT (P) or DROP (D)')
    while x != a and x != b:
        print('Error. Invalid input.')
        x = input('POPOUT (P) or DROP (D)')
    x.upper()
    if x == a:
      return True
    if x == b:
      return False 


def display_board(my_game):
    for i in my_game.mat[::-1]: 
      print(i)

def apply_move(my_game, col, pop):
    a = True
    b = 0
    if pop:
        for i in range(my_game.rows - 1): 
          my_game.mat[i][col] = my_game.mat[i + 1][col]
          my_game.mat[i+1][col] = 0
    else:
        while a:
        #for i in range(my_game.rows):
            if my_game.mat[b][col] == 0 and my_game.mat[my_game.rows-1][col] == 0:
                my_game.mat[b][col] = my_game.turn
                a = False
            else:
                b += 1
                if b == my_game.rows:
                 a = False
    my_game.turn += 2
    my_game.turn %= 2 
    my_game.turn += 1 
    return my_game

def check_move(my_game, col, pop):
    if col not in range(my_game.cols):
        return False
    elif pop:
        a = 0
        if my_game.mat[0][col] != my_game.turn:
          a +=1
        return a == 0
    else:
        b = 0
        if my_game.mat[-1][col] != 0: 
          b += 1
        return b == 0 

def check_victory(my_game):
    piece = 3 - my_game.turn
    ano_piece = my_game.turn 
    #Check vertical piece
    for c in range(my_game.cols):
        for r in range(my_game.rows - 3):
            if my_game.mat[r][c] == piece and my_game.mat[r+1][c] == piece and my_game.mat[r+2][c] == piece and my_game.mat[r+3][c] == piece:
                return piece
    #Check horizontal piece
    for c in range(my_game.cols - 3):
        for r in range(my_game.rows):
            if my_game.mat[r][c] == piece and my_game.mat[r][c+1] == piece and my_game.mat[r][c+2] == piece and my_game.mat[r][c+3] == piece:
                return piece          
    #Check sloped piece
    for c in range(my_game.cols - 3):
        for r in range(my_game.rows - 3):
            if my_game.mat[r][c] == piece and my_game.mat[r+1][c+1] == piece and my_game.mat[r+2][c+2] == piece and my_game.mat[r+3][c+3] == piece:
                return piece       
    for c in range(my_game.cols - 3):
        for r in range(3, my_game.rows):
            if my_game.mat[r][c] == piece and my_game.mat[r-1][c+1] == piece and my_game.mat[r-2][c+2] == piece and my_game.mat[r-3][c+3] == piece:
                return piece
    #Check vertical ano_piece
    for c in range(my_game.cols):
        for r in range(my_game.rows - 3):
            if my_game.mat[r][c] == ano_piece and my_game.mat[r+1][c] == ano_piece and my_game.mat[r+2][c] == ano_piece and my_game.mat[r+3][c] == ano_piece:
                return ano_piece
    #Check horizontal ano_piece
    for c in range(my_game.cols - 3):
        for r in range(my_game.rows):
            if my_game.mat[r][c] == ano_piece and my_game.mat[r][c+1] == ano_piece and my_game.mat[r][c+2] == ano_piece and my_game.mat[r][c+3] == ano_piece:
                return ano_piece          
    #Check sloped ano_piece
    for c in range(my_game.cols - 3):
        for r in range(my_game.rows - 3):
            if my_game.mat[r][c] == ano_piece and my_game.mat[r+1][c+1] == ano_piece and my_game.mat[r+2][c+2] == ano_piece and my_game.mat[r+3][c+3] == ano_piece:
                return ano_piece       
    for c in range(my_game.cols - 3):
        for r in range(3, my_game.rows):
            if my_game.mat[r][c] == ano_piece and my_game.mat[r-1][c+1] == ano_piece and my_game.mat[r-2][c+2] == ano_piece and my_game.mat[r-3][c+3] == ano_piece:
                return piece
    for c in range(my_game.cols):
      for r in range(my_game.rows):
        if my_game.mat[r][c] == 0:
         return 0
    return 3

def check_victory_human(my_game):
    piece = 1
    #Check vertical 
    for c in range(my_game.cols):
        for r in range(my_game.rows - 3):
            if my_game.mat[r][c] == piece and my_game.mat[r+1][c] == piece and my_game.mat[r+2][c] == piece and my_game.mat[r+3][c] == piece:
                return True
    #Check horizontal 
    piece = 3 - my_game.turn
    for c in range(my_game.cols - 3):
        for r in range(my_game.rows):
            if my_game.mat[r][c] == piece and my_game.mat[r][c+1] == piece and my_game.mat[r][c+2] == piece and my_game.mat[r][c+3] == piece:
                return True            
    #Check sloped 
    for c in range(my_game.cols - 3):
        for r in range(my_game.rows - 3):
            if my_game.mat[r][c] == piece and my_game.mat[r+1][c+1] == piece and my_game.mat[r+2][c+2] == piece and my_game.mat[r+3][c+3] == piece:
                return True        
    for c in range(my_game.cols - 3):
        for r in range(3, my_game.rows):
            if my_game.mat[r][c] == piece and my_game.mat[r-1][c+1] == piece and my_game.mat[r-2][c+2] == piece and my_game.mat[r-3][c+3] == piece:
                return True  
    return False

def computer_move(my_game,b):
  #have to run it many times
  pop = True
  if b == 1:
    col = randint(0,my_game.cols-1)
    a = randint(1,2)
    if a == 1:
      pop = False
    return col,pop
  if b == 2:
    col = randint(0,my_game.cols-1)
    a = randint(1,2)
    if a == 1:
      pop = False
    while check_victory_human(my_game):
       col = randint(0,my_game.cols-1)
       a = randint(1,2)
       if a == 1:
        pop = False
    return col,pop

def menu():
  print("Who do you wish to play against?")
  print("1. Human")
  print("2. Bots")
  r = int(input("Your Input: "))
  if r == 1:
    display_board(my_game)
    while not check_victory(my_game):
        print('This is player',my_game.turn,'turn')
        pop = DorP('P','D') 
        col = check( 0, my_game.cols-1) 
        while not check_move(my_game, col, pop):
            print('Error')
            pop = DorP('P','D')
            col = check( 0, my_game.cols-1 ) 
        
        apply_move(my_game, col, pop)
        display_board(my_game)
        #my_game.turn += 2
        #my_game.turn %= 2 
        #my_game.turn += 1  
    if check_victory(my_game) == 1 or check_victory(my_game) == 2:
        print('%s is the winner!' %(check_victory(my_game)))
    elif check_victory(my_game) == 3:
        print(' Draw ')
  if r == 2:
    print('Which level?')
    print('1. Easy')
    print('2. Hard')
    y = int(input('Your Input: '))
    if y == 1: 
      display_board(my_game)
      while not check_victory(my_game):
       print('This is player',my_game.turn,'turn')
       if my_game.turn == 1:
        pop = DorP('P','D') 
        col = check( 0, my_game.cols-1) 
        while not check_move(my_game, col, pop):
            print('Error')
            pop = DorP('P','D')
            col = check( 0, my_game.cols-1 ) 
        
        apply_move(my_game, col, pop)
        display_board(my_game)
       elif my_game.turn == 2:
        col,pop =  computer_move(my_game,y)
        while not check_move(my_game, col, pop):
            print('Error')
            col,pop =  computer_move(my_game,y)
        apply_move(my_game, col, pop)
        display_board(my_game)    
      if check_victory(my_game) == 1 or check_victory(my_game) == 2:
        print('%s is the winner!!!!' %(check_victory(my_game)))
      elif check_victory(my_game) == 3:
        print(' Draw ')
    if y == 2: 
      display_board(my_game)
      while not check_victory(my_game):
       print('This is player',my_game.turn,'turn')
       if my_game.turn == 1:
        pop = DorP('P','D') 
        col = check( 0, my_game.cols-1) 
        while not check_move(my_game, col, pop):
            print('Error')
            pop = DorP('P','D')
            col = check( 0, my_game.cols-1 ) 
        
        apply_move(my_game, col, pop)
        display_board(my_game)
       elif my_game.turn == 2:
        col,pop =  computer_move(my_game,y)
        while not check_move(my_game, col, pop):
            print('Error')
            col,pop =  computer_move(my_game,y)
        apply_move(my_game, col, pop)
        display_board(my_game)    
      if check_victory(my_game) == 1 or check_victory(my_game) == 2:
        print('%s is the winner!!!!' %(check_victory(my_game)))
      elif check_victory(my_game) == 3:
        print(' Draw ')
        


menu()

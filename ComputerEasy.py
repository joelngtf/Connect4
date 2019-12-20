import numpy as np
from random import randint
def create_board(rows,cols):
 def make_board(): #create a begin board
  board = np.zeros((rows,cols ))
  return board
 
 c = cols
 r = rows

 board = make_board() #create a begin board

 def reverse_board(board): #reverse the board
  return np.flip(board,0)

 def check(board,col): #check the above row are avalable or not
  return board[5][col] == 0

 def player_drop(board,row,col,num): #set the value to board
  board[row][col] = num

 def get_column(board, col): #find the place drop
  for j in range(rows):
    if board[j][col] == 0 :
      return j

 def pop_out(board,col):
   for i in range(rows-1):
    board[i][col] = board[i+1][col]
    board[i+1][col] = 0
 
 def check_bot(board,turn):
   so = 0
   for i in range(7):
     if board[0][i] == turn +1:
       so += 1
   return so > 0
  
 
 game_finished = False
 print(board)
 turn = 0

 while not game_finished: #while game is continuing
  a = 'P1 from 0 to  ' + str(c) + ' :'
  b = 'P2 from 0 to  ' + str(c) + ' :'
  m = True
  if turn == 0:
    out_or_drop = str(input('Out or Drop: O-D'))
    if out_or_drop.upper() == 'O' and check_bot(board,turn):
      pass
    else:
      out_or_drop = 'D'
  elif turn == 1:
    a = randint(1,2)
    if a == 1 and check_bot(board,turn):
      out_or_drop = 'O'
    elif a == 2:
      out_or_drop = 'D' 
    else:
      out_or_drop = 'D'
  if out_or_drop.upper() == 'D':
   if turn == 0:
    print('This is player',turn+1,'turn')
    col = int(input(a))
    while m:
     if col < 0 or col >= c:
      col = int(input(a))
     else:
      if check(board,col):
       row = get_column(board,col)
       player_drop(board,row,col,1)
       m = False
   else:
     print('This is player',turn+1,'turn')
     col = randint(0,6)
     while m:
      if col < 0 or col >= c:
       col = int(input(b))
      else:
       if check(board,col):
        row = get_column(board,col)
        player_drop(board,row,col,2)
        m = False
   print(reverse_board(board))
   turn += 1 #get turn become 1
   turn =  turn%2 #get turn become 0
   #if game finishes, so that game_finished = True, should write the check_victory function outside of while and put it in while to change variable of game_finished
  elif out_or_drop.upper() == 'O':
   if turn == 0:
    print('This is player',turn+1,'turn')
    col = int(input(a))
    while m:
     if col < 0 or col >= c or turn != board[0][col] -1:
      col = int(input(a))
     else:
        pop_out(board,col)
        m = False
   elif turn == 1:
    print('This is player',turn+1,'turn')
    col = randint(0,6)
    while m:
     if col < 0 or col >= c or turn != board[0][col] -1:
      col = randint(0,6)
     else:
        pop_out(board,col)
        m = False 

   print(reverse_board(board))
   turn += 1 #get turn become 1
   turn =  turn%2
        
#if you want the code to be more accurate, we should make the input in range (0,6) in order to drop correctly and continue the game, if not, require player to input again between 0 and 6.
create_board(6,7)
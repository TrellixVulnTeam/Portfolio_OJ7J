import numpy as np # This is a module for Python
import pygame # This is a module for Python
import sys
import math # Needed for advance math


# RGB (Red, Green, Blue)
BLUE = (0,0,255) # The is defining the colors RGB value (Red, Green, Blue) 
BLACK = (0,0,0) # The is defining the colors RGB value (Red, Green, Blue)
RED = (255,0,0) # The is defining the colors RGB value (Red, Green, Blue)
YELLOW = (255,255,0) # The is defining the colors RGB value (Red, Green, Blue)


# Rows and Columns
ROW_COUNT = 6 # This is where you set the number of rows
COLUMN_COUNT = 7 # This is where you set the number of columns


# Defining Variables
def create_board(): # This is where you are defining the variable
    board = np.zeros((ROW_COUNT, COLUMN_COUNT)) # This is where you decide how many rows and colums are displayed (up/down, right/left)
    return board # This is where your returning the function


def drop_piece(board, row, col, piece): # This is where you are defining the variable
    board[row][col] = piece
    

def is_valid_location(board, col): # This is where you are defining the variable
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col): # This is where you are defining the variable
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board): # This is where you are defining the variable
    print(np.flip(board, 0))


def winning_move(board, piece): # This is where you are defining the variable
    
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT): 
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True


    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3): 
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True


    # Check upward diagonal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3): 
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True


    # Check downward diagonal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT): 
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True 


def draw_board(board): # This is where you are defining the variable
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)


    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):    
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board [r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0
pygame.init() # Initialized pygame
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace", 75) # This is how you change the font


# Game Loop
while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()


        if event.type == pygame.MOUSEBUTTONDOWN: 
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            
            # Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
    
                    if winning_move(board, 1): 
                        label = myfont.render("Player 1 Wins!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True
    
    
            # Ask for Player 2 Input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2): 
                        label = myfont.render("Player 2 Wins!", 1, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True


            print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(750) # This is the wait after you win the game and the screen disappears


from Sudoku_Solver import solved_board
import pygame
pygame.init()
from Grid import unsolved_grid as us
display = (460,460)
WIN = pygame.display.set_mode(display)
pygame.display.set_caption("The Sudoku Board")
font = pygame.font.Font("assets/Kalam-Regular.ttf", 40)

#colours
WHITE = (255,255,255)
MILD_BLACK = (96,96,96)
PINK = (0,0,51)
BLACK = (0,0,0)
BLUE = (0,255,255)


def draw_window():    #Makes a window in pygame
    WIN.fill(WHITE)
    filled_box(us)
    grid()
    print_numbers(solved_board)
    pygame.display.update()

def filled_box(board):      # Fill's Blue colour for the numbers which are already in the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                box = pygame.Rect(5+ 50*j , 5 + 50*i , 50 , 50)
                pygame.draw.rect(WIN,BLUE, box)

def print_numbers(board): #prints solved board on the board
    for row in range(9):
        for col in range(9):
            number = board[row][col]
            text = font.render(str(number) , True , (0,0,0))
            WIN.blit(text , pygame.Vector2(col*50 + 24 , row*50 + 7))



def grid():       #Draw's Grid on the surface
    width = 1
    colour = MILD_BLACK
    for i in range(10):
        if i % 3 == 0:
             width = 5
             colour = MILD_BLACK
        else:
            width = 1 
            colour = PINK 

        pygame.draw.line(WIN,colour,(5,5+ 50*i),(455,5 + 50*i),width)
        pygame.draw.line(WIN,colour,(5 + 50*i,5),(5 + 50*i,455),width)

###
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit
main()

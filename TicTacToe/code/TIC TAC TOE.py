import pygame, sys
import numpy as np


pygame.init()


width_board = 600
height_board = 600
line_width = 15
win_line_width = 15
board_rows = 3
board_coloumns = 3
square_size = 200
cirle_radius = 60
circle_width = 15
cross_width = 25
space = 55

red = (255, 0, 0)
background_color = (255, 165, 0)
line_color = (23, 145, 135)
circle_color = (128, 128, 128)
cross_color = (0, 0, 0)


screen = pygame.display.set_mode( (width_board, height_board) )
pygame.display.set_caption( 'Python project' )
screen.fill( background_color )

board = np.zeros( (board_rows, board_coloumns) )


def drawing_lines():
	
	pygame.draw.line( screen, line_color, (0, square_size), (width_board, square_size), line_width )
	
	pygame.draw.line( screen, line_color, (0, 2 * square_size), (width_board, 2 * square_size), line_width)

	pygame.draw.line( screen, line_color, (square_size, 0), (square_size, height_board), line_width )
	
	pygame.draw.line( screen, line_color, (2 * square_size, 0), (2 * square_size, height_board), line_width )

def drawing_figures():
	for row in range(board_rows):
		for col in range(board_coloumns):
			if board[row][col] == 1:
				pygame.draw.circle( screen, circle_color, (int( col * square_size +square_size //2 ), int( row * square_size + square_size//2 )), cirle_radius, circle_width )
			elif board[row][col] == 2:
				pygame.draw.line( screen, cross_color, (col * square_size  + space, row * square_size + square_size - space), (col * square_size + square_size - space, row * square_size + space), cross_width )	
				pygame.draw.line( screen, cross_color, (col * square_size + space, row * square_size + space), (col * square_size + square_size - space, row * square_size + square_size - space), cross_width )

def marking_square(row, col, player):
	board[row][col] = player

def checking_available_square(row, col):
	return board[row][col] == 0

def is_board_full():
	for row in range(board_rows):
		for col in range(board_coloumns):
			if board[row][col] == 0:
				return False

	return True

def check_win(player):
	
	for col in range(board_coloumns):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_winning_line(col, player)
			return True

	
	for row in range(board_rows):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(row, player)
			return True

	
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_ascending_diagonal(player)
		return True

	
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc_diagonal(player)
		return True

	return False

def draw_vertical_winning_line(col, player):
	posX = col *  square_size+ square_size//2

	if player == 1:
		color = circle_color
	elif player == 2:
		color = cross_color

	pygame.draw.line( screen, color, (posX, 15), (posX, height_board - 15), line_width )

def draw_horizontal_winning_line(row, player):
	posY = row  *  square_size+ square_size//2

	if player == 1:
		color = circle_color
	elif player == 2:
		color = cross_color

	pygame.draw.line( screen, color, (15, posY), (width_board - 15, posY), win_line_width )

def draw_ascending_diagonal(player):
	if player == 1:
		color = circle_color
	elif player == 2:
		color = cross_color

	pygame.draw.line( screen, color, (15, height_board - 15), (width_board - 15, 15), win_line_width )

def draw_desc_diagonal(player):
	if player == 1:
		color = circle_color
	elif player == 2:
		color = cross_color

	pygame.draw.line( screen, color, (15, 15), (width_board - 15, height_board - 15), win_line_width )

def starting_new_game():
	screen.fill( background_color )
	drawing_lines()
	for row in range(board_rows):
		for col in range(board_coloumns):
			board[row][col] = 0

drawing_lines()


player = 1
game_over = False


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

			mouseX = event.pos[0] # x
			mouseY = event.pos[1] # y

			clicked_row = int(mouseY // square_size)
			clicked_col = int(mouseX // square_size)

			if checking_available_square( clicked_row, clicked_col ):

				marking_square( clicked_row, clicked_col, player )
				if check_win( player ):
					game_over = True
				player = player % 2 + 1

				drawing_figures()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				starting_new_game()
				player = 1
				game_over = False

	pygame.display.update()

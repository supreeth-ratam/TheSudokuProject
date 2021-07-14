from test import grid
def blank_space(board):          #To find 0's in the board
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row,col)  
    return False

def is_possible(num,blank_pos,board): #checks if the number is valid 
    # checking rows
    for row in range(9):
        if board[blank_pos[0]][row] == num:
            return False
    # checking columns
    for col in range(9):
        if board[col][blank_pos[1]] == num:
            return False
    # checking boxes
    box_row = blank_pos[0]//3
    box_column = blank_pos[1]//3

    for i in range(box_row*3, box_row*3 + 3):
        for j in range(box_column * 3, box_column*3 + 3):
            if board[i][j] == num :
                return False


    return True
def solver(board):  #Solves the board
    if blank_space(board) == False:  
        return True
    else:
        blank_pos = blank_space(board)   
        for i in range(1,10):  
            if is_possible(i,blank_pos,board):    
                board[blank_pos[0]][blank_pos[1]] = i    
                if solver(board):  
                    return True   
                board[blank_pos[0]][blank_pos[1]] = 0  #backtracking
        return False
solver(grid)
solved_board = grid


                






    
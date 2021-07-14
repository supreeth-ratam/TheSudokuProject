f = open("assets/input_sudoku board.txt", "r")
message = f.read()

grid = []
unsolved_grid = []
k = message.split('\n')
for line in k:
    m = line.split(" ")
    l = list(map(int , m))
    grid.append(l)
    unsolved_grid.append(l)

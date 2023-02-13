import random

grid_size = 10
grid = [ ['']*grid_size for i in range(grid_size) ]
twoDarry = [ ['']*grid_size for i in range(grid_size) ]
num_of_ships = 5
ships_sunk = 0
game_over = False
my_grid = "+---"
my_grid2 = "|"

def drawBoard(myBoard):
    game_board = [["+--+--+--+--+--+--+--+--+--+--+--+"],
                  ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
                  ["+--+--+--+--+--+--+--+--+--+--+--+"],
                  ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
                  ["+--+--+--+--+--+--+--+--+--+--+--+"],
                  ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
                  ["+--+--+--+--+--+--+--+--+--+--+--+"],
                  ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
                  ["+--+--+--+--+--+--+--+--+--+--+--+"],
                  ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
                  ["+--+--+--+--+--+--+--+--+--+--+--+"],
                  ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
                  ["+--+--+--+--+--+--+--+--+--+--+--+"],
                  ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
                  ["+--+--+--+--+--+--+--+--+--+--+--+"],
                  ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
                  ["+--+--+--+--+--+--+--+--+--+--+--+"],
                  ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
                  ["+--+--+--+--+--+--+--+--+--+--+--+"],
                  ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
                  ["+--+--+--+--+--+--+--+--+--+--+--+"],
                  ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
                  ["+--+--+--+--+--+--+--+--+--+--+--+"],]
    for i in game_board:
        print(*i)


# def play_game():
#     game_board = [["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],]
#     for i in game_board:
#         print(*i)

# if __name__ == "__main__":
#     play_game()
    

        

def setupBoard(myBoard):
    display_matrix = ()
    for i in range(grid_size):
            for j in range(grid_size):
                print(myBoard[i][j], end = "")
            print()
# initilize the 2 d array (the grid)
    setup_matrix =()
    i = j = 0
    while i < grid_size:
        while j < grid_size:
            # store the string "i, j" into the array
            myBoard[i][j] = str(i) + "," + str(j) + " "
            j += 1
        j = 0
        i += 1
            
def main(myBoard):
    setupBoard(myBoard)
    drawBoard(myBoard)
main(grid)
    
##    grid[i,j] = '.'
##    randomRow = random.randint(0, grid_size - 1)
##    randomCol = random.randint(0, grid_size - 1)
##    myBoard[randomRow][randomCol] = 'S'
    
    

##def hitOrMiss(myBoard, row, col):
##    if grid[row,col] == ".":
##        print("You missed!")
##    elif grid[row,col] == "S":
##        print("Ship sunk!")
##        ships_sunk +=  1
##    
##    
##    
##
##def isGameOver(myBoard):
##    if num_of_ships == ships_sunk:
##              print("You win!")
##              game_over = True
##              
##def main(myBoard):
##    drawBoard(myBoard)
##    setupBoard(myBoard)
##    
    
     

# import random

# grid_size = 10
# grid = [ ['']*grid_size for i in range(grid_size) ]
# ships_sunk = 0
# game_over = False

# def create_ship():
#     return random.randint(0, 9), random.randint(0, 9)
# def rows_and_columns():
#     labels = ()

# def drawBoard():
#     game_board = [["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
#                   ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],]
#     for i in game_board:
#         print(*i)
#     ship1 = create_ship()
#     ship2 = create_ship()
#     ship3 = create_ship()
#     ship4 = create_ship()
#     ship5 = create_ship()
#     num_of_ships = 5

#     while game_over == False:
#         try:
#             row = int(input("Enter a row number between 0-9: "))
#             column = int(input("Enter a column number between 0-9: "))
#         except ValueError:
#             print("Only enter number!")
#             continue

#         if row not in range(0,10) or column not in range(0, 10):
#             print("\nThe numbers must be between 0-9!")
#             continue

#         row = row - 1 # Reducing number to desired index.
#         column = column - 1 # Reducing number to desired index.

#         if game_board[row][column] == "O" or game_board[row][column] == "X":
#             print("\nA shot was used there, try again!\n")
#             continue
#         elif (row, column) == ship1 or (row, column) == ship2 or (row, column) == ship3 or (row, column) == ship4 or (row, column) == ship5:
#             print("\nHit! You've sunk a ship!\n")
#             game_board[row][column] = "X"
#             ships_sunk += 1
#             if ships_sunk == num_of_ships:
#                 print("Congratz, you won! GAME")
#         else:
#             print("\nYou missed!\n")
#             game_board[row][column] = "O"

#         for i in game_board:
#             print(*i)

# if __name__ == "__main__":
#     drawBoard()
    
# def drawBoard():
#     game_board = [["+--+--+--+--+--+--+--+--+--+--+--+"],
#                   ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
#                   ["+--+--+--+--+--+--+--+--+--+--+--+"],
#                   ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
#                   ["+--+--+--+--+--+--+--+--+--+--+--+"],
#                   ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
#                   ["+--+--+--+--+--+--+--+--+--+--+--+"],
#                   ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
#                   ["+--+--+--+--+--+--+--+--+--+--+--+"],
#                   ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
#                   ["+--+--+--+--+--+--+--+--+--+--+--+"],
#                   ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
#                   ["+--+--+--+--+--+--+--+--+--+--+--+"],
#                   ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
#                   ["+--+--+--+--+--+--+--+--+--+--+--+"],
#                   ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
#                   ["+--+--+--+--+--+--+--+--+--+--+--+"],
#                   ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
#                   ["+--+--+--+--+--+--+--+--+--+--+--+"],
#                   ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
#                   ["+--+--+--+--+--+--+--+--+--+--+--+"],
#                   ["| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| ", "| "],
#                   ["+--+--+--+--+--+--+--+--+--+--+--+"],]
#     for i in game_board:
#         print(*i)

# if __name__ == "__main__":
#     drawBoard()
def begining():
    """
    Introduction to the game:
    Welcome message and game rules.

    """
    print("Welcome to TIC TAC TOE\n")
    print("Rules of the game are:\n Choose your marking between O and X\n"
    "Players will take turns and place their simbols on the grid\n "
    "In order to win one of the plyers need to place 3 of the symbols in a horizontal, vertical or diogonal row\n "
    "If this is not achieved then it is a tie and the game will restart \n")
    input("Press Enter to continue")

def print_board(board): #done
    """
    Creating and printing out the board
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)



def if_winner(board): #done
    """
    Will check rows , columns and dioganals for the win
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " " :
            return board[i][0] # win row
        if board[0][i] == board[1][i] == board[2][i] != " " :
            return board[0][i] # win column
        if board[0][0] == board[1][1] == board[2][2] != " " :
            return board[0][2] #win dioganal 1
        if board[0][2] == board[1][1] == board[2][0] != " " :
            return board[0][2] # win dioganal 2
        return None


def full_board(board): # done
    """
    Checks id the board is full
    """
    for row in board:
        if " " in row:
            return False
    return True



def player_symbols(): #done
    """
    Player 1 will choose the symbol from X or O.
    Will return error message is other symbol is chosen
    """
    player1 = input("Please Choose X or O: \n").upper()
    while player1 not in ["X", "O"]:
        print("Invalid input, please choose from X , O")
        player1 = input("Please Choose X or O: \n").upper()

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return player1, player2


def out_of_board(row,col):
    return 0<= row <= 2 and 0 <= col <= 2


def player_move(player):
    while True:
        row = int(input(f"Player {player}, please enter row (0, 1, or 2)"))
        col = int(input(f"Player {player}, please enter row (0, 1, or 2)"))

        if out_of_board(row, col):
            return row, col
        else:
            print("Pot of range. Please choose beween 0 and 2")
        
def move(board, player, row, col):
    if board[row][col] == " ":
        board[row][col] = player
    else:
        print("Please try again. This cell is already occupied")

    new_row, new_col = player_move(player)
    move(board, player, row, col)


def player_swap(current_player, player_first, player_second):
    return player_second if current_player == player_first else player_first



def play_game():
    """
    """
    player1, player2 = player_symbols()
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = player1

    while True:
        print_board(board)
        row, col = player_move(current_player)
        move(board, current_player, row, col)
        winner = if_winner(board)


        if winner:
            print_board(board)
            print(f"Player {winner} wins!")

            break

        if full_board(board):
            print_board(board)
            print("Its a tie!")

            break
            
        current_player = player_swap(current_player, player1, player2) #to do 

begining()

if __name__ == "__main__":
    play_game()


def introduction():
    print("Welcome to the game of Tic-TacToe! \n")
    print("Please read the rules of the game: \n")
    print("1. Game is played on a 3x3 board ")
    print("2. Players choose the X or O for their symbole in the game")
    print("3. Players take turns to choose the space on the game board")
    print("4. Player who will place three of their symboles in a row , column or dioganal first wins")
    print("5. If the intire board is filled and there is no winner , the game is a draw.\n")
    print("Good Luck :)\n")

def print_board(board): #done
    """
    Creating and printing out the board
    Limits how many rows are printed out
    """
    for i, row in enumerate(board): 
        print(" | ".join(row))
        if i < 2:  
            print("-" * 10)



def if_winner(board): #done
    """
    Will check rows , columns and dioganals for the winner
    """
     # Will heck rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Will check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Will check both diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

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
        print("Invalid input, please choose from X , O\n")
        player1 = input("Please Choose X or O: \n").upper()

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return player1, player2


def out_of_board(row,col):
    return 0 <= row <= 2 and 0 <= col <= 2


def player_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, please enter row (0, 1, or 2)"))
            col = int(input(f"Player {player}, please enter column (0, 1, or 2)"))

            if out_of_board(row, col):
                return row, col
            else:
                print("Out of range. Please choose beween 0 and 2\n")
        except ValueError:
            print("Invalid input. Please enter a number 0, 1 or 2. Please try again!\n")
        
def move(board, player, row, col):
    if board[row][col] == " ":
        board[row][col] = player
    else:
        print("Please try again. This cell is already occupied \n")
        new_row, new_col = player_move(player)
        move(board, player, row, col)


def player_swap(current_player, player_first, player_second):
    return player_second if current_player == player_first else player_first



def play_game():
    """
    """
    introduction()
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
            
        current_player = player_swap(current_player, player1, player2) 


play_game()
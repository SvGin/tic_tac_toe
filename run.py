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

def print_board(board):
    """
    Creating and printing out the board
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def player_symbols():
    """
    Player 1 will choose the symbol from X or O.
    Will return error message is other symbol is chosen
    """
    payer1 = input("Please Choose X or O: \n").upper()
    while player1 not in ["X", "O"]:
        player1 = input("Invalid. Please Choose X or O: \n").upper()

    player2 = "X" if payer1 == "O" else "O"
    return player1, player2


    





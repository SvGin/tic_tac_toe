board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
winner = None

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


def marking():
    """
    Assignes the symbol to each player: X or O
    If player one will choose X then player 2 will be assigned O or other way round
    """
    print("Please use CAPITAL X or O")
    first = input("Player1, please choose your symbol between X or O \n")
    if first == "X" :
        second = "O"
        print("Player2, your symbol is O")
    elif first == "O":
        second = "X"
        print("Player 2, you are X. ")
    elif first != "X" or first != "O":
        print("Not valid input , please try again") 
    else:
        return first, second  
    

    #print(first, second)
   
    




def main():
    """
    Will store and call all the functions
    """
    introduction = begining()
    choosing_symbol = marking()

main()


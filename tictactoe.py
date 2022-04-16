import random
#Resets board to default state of all null values.
def reset_game():
    global board
    board = [10, 10, 10, 10, 10, 10, 10, 10, 10]


def draw_board():
    #Define board_letters array.
    board_letters = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    #iterate over the 9 spaces in board_letters and convert ' ' to an X or O as needed.
    for number in range(len(board)):
        if board[number] == 1:
            board_letters[number] = "X"
        elif board[number] == 2:
            board_letters[number] = "O"
        else:
            board_letters[number] = " "
    #Draw the board.
    print(" "+board_letters[0]+" | "+board_letters[1]+" | "+board_letters[2]+" ")
    print("___|___|___")
    print(" "+board_letters[3]+" | "+board_letters[4]+" | "+board_letters[5]+" ")
    print("___|___|___")
    print(" "+board_letters[6]+" | "+board_letters[7]+" | "+board_letters[8]+" ")
    print("   |   |   ")

def move_invalid(player_input):
    if board[int(player_input)] == 10:
        return False
    else:
        return True


def do_move(active_player, player_input):
    board[int(player_input)] = active_player


def player_turn(active_player, XorO, turn):
    pinput_invalid = True
    while pinput_invalid:
        player_input = input("Player "+ str(active_player)+": Enter number to place your "+XorO+" or type 'help' for instructions.")
        player_input = player_input.upper()
        if player_input == "HELP":
            help()
            input("Please press the Enter key to proceed")
        elif player_input.isnumeric() == False:
            print("Input invalid: Enter a number between 1 and 9 or type 'help'")
        elif int(player_input) > 0 and int(player_input) <= 9:
            #0 is technically the location of the first square, though this is unitivitive to most people. This will set the player input one lower than what they actually entered.
            player_input = int(player_input) - 1
            #If the user input is between 1 and 9 check if the space is open. If not condition fails. If so make the move.
            if move_invalid(player_input) == False:
                do_move(active_player, player_input)
                pinput_invalid = False
                # The game cannot be won before turn 5. Thus there is no reason to check for a winner before turn 5.
                #if turn >= 5:
                #    check_win()

            else:
                print("Move is invalid: Space already occupied.")
        else:
            print("Input invalid: Enter a number between 1 and 9.")


def ai_turn(difficulty):
    #Difficulty will be implimented later.
    #Easy Difficulty. Simply picks a random location on the grid to play.
    if difficulty == 0:
        retry = True
        while retry:
            AI_input = random.randint(0,8)
            if move_invalid(AI_input) == False:
                retry = False
                do_move(2, AI_input)
                # The game cannot be won before turn 5. Thus there is no reason to check for a winner before turn 5.
                #if turn >= 5:
                #    check_win()
            else:
                retry = True


def check_win(active_player):

    win_number = active_player * 3
    #Horizontal Wins
    if board[0] + board[1] + board[2] == win_number:
        return True
    elif board[3] + board[4] + board[5] == win_number:
        return True
    elif board[6] + board[7] + board[8] == win_number:
        return True
    #Vertical wins
    elif board[0] + board[3] + board[6] == win_number:
        return True
    elif board[1] + board[4] + board[7] == win_number:
        return True
    elif board[2] + board[5] + board[8] == win_number:
        return True
    #Cross wins
    elif board[0] + board[4] + board[8] == win_number:
        return True
    elif board[2] + board[4] + board[6] == win_number:
        return True
    else:
        return False


def again():
    input_invalid = True
    while input_invalid:
        response = input("Do you want to play again? y/n")
        response = response.upper()
        if response =='Y':
            input_invalid = False
            return True
        elif response == "N":
            input_invalid = False
            return False
        else:
            input_invalid = True

def help():
    print(
        "In tic-tac-toe two players take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.")
    print("In this program you will enter a number between 1-9 to place your X or O on the grid.")
    # Draw a sample grid.
    print(" 1 | 2 | 3 ")
    print("___|___|___")
    print(" 4 | 5 | 6 ")
    print("___|___|___")
    print(" 7 | 8 | 9 ")
    print("   |   |   ")
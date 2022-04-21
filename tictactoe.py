import random
first_run = 0


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


#Check if square in board[] is == 10. If so the move is valid.
def move_invalid(player_input):
    if board[int(player_input)] == 10:
        return False
    else:
        return True



def do_move(active_player, player_input):
    board[int(player_input)] = active_player


def player_turn(active_player, XorO, sim, turn):
    pinput_invalid = True
    if sim == True:
        X = board.count(1)
        Y = board.count(2)
        if Y > X or Y >= turn / 2:
            input("HALT. CHEAT!")
        retry = True
        while retry:
            player_input = random.randint(0,8)
            if move_invalid(player_input) == False:
                retry = False
                do_move(1, player_input)
            else:
                retry = True
    else:
        while pinput_invalid:
            player_input = input("Player "+ str(active_player)+": Enter number to place your "+XorO+" or type 'help' for instructions.\n>")
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
                else:
                    print("Move is invalid: Space already occupied.")
            else:
                print("Input invalid: Enter a number between 1 and 9.")




def ai_turn(difficulty, turn):
    #Easy Difficulty. Simply picks a random location on the grid to play.
    if difficulty == 0:
        retry = True
        while retry:
            AI_input = random.randint(0,8)
            if move_invalid(AI_input) == False:
                retry = False
                do_move(2, AI_input)
            else:
                retry = True
    #Medium Difficulty will actually look to counter the player but can be mislead; It does not actively seize upon victories.
    if difficulty >= 1:
        top = [0, 1, 2]
        center =  [3, 4, 5]
        bottom =  [6, 7, 8]
        done_hard_difficulty_pass = False
        retry = True
        count_to_three =  0
        retry_rand = True
        while retry:
            #The game cannot be won before turn 5. If it is turn 5 or greater and the difficulty is at maximum the AI will actively check to see if it can play a winning move and if so take it.
            if retry == True:
                current_check = 1
                if turn == 2 and difficulty == 2:
                    if board[4] == 1 and retry == True:
                        do_move(2, 0)
                        retry = False
                    if board[5] == 1 and retry == True:
                        do_move(2, 2)
                        retry = False
                    if board[3] == 1 and retry == True:
                        do_move(2,0)
                        retry = False
                    if board[7] == 1 and retry == True:
                        do_move(2,1)
                        retry = False
                    if move_invalid(4) == False and retry == True:
                        do_move(2, 4)
                        retry = False
                elif turn == 2 and difficulty == 1 and retry == True:
                        while retry_rand:
                            corners = [0, 2, 6, 8]
                            AI_input = random.randint(0,3)
                            AI_input = corners[AI_input]
                            if move_invalid(AI_input) == False:
                                do_move(2, AI_input)
                                retry=False
                                retry_rand = False
                  
                #If the difficulty is set the hard the AI will run a seperate pass over the board to actively check to see if it can win. If there are no winning moves it will attemt to play a perfect counter move to the players current input.
                #If there is no winning move or counter move the AI will play in a random square.
                if turn > 4 and difficulty == 2 and done_hard_difficulty_pass == False:
                    current_check = 2
                    done_hard_difficulty_pass = True

                for horizon in range(0, 3):
                    if horizon == 0:
                        wincheck = top.copy()
                    elif horizon == 1:
                        wincheck = center.copy()
                    else:
                        wincheck = bottom.copy()
                    if board[wincheck[0]] == current_check and board[wincheck[1]]==current_check and move_invalid(wincheck[2]) == False and retry == True:
                        retry = False
                        do_move(2, wincheck[2])
                    elif board[wincheck[1]] == current_check and board[wincheck[2]]==current_check and move_invalid(wincheck[0]) == False and retry == True:
                        retry = False
                        do_move(2, wincheck[0])         
                    elif board[wincheck[0]] == current_check and board[wincheck[2]]==current_check and move_invalid(wincheck[1]) == False and retry == True:
                        retry = False
                        do_move(2, wincheck[1])
               
                for vert in range(0, 3):
                    if board[top[vert]] == current_check and board[center[vert]] == current_check and move_invalid(bottom[vert]) == False and retry == True:
                        retry = False
                        do_move(2, bottom[vert])
                    elif board[top[vert]] == current_check and board[bottom[vert]] == current_check and move_invalid(center[vert]) == False and retry == True:
                        retry = False
                        do_move(2, center[vert])
                    elif board[center[vert]] == current_check and board[bottom[vert]] == current_check and move_invalid(top[vert]) == False and retry == True:
                        retry = False
                        do_move(2, top[vert])



                if board[0] == current_check and board[8] == current_check and retry == True and difficulty == 2 and move_invalid(4) == False or board[2] == current_check and board[6] == current_check and retry == True and difficulty == 2 and move_invalid(4) == False:
                    do_move(2, 4)
                    retry = False


                if board[4] == current_check and retry == True:
                    if board[0] == current_check and move_invalid(8) == False and retry == True:
                        retry = False
                        do_move(2, 8)
                    elif board[8] == current_check and move_invalid(0) == False and retry == True:
                        retry = False
                        do_move(2, 0)
                    elif board[2] == current_check and move_invalid(6) == False and retry == True:
                        retry = False
                        do_move(2, 6)
                    elif board[6] == current_check and move_invalid(2) == False and retry == True:
                        retry = False
                        do_move(2, 2)


                if turn == 4 and difficulty == 2 and retry == True:
                    if board[7] == 1 and retry == True:
                        if board[3] == 1 or board[5] == 1 and retry == True:
                            if board[0] == 2:
                                do_move(2, 2)
                                retry = False
                            elif board[1] == 2 and retry == True:
                                do_move(2, 6)
                                retry = False
                        elif board[2] == 1 or board[0] == 1 and retry == True:
                             do_move(2, 6)
                             retry = False
                        elif board[4] == 1 and board[1] == 2 and retry == True:
                            do_move(2,0)
                            retry = False
                    if board[4] == 1 and retry == True:
                        if board[6] == 1 or board[8] == 1:
                            do_move(2,2)
                            retry = False
                    if move_invalid(4) == False and retry == True:
                        do_move(2, 4)
                        retry = False
                    if board[4] == 2 and retry == True:
                        if board[8] == 1 and board[0] == 1 or board[6] == 1 and board[2] == 1 and retry == True:
                            do_move(2, 1)
                            retry = False
                    if board[1] == 1 and retry == True:
                        if board[5] == 1 and move_invalid(2) == False and retry == True:
                            do_move(2, 2)
                            retry = False
                        elif board[3] == 1 and move_invalid(0) == False and retry == True:
                            do_move(2, 0)
                            retry = False
                        elif board[8] == 1 and move_invalid(0) == False and retry == True:
                            do_move(2, 0)
                            retry = False
                        elif board[6] == 1 and move_invalid(2) == False and retry == True:
                            do_move(2, 2)
                            retry = False  
                    elif board[7] == 1 and retry == True:
                        if board[5] == 1 and move_invalid(8) == False and retry == True:
                            do_move(2, 8)
                            retry = False
                        elif board[3] == 1 and move_invalid(6) == False and retry == True:
                            do_move(2, 6)
                            retry = False
                        elif board[2] == 1 and move_invalid(8) == False and retry == True:
                            do_move(2, 8)
                            retry = False
                        elif board[0] == 1 and move_invalid(6) == False and retry == True:
                            do_move(2, 6)
                            retry = False 
                    elif board[3] == 1 and retry == True:
                        if board[2] == 1 and move_invalid(0) == False and retry == True:
                            do_move(2, 0)
                            retry = False
                        elif board[8] == 1 and move_invalid(6) == False and retry == True:
                            do_move(2, 6)
                            retry = False 
                    elif board[5] == 1 and retry == True:
                        if board[0] == 1 and move_invalid(2) == False and retry == True:
                            do_move(2, 2)
                            retry = False
                        elif board[6] == 1 and move_invalid(8) == False and retry == True:
                            do_move(2, 8)
                            retry = False

                  
                if turn == 5 and difficulty == 2 and retry == True:
                        if move_invalid(4) == False:
                            do_move(2, 4)
                            retry = False

                 #If no move is valid play a random move.
                if retry == True:
                #If the AI is set to hard this will check to see if the AI has made its 'winning move' pass. If so it will change the current check target to 1 and actively seek to counter player moves.
                    if difficulty == 2 and done_hard_difficulty_pass == True and current_check == 1 or difficulty == 2 and count_to_three < 9 and turn <= 4 or difficulty == 1:
                        if move_invalid(4) == False:
                            do_move(2, 4)
                            retry = False
                        elif retry == True:
                            while retry_rand:
                                AI_input = random.randint(0,8)
                                if move_invalid(AI_input) == False and retry == True:
                                    retry_rand = False
                                    retry = False
                                    do_move(2, AI_input)
                                else:
                                      retry_rand = True
                    if difficulty == 2 and done_hard_difficulty_pass == True:
                        current_check = 1






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


def again(sim, games_played):
    input_invalid = True
    while input_invalid:
        if sim == True:
            response = "Y"
        else:
            response = input("Do you want to play again? y/n\n>")
            response = response.upper()
        if response =='Y':
            if games_played == 255169 * 4:
                halt = input("HALT")
            input_invalid = False
            return True
        elif response == "N":
            input_invalid = False
            return False
        else:
            input_invalid = True

def help():
    print("In tic-tac-toe two players take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.")
    print("In this program you will enter a number between 1-9 to place your X or O on the grid.")
    # Draw a sample grid.
    print(" 1 | 2 | 3 ")
    print("___|___|___")
    print(" 4 | 5 | 6 ")
    print("___|___|___")
    print(" 7 | 8 | 9 ")
    print("   |   |   ")
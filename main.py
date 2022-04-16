import tictactoe

game_active = True
use_AI = False
P1_wins = 0
P2_wins = 0
turn = 0
print("Tic-Tac-Toe!")
input_invalid = True

while input_invalid:
    print("Will you be playing (s)olo or (m)ultiplayer?")
    choice_multiplayer = input()
    choice_multiplayer = choice_multiplayer.capitalize()
    if choice_multiplayer == "S":
        difficulty = 0
        input_invalid = False
        use_AI = True
    elif choice_multiplayer == "M":
        input_invalid = False
        use_AI = False
    else:
        print("Error: Input Invalid")
        input_invalid = True

tictactoe.reset_game()

while game_active:
    turn += 1
    tictactoe.draw_board()
    print("Round: " + str(turn))
    # Divide turn by 2. Player 1(X) always plays on odd turns, Player 2(O) on Even turns
    if turn % 2 != 0:
        active_player = 1
        XorO = "X"
    else:
        active_player = 2
        XorO = "O"

    if use_AI == False:
        print("Player 1 Wins: "+ str(P1_wins)+ " Player 2 Wins: "+ str(P2_wins))
        tictactoe.player_turn(active_player, XorO, turn)
    elif active_player == 1:
        print("Wins: "+ str(P1_wins)+ " Loses: "+ str(P2_wins))
        tictactoe.player_turn(active_player, XorO, turn)
    else:
        print("Wins: "+ str(P1_wins)+ " Loses: "+ str(P2_wins))
        tictactoe.ai_turn(difficulty)

    # The game cannot be won before turn 5. Thus there is no reason to check for a winner before turn 5.
    if turn >= 5:
        if tictactoe.check_win(active_player) == True:
            tictactoe.draw_board()
            print("Player " + str(active_player) + ": wins!!!")
            print(XorO * 20)
            if active_player == 1:
                P1_wins += 1
            else:
                P2_wins += 1
            if tictactoe.again() == True:
                tictactoe.reset_game()
                turn = 0
            else:
                game_active = False
            # If no winner on turn 9 the game is a draw.
        if turn == 9:
            tictactoe.draw_board()
            print("Draw! There are no winners.")
            if tictactoe.again() == True:
                tictactoe.reset_game()
                turn = 0
            else:
                game_active = False


print("Thank you for playing.")
import tictactoe

game_active = True
use_AI = False
P1_wins = 0
P2_wins = 0
draw = 0
turn = 0
games_played = 0
print("Tic-Tac-Toe!")

input_invalid = True

while input_invalid:
    print("Will you be playing (s)olo or (m)ultiplayer?")
    global sim
    sim = False
    difficulty = 0
    choice_multiplayer = input()
    choice_multiplayer = choice_multiplayer.upper()
    if choice_multiplayer == "S" or choice_multiplayer == "SIM":
        if choice_multiplayer == "SIM":
            sim = True
        while input_invalid:
            dif_select = input("Select (e)asy, (m)edium, or (h)ard\n>")
            dif_select = dif_select.upper()
            if dif_select == 'E' or dif_select == "0":
                input_invalid = False
            elif dif_select == 'M'or dif_select == "1":
                input_invalid = False
                difficulty = 1
            elif dif_select == "H"or dif_select == "2":
                difficulty = 2
                input_invalid = False
            else: 
                print("Error: Input Invalid")
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
        print("Player 1 Wins: "+ str(P1_wins)+ " Player 2 Wins: "+ str(P2_wins+ "Draw: " +str(draw) + " Games Played: " + str(games_played)))
        tictactoe.player_turn(active_player, XorO, sim, turn)
    elif active_player == 1:
        print("Wins: "+ str(P1_wins)+ " Loses: "+ str(P2_wins) + " Draw: " + str(draw) + " Games Played: " + str(games_played))
        tictactoe.player_turn(active_player, XorO, sim, turn)
    else:
        print("Wins: "+ str(P1_wins)+ " Loses: "+ str(P2_wins) + " Draw: " + str(draw) + " Games Played: " + str(games_played))
        tictactoe.ai_turn(difficulty, turn)

    # The game cannot be won before turn 5. Thus there is no reason to check for a winner before turn 5.
    if turn >= 5:
        if tictactoe.check_win(active_player) == True:
            tictactoe.draw_board()
            print("Player " + str(active_player) + ": wins!!!")
            print(XorO * 30)
            if active_player == 1:
                P1_wins += 1
                games_played += 1
            else:
                P2_wins += 1
                games_played += 1
            if tictactoe.again(sim, games_played) == True:
                tictactoe.reset_game()
                turn = 0
            else:
                game_active = False
            # If no winner on turn 9 the game is a draw.
        if turn == 9:
            tictactoe.draw_board()
            print("Draw! There are no winners.")
            draw += 1
            games_played +=1
            if tictactoe.again(sim, games_played) == True:
                tictactoe.reset_game()
                turn = 0
            else:
                game_active = False


print("Thank you for playing.")
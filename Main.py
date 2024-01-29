player1S = 0
player2S = 0

while True:
    player1 = input("Player 1 Input? ")
    player2 = input("Player 2 Input? ")
    if player1 == "R" and player2 == "R":
        print("Draw")
    elif player1 == "R" and player2 == "P":
        print("Player 2 Wins")
        player2S += 1
    elif player1 == "R" and player2 == "S":
        print("Player 1 Wins")
        player1S += 1
    elif player1 == "S" and player2 == "S":
        print("Draw")
    elif player1 == "S" and player2 == "R":
        print("Player 2 Wins")
        player2S += 1
    elif player1 == "S" and player2 == "P":
        print("Player 1 Wins")
        player1S += 1
    elif player1 == "P" and player2 == "P":
        print("Draw")
    elif player1 == "P" and player2 == "S":
        print("Player 2 Wins")
        player2S += 1
    elif player1 == "P" and player2 == "R":
        print("Player 1 Wins")
        player1S += 1
    print("Player 1 has", player1S, "wins.")
    print("plater 2 has", player2S, "wins.")

    if player1S == 3:
        print("Player 1 Wins All Game")
    if player2S == 3:
        print("Player 2 Wins All Game")

    if player1S == 3 or player2S == 3:
        print("Game Over")
        exit()
    else:
        continue

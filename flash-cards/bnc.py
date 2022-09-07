import imp
from random import randint, random; import time; import random, sys

#imported random library and time library for countdown during game

# define roles

roles = ["Bear", "Ninja", "Cowboy"]


#generate a random role using an array

computer = roles[randint(1,4)]

player = False

# variables to keep track of score

wins = 0
losses = 0
ties = 0

# game loop

while True:
    while True:
        print("{} wins, {} losses, {} ties" .format(wins,losses, ties))
        print("(B)ear, (N)inja, (C)owboy, or (Q)uit")
        player = input(">").upper()
        if player == "Q":
            print("thanks for playing!")
            sys.exit()

        if player == "B" or player == "N" or player == "C":
            break
        else:
            print("type one of B,N,C,or Q. ")

# show what player chose

    if player == "B":
        print("BEAR versus...")
        player = "BEAR"
    elif player == "N":
        print("NINJA versus...")
        player = "NINJA"
    elif player == "C":
        print("COWBOY versus...")
        player = "COWBOY"

# countdown clock for dramatic effect ;)

    time.sleep(0.5)
    print("1...")
    time.sleep(0.25)
    print("2...")
    time.sleep(0.25)
    print("3...")
    time.sleep(0.25)

# show what the computer chose

    random_number = random.randint(1, 3)
    if random_number == 1:
        computer = "BEAR"
    elif random_number == 2:
        computer = "NINJA"
    elif random_number == 3:
        computer = "COWBOY"
    print(computer)
    time.sleep(0.5)

# show and keep track of game & scores

    if player == computer:
        print("DRAW!")
        ties = ties + 1
    if player == "NINJA" and computer == "COWBOY":
        print("You Win!", player, "defeats", computer)
        wins = wins + 1
    if player == "COWBOY" and computer == "BEAR":
        print("You Win!", player, "shoots", computer)
        wins = wins + 1
    if player == "BEAR" and computer == "NINJA":
        print("You win!", player, "eats", computer)
        wins = wins + 1
    if player == "COWBOY" and computer == "NINJA":
        print("You lose!", computer, "defeats", player)
        losses = losses + 1
    if player == "BEAR" and computer == "COWBOY":
        print("You lose!", computer, "shoots", player)
        losses = losses +1
    if player == "NINJA" and computer == "BEAR":
        print("You lose!", computer, "eats", player)
        losses = losses + 1

# ask if user wants to play again

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == "yes":
        player = False
        computer = True
    else:
      break








    


 
   
 




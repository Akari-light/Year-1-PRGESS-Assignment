from random import randint

#Plays 1 round
def single_round():
    p_option = input("Enter 0(fire), 1(grass) or 2(water): ")
    p_option = p_option.strip() 
    npc_option = randint(0,2)

    #Check if option is valid
    if p_option not in valid_options:
        print("You entered an invalid option, you lost!")
        return -1
    else:
        p_option = int(p_option)
        #Same monster, Draw
        if p_option == npc_option:   
            print("Draw!")
            return 0
        #Player wins
        elif (((p_option + 1) % 3) == (npc_option % 3)): 
            print("You are {} and computer is {}, you won!".format(monsters[p_option], monsters[npc_option]))
            return 1
        #Player loses
        else:
            print("You are {} and computer is {}, you lost!".format(monsters[p_option], monsters[npc_option]))
            return -1


monsters = ["fire","grass","water"]
valid_options = ["0","1","2"]
score = []
availiable_points = 10

while availiable_points > 0:
    print("You have {} points. (-1 to leave)".format(availiable_points))
    wager = int(input("Enter the number of points to be used for next game: "))

    if wager == -1:
        quit("\nThank you for playing!! Hope you had a fun.\n")
    elif wager > availiable_points:
        print("You do not have enough points.\n")
    elif wager == 0:
        print("You have to wage a minimum of 1 point to enter a game!\n")
    else:
        #Plays 3 round
        for i in range(1,4):
            score.append(single_round())

        #Initialize W,L,D
        win, lose, draw = 0, 0, 0

        #Convert array to W,L,D
        for i in score:
            if score[i] == -1:
                lose += 1
            elif score[i] == 0:
                draw += 1
            elif score[i] == 1:
                win += 1
            else:
                pass
        
        print("You have {} win, {} loss and {} draw".format(win,lose,draw))
        if win > lose:
            availiable_points += wager
            print("You won the game with {} points added.\n".format(wager))
        elif win < lose:
            availiable_points -= wager
            print("You lost the game with {} points deducted.\n".format(wager))

            if availiable_points == 0:
                print("You have no more points. End of game!")        
        else:
            print("Tie!\n")
    score.clear()


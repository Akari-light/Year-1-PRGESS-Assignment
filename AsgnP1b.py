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

#Plays 3 round
for i in range(1,4):
    score.append(single_round())

#Initialize W,L,D.
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
    print("You won the game.\n")
elif win < lose:
    print("You lost the game.\n")
else:
    print("Tie!\n")




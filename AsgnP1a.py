from random import randint

monsters = ["fire","grass","water"]
valid_options = ["0","1","2"]

p_option = input("Enter 0(fire), 1(grass) or 2(water): ")
p_option = p_option.strip() 
npc_option = randint(0,2)

#Check if option is valid
if p_option not in valid_options:
    print("You entered an invalid option, you lost!")
else:
    p_option = int(p_option)
    #Same monster, Draw
    if p_option == npc_option:   
        print("Draw!")
    #Player wins
    elif (((p_option + 1) % 3) == (npc_option % 3)): 
        print("You are {} and computer is {}, you won!".format(monsters[p_option], monsters[npc_option]))
    #Player loses
    else:
        print("You are {} and computer is {}, you lost!".format(monsters[p_option], monsters[npc_option]))
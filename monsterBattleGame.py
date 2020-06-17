#!/usr/bin/env python3
from random import randint
from time import sleep 
import sys, os

clean_screen = lambda: os.system("cls")
pause = lambda: os.system("PAUSE")

#Play 1 round and returns either -1 for Lose, 0 for Draw, 1 for Win.
def single_round(monsters, valid_options, void):
    
    p_option = input("Enter 0(fire), 1(grass) or 2(water) or V (Void): " if void > 0 else "Enter 0(fire), 1(grass) or 2(water): ")

    p_option = p_option.strip() 
    npc_option = randint(0,2)

    #Check if option is valid
    if p_option.lower() not in valid_options:
        print("You entered an invalid option, you lost!")
        return -1
    else:
        #Voided the game.
        if p_option.lower() == "v":
            return "v"
        else: 
            p_option = int(p_option)
            #Same monster, Draw.
            if p_option == npc_option:
                print("Draw!")
                return 0
            #Player wins.
            elif (((p_option + 1) % 3) == (npc_option % 3)): 
                print("You are {} and computer is {}, you won!".format(monsters[p_option], monsters[npc_option]))
                return 1
            #Player loses.
            else: 
                print("You are {} and computer is {}, you lost!".format(monsters[p_option], monsters[npc_option]))
                return -1

#MonsterBattler Game
def play_game():
    monsters = ["fire","grass","water"]
    valid_options = ["0","1","2","v"]
    score = []
    games_played = 0
    availiable_points = 10
    void_ability = 1
    win_streak = 0
    highest_streak = 0
    
    user_input = (input("Would you like to clean the screen after every 5 rounds?(y/n) "))
    if user_input.lower() == 'y':
        user_input = True 
    else:
        user_input = False

    while availiable_points > 0:        
        print("You have {} points and {} void chance. (-1 to leave)".format(availiable_points, void_ability))
        if win_streak >= 2:
            print("You are currently on {} winning streak, Keep it up!".format(win_streak))

        #Check if input is a integer
        try:
            wager = int(input("Enter the number of points to be used for next game: "))
        except ValueError:
            print("ERROR: Invalid input. Please enter an integer.\n")
        else: 
            if wager == -1:#Exit game
                quit("\nThank you for playing!! Hope you had a fun.\n")
                update_leaderboard(highest_streak)
            elif wager > availiable_points:
                print("You do not have enough points.\n")
            elif wager <= 0:#Validate the points used for next game.
                print("You have to wage a minimum of 1 point to enter a game!\n")
            else:
                    
                #Plays 3 rounds.
                for i in range(1,4):
                    round_result = single_round(monsters, valid_options, void_ability)
                    #Check if player voided.
                    if round_result == "v":
                        score.append(round_result)
                        break
                    else:
                        score.append(round_result)

                #Initialize W,L,D.
                win, lose, draw = 0, 0, 0                
                voided = False

                #Convert array to W,L,D.
                for i in score:
                    if i == -1:
                        lose += 1
                    elif i == 0:
                        draw += 1
                    elif i == 1:
                        win += 1
                    else:
                        voided = True
                
                #Removes the ability to void and the current game is voided.
                if voided:
                    del valid_options[-1]
                    void_ability -= 1
                    games_played += 1
                    print("Your game is void.\n")
                else:
                    print("You have {} win, {} loss and {} draw".format(win,lose,draw))
                    if win > lose:#Win & compute total points.
                        games_played += 1
                        win_streak += 1                         
                        availiable_points += wager                               
                        print("You won the game with {} points added.\n".format(wager))
                    elif win < lose:#Lose & compute total points.
                        games_played += 1
                        #Check streak
                        if (win_streak > highest_streak) and (win_streak > 1):
                            highest_streak = win_streak
                        win_streak = 0
                        availiable_points -= wager
                        print("You lost the game with {} points deducted.\n".format(wager))                                            
                    else:#Draw
                        games_played += 1
                        #Check streak
                        if (win_streak > highest_streak) and (win_streak > 1):
                            highest_streak = win_streak
                        win_streak = 0
                        print("Tie!\n") 

                score.clear()
                if availiable_points == 0: 
                    print("You have no more points. Better luck next time!\n")
                
                if (games_played == 5) and user_input:
                    print("Clearing screen....")
                    sleep(2)
                    clean_screen()
                    print ("="*10, "Monster Battler", "="*10)

    update_leaderboard(highest_streak)
    sleep(2)
    clean_screen()

def view_instructions():
    instructions = ['Bet your points to start', 'Each game consist of 3 rounds, win 2 rounds to win the game', 'You have 3 types of monsters (Fire, Water and Grass) and a chance to void.', 'Fire beats Grass\n    Grass breats Water\n    Water beats Fire', 'Winstreaks are counted by total consecutive games won.']
    print("")
    for i in instructions:
        print ("[{}] {}".format(instructions.index (i) + 1, i ))
    pause()
    sleep(0.2)
    clean_screen()   

def leaderboard_contents():
    leaderboard_contents = []
    with open("leaderboard.txt","r") as f:
        for line in f:
            line = line.strip('\n').strip().split(',')
            line[1] = int(line[1])           
            leaderboard_contents.append(line)
    #Sort the list from highest to lowest winstreak
    leaderboard_contents = sorted(leaderboard_contents, key=lambda x:x[1], reverse = True)

    return leaderboard_contents

def update_leaderboard(win_streak):
    leaderboard = leaderboard_contents()

    with open("leaderboard.txt","w+") as fw:
        #Check if leaderboard.txt has 10 positions.
        if len(leaderboard) == 10:
            #Check if new winstreak is higher than the last places streak.
            if win_streak > int(leaderboard[-1][1]):
                p_name = input("Congragulations! You have entered the top 10 places in the leaderboard, please register a name to this score: ")
                new_profile = [p_name, win_streak]
                del leaderboard[-1]
                leaderboard.append(new_profile)
                
                for i in range(len(leaderboard)):
                    fw.write("{},{}\n".format(leaderboard[i][0],leaderboard[i][1]))
            else:
                for i in range(len(leaderboard)):
                    fw.write("{},{}\n".format(leaderboard[i][0],leaderboard[i][1]))
        elif win_streak > 1:
            p_name = input("Congragulations! You have entered the top 10 places in the leaderboard, please register a name to this score: ")
            new_profile = [p_name, win_streak]
            leaderboard.append(new_profile)

            for i in range(len(leaderboard)):
                fw.write("{},{}\n".format(leaderboard[i][0],leaderboard[i][1]))
        else:
            pass

def view_leaderboard():
    leaderboard = leaderboard_contents()
    print("")
    for i in range(len(leaderboard)):
        print("[{}] {} with {} winstreak".format(i + 1, leaderboard[i][0].upper(), leaderboard[i][1]))
    pause()
    sleep(0.2)
    clean_screen()


if len( sys.argv ) == 1 :
	pass 
else :
	print ("Correct usage ./[filename].py ")
	quit ()

if __name__ == '__main__':
    is_running = True
    menu_items =['How to play','Play Game','View Leaderboard']

    clean_screen()
    while (is_running):
        #Show Menu
        print(" "*10 + "{}".format("MAIN MENU"))        
        print("=" * 40 )
        print("Monster Battle Game created by Akari.")
        print("=" * 40 )
        for i in menu_items:
            print ("[{}] {}".format(menu_items.index (i) + 1, i ))
        print ("[{}] {}".format(0 ,"Exit Game"))

        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Please enter a number from 0-3.\n")
        else:
            if option == 0:#Exit
                print ("="*10, "Closing Programe", "="*10)
                sleep(0.5)
                clean_screen()
                is_running = False
            elif option == 1:#View Instructions
                sleep(0.5)
                clean_screen()
                print ("="*10, "Instructions", "="*10)
                view_instructions()
            elif option == 2:#Play Game
                sleep(0.5)
                clean_screen()
                print ("="*10, "Monster Battler", "="*10)
                play_game()
            elif option == 3:#View Leaderboard
                sleep(0.5)
                clean_screen()
                print ("="*10, "Leaderboard", "="*10)
                view_leaderboard()
            elif option > 3 and option < 0:
                print("Invalid option. Please enter a valid option")
            else:
                pass
# Samet Altuntaş saltuntas717@gmail.com (Send me feedback & suggestions!)

import random
# R > S, P > R, S > P
# game ends when user or pc has arrived 3 points

def play():
    try:
        pc_score = 0
        user_score = 0
        while (pc_score < 3) and (user_score < 3):
            user_choice = input("(r)ock, (p)aper, (s)cissor... What is your choice? ")
            if (user_choice != 'r') and (user_choice != 'p') and (user_choice != 's'):
                print("Invalid user input. Try again")
                continue
            pc_choice = random.choice(['r', 'p', 's'])
            print(f"pc' choice: {pc_choice}")

            if (user_choice == pc_choice):
                print("tie")
            elif (user_choice == 'p') and (pc_choice == 'r'):
                user_score += 1
                print("user has win this time... ")
            elif (user_choice == 'p') and (pc_choice == 's'):
                pc_score += 1
                print("pc has win this time")
            elif (user_choice == 'r') and (pc_choice == 'p'):
                pc_score += 1
                print("pc has win this time")
            elif (user_choice == 'r') and (pc_choice == 's'):
                user_score += 1
                print("user has win this time")
            elif (user_choice == 's') and (pc_choice == 'p'):
                user_score += 1
                print("user has win this time")
            elif (user_choice == 's') and (pc_choice == 'r'):
                pc_score += 1
                print("pc has win this time")

            print(f"Instant score table: PC: {pc_score} ve USER: {user_score} \n")

        if (user_score > pc_score):
            print("Our winner is user! 🎉")
        else:
            print("Our winner is pc! 🎉")
    except:
        print("Some error occured!")

play()
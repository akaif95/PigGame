'''
Author: <Ali Kaif>
Date: <2/29/18>
Class: ISTA 130
Section Leader: <Sebastian>

Description:
<A list of varying functions that help to create the game 'Pig'>
'''


import random

def print_scores(name1, score1, name2, score2):
    '''This function is 
        designed to print out 
        the scores of the game'''
    print()
    print("--- SCORES\t" + name1 + ": " + str(score1) + "\t" + name2 + ": " + str(score2) +" ---")

    

    

def check_for_winner(name, score):
    '''Function determines which player 
        wins when they reach a score of 50'''
    if score >= 50:
        print("THE WINNER IS: " + name + "!!!!!")
        return True
    else:
        return False

    

    
    
def roll_again(name):
    '''Function determines if player goes 
        again based on input selection'''
    while True:
        again = input("Roll again, " + name + "? (Y/N) ")
        if len(again) == 1 and again in 'YynN':
            if again.lower() == 'y':
                return True
            else:
                return False      
        else:
            print('I don\'t understand: "' + again + '". Please enter either "Y" or "N".')

           

def play_turn(name):
    '''This function tells the users
        what each player rolled and sums 
        up their individual scores'''
    print("---------- " + name + "'s turn ----------")
    score = 0

    while True:
        random_role = random.randint(1, 6)
        print("\t<<< " + name + " rolls a " + str(random_role) + ' >>>')
        if random_role == 1:
            print("\t!!! PIG! No points earned, sorry " + name + " !!!")
            input("(enter to continue)")
            return 0
        else:
            score += random_role
            print("\tPoints: " + str(score))
            if not roll_again(name):
                return score
 





#==========================================================
def main():
    '''All functions are combined here to
        create the game of PIG
    '''

    seed_value = int(input("Enter seed value: "))
    random.seed(seed_value)
    print()
    print()
    print("Pig Dice")
    player1 = input("Enter name for player 1: ")
    player2 = input("Enter name for player 2: ")
    print("\tHello " + player1 + " and " + player2 + ", welcome to Pig Dice!")
    player1_score = 0
    player2_score = 0
    print_scores(player1, player1_score, player2, player2_score)

    while True:
        player1_score += play_turn(player1)
        print_scores(player1, player1_score, player2, player2_score)
        if not check_for_winner(player1, player1_score):
            player2_score += play_turn(player2)
            print_scores(player1, player1_score, player2, player2_score)
            if check_for_winner(player2, player2_score):
                break
        else:
            break


        
        
        

if __name__ == '__main__':
    main()

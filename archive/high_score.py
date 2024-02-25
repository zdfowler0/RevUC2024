import random
import MathGame

def play_high_score(name="Player"):
    print("Mode: High Score")
    print("Play until you lose!\n")

    score = 0

    while(True):
        print(f"Score: {score}")
        
        # generate question level
        level = random.randint(1, 12)

        # chance for a 1.5x bonus
        bonus15 = random.randint(1, 100)

        # chance for a 2x bonus
        bonus2 = random.randint(1, 100)

        # calculate total bonus
        if(bonus15 < 15):
            bonus15 = 1.5
        else:
            bonus15 = 1

        if(bonus2 < 5):
            bonus2 = 2
        else:
            bonus2 = 1
        total_bonus = bonus15 * bonus2

        # show user if they have a bonus
        if(total_bonus > 1):
            print(f"***Bonus this round: {total_bonus}***")

        # get user input and generate question
        user_ans = (input(MathGame.generate_problem(level) + " = "))
        
        # increment the user's score if they get a problem right 
        if(not(user_ans.isnumeric())):
            break # quit sequence
        elif(int(user_ans) == MathGame.ans):
            # increment score
            score += int(level * 100 * total_bonus)
        else:   # wrong answer
            print(f"{user_ans} is incorrect!\n")
            break
        print()

    print(f"{name} got {score} points!")

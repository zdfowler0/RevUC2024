'''
This file contains the back end code for most of
the math game. The levels are are loosely based on
common core standards for math up until about grade 5.
The main function of this code is to provide a versitle
way to generate problems in line with the defined levels
in the README. 
'''

# import libraries
import random
import math
import time

# global variables
ans = 0

# function to generate level 1 problems
def generate_level_1_problem(lower=0, upper=5):
    # create random numbers
    num1 = random.randint(lower, upper)
    num2 = random.randint(lower, upper)

    # update answer
    global ans
    ans = num1 + num2

    # return the problem as a string
    return f"{num1} + {num2}"

# function to generate level 2 problems
def generate_level_2_problem(lower=0, upper=10):
    # generate random numbers
    num1 = random.randint(lower, upper)
    num2 = random.randint(lower, num1)

    # update answer
    global ans
    ans = num1 - num2

    # return the problem as a string
    return f"{num1} - {num2}"

# function to generate level 3 problems
def generate_level_3_problem():
    # determine operation
    operation = random.randint(0, 1)
    
    if(operation == 0): # Addition
        return generate_level_1_problem()
    else: # Subtraction
        return generate_level_2_problem()

# function to generate level 4 problems
def generate_level_4_problem():
    # determine operation
    operation = random.randint(0, 1)
    
    # bounds
    lower = 0
    upper = 20

    if(operation == 0): # Addition
        upper /= 2
        return generate_level_1_problem(lower=lower, upper=upper)
    else: # Subtraction
        return generate_level_2_problem(lower=lower, upper=upper)

# function to generate level 5 problems
def generate_level_5_problem():

    # determine operation
    operation = random.randint(0, 1)
    
    # bounds for operation
    lower = 5
    upper = 100

    if(operation == 0): # Addition
        upper /= 2
        return generate_level_1_problem(lower=lower, upper=upper)
    else: # Subtration
        return generate_level_2_problem(lower=lower, upper=upper)

# function to generate level 6 problems
def generate_level_6_problem():
    # determine operation
    operation = random.randint(0, 1)
    
    # bounds for operation
    lower = 5
    upper = 100
    global ans

    # change upper bound to make calculations valid
    upper //= 2
    # make third number
    num3 = random.randint(lower, upper)

    if(operation == 0): # Add third number
        output = generate_level_5_problem()
        ans += num3
        return output + f" + {num3}"
    else: # Subtract
        output = generate_level_5_problem()
        ans -= num3
        return f"{output} - {num3}"

'''
↑ Addition/Subtraction
↓ Multiplication/Division
'''

# function to generate level 7 problems
def generate_level_7_problem(lower=0, upper=5):
    # create random numbers
    num1 = random.randint(lower, upper)
    num2 = random.randint(lower, upper)

    # update answer
    global ans
    ans = num1 * num2

    # return the problem as a string
    return f"{num1} * {num2}"

# function to generate level 8 problems
def generate_level_8_problem(lower=2, upper=20):
    num2 = 1

    # make sure not to divide by 1
    while(num2 == 1):
        # create random numbers
        num1 = random.randint(lower, upper)
        
        # make sure division result will be an int
        factors = []
        for i in range(1, num1):
            if(num1 % i == 0):
                factors.append(i)

        num2 = factors[random.randint(0, len(factors)-1)]
    
    # update answer
    global ans
    ans = int(num1 / num2)

    # return the problem as a string
    return f"{num1} / {num2}"

# function to generate level 9 problems
def generate_level_9_problem():
    lower = 3
    upper = 10

    return generate_level_7_problem(lower, upper)

# function to generate level 10 problems
def generate_level_10_problem():
    lower = 5
    upper = 100

    return generate_level_8_problem(lower, upper)

# function to generate level 11 problems
def generate_level_11_problem():
    # determine operation
    operation = random.randint(0, 1)

    if(operation == 0): # Multiplication
        # bounds for operation
        lower = 2
        upper = 12
        return generate_level_7_problem(lower=lower, upper=upper)
    else: # Division
        # bounds for operation
        lower = 5
        upper = 100
        return generate_level_10_problem() 

# function to generate level 11 problems
def generate_level_12_problem():
    # determine operation
    operation1 = random.randint(0, 1)

    # bounds for operation
    lower = 5
    upper = 100
    global ans

    # make third number
    num3 = 1

    output = generate_level_11_problem()

    if(operation1 == 0): # Multiply
        num3 = random.randint(lower, upper)
        ans *= num3
        return f"({output}) * {num3}"
    else: # Divide
        
        # make sure not to divide by 1
        while(num3 == 1):
            # create random numbers
            output = generate_level_11_problem()
            
            # make sure division result will be an int
            factors = []
            for i in range(1, ans):
                if(ans % i == 0):
                    factors.append(i)

            num3 = factors[random.randint(0, len(factors)-1)]
            
        ans /= num3
        return f"({output}) / {num3}"

# generate a problem with a specified level
def generate_problem(level):
    print(f"Level {level} problem:")
    
    # determine which level problem to generate
    match level:
        case 1:
            return generate_level_1_problem()
        case 2:
            return generate_level_2_problem()
        case 3:
            return generate_level_3_problem()
        case 4:
            return generate_level_4_problem()
        case 5:
            return generate_level_5_problem()
        case 6:
            return generate_level_6_problem()
        case 7:
            return generate_level_7_problem()
        case 8:
            return generate_level_8_problem()
        case 9:
            return generate_level_9_problem()
        case 10:
            return generate_level_10_problem()
        case 11:
            return generate_level_11_problem()
        case 12:
            return generate_level_12_problem()
        case _:
            print(f"ERROR: NO LEVEL WITH ID {level}")

'''
Contains functions for the three game modes availible
in the main menu but playable through the console.
'''

# play high score mode
def play_high_score(name="Player"):
    # describe game objective
    print("Mode: High Score")
    print("Play until you lose!\n")

    score = 0

    # main game loop
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
        user_ans = (input(generate_problem(level) + " = "))
        
        # increment the user's score if they get a problem right 
        if(not(user_ans.isnumeric())):
            break # quit sequence
        elif(int(user_ans) == ans):
            # increment score
            score += int(level * 100 * total_bonus)
        else:   # wrong answer
            print(f"{user_ans} is incorrect!\n")
            break
        print()

    print(f"{name} got {score} points!")
          
# play time attack mode
def play_time_attack(name="Player", level=1, timer=30):
    # descrie game objective
    print("Mode: Time Attack")
    print(f"Answser as may questions as you can in {timer} seconds!\n")

    # Introduction Sequence
    time.sleep(1)
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("GO!")

    # set the start of the timer
    start = time.time()

    total_correct = 0

    # main game loop
    while(timer > time.time() - start):
        # let the user know how much time is left
        print("Time left: {0}".format(int(abs((time.time() - start) - timer))))

        # get user input and generate question
        user_ans = int(input(generate_problem(level) + " = "))
        
        # increment the user's score if they get a problem right 
        if(user_ans == ans):
            total_correct += 1
        print()
        
    print("End!")
    print(f"{name} got {total_correct} level {level} questions correct in {timer} seconds!")

# play focus mode
def play_focus(name="Player", level=1, questions=5):
    # show game mode and description
    print("Mode: Focus")
    print("Answer as many questions as you want of a certain level!\n")
    
    # keep track of the amount of questions that the user gets correct
    total_correct = 0
    
    # prompt the user for the specified amount of questions
    for i in range(questions):
        # get user input and generate question
        user_ans = int(input(generate_problem(level) + " = "))
        
        # increment the user's score if they get a problem right 
        if(user_ans == ans):
            total_correct += 1
        print()
    
    # tell the user how many problems they got correct
    print(f"{name} got {total_correct}/{questions} level {level} questions correct!")

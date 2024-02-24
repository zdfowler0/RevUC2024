# import libraries
import random
import math

# list of valid operations
operations = [" + ", " - ", " * ", " / ", " ^", " ^-"]

# global variable answer for each problem
ans = 0

# function to generate level 1 problems
def generate_level_1_problem(lower=0, upper=5):
    # create random numbers
    num1 = random.randint(lower, upper)
    num2 = random.randint(lower, upper)

    # update answer
    global ans
    ans = num1 + num2
    print(ans)

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
    print(ans)

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
    lower = 0
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
    lower = 0
    upper = 100
    global ans

    # change upper bound to make calculations valid
    upper //= 2
    # make third number
    num3 = random.randint(lower, upper)

    if(operation == 0): # Add third number
        output = generate_level_5_problem()
        ans += num3
        print(ans)
        return output + f" + {num3}"
    else: # Subtract
        output = generate_level_5_problem()
        ans -= num3
        print(ans)
        return output + f" - {num3}"

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
        case _:
            print("ERROR: NO LEVEL 0 PROBLEMS")
    
# Test print
print("Welcome to the Math Game!")
print("Mode: High Score\n")

# Generate 5 problems levels 1-5
for i in range(1, 7):
    print(generate_problem(i) + "\n")

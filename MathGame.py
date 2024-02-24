# import libraries
import random
import math

# list of valid operations
operations = ["+", "-", "*", "/", "^", "^-"]

# function to generate level 1 problems
def generate_level_1_problem(lower=0, upper=5):
    num1 = random.randint(lower, upper)
    num2 = random.randint(lower, upper)

    print(f"{num1} + {num2}")

    result = num1 + num2
    print(result)

# function to generate level 2 problems
def generate_level_2_problem(lower=0, upper=5):
    num1 = random.randint(lower, upper)
    num2 = random.randint(lower, num1)

    print(f"{num1} - {num2}")

    result = num1 - num2
    print(result)

# function to generate level 3 problems
def generate_level_3_problem():
    # determine operation
    operation = random.randint(0, 1)
    
    if(operation == 0): # Addition
        generate_level_1_problem()
    else: # Subtraction
        generate_level_2_problem()

# function to generate level 4 problems
def generate_level_4_problem():
    # determine operation
    operation = random.randint(0, 1)
    
    lower = 0
    upper = 20

    if(operation == 0): # Addition
        upper /= 2
        generate_level_1_problem(lower=lower, upper=upper)
    else: # Subtraction
        generate_level_2_problem(lower=lower, upper=upper)

# function to generate level 5 problems
def generate_level_5_problem():
    # determine operation
    operation = random.randint(0, 1)
    
    # bounds for operation
    lower = 0
    upper = 100

    if(operation == 0): # Addition
        upper /= 2
        generate_level_1_problem(lower=lower, upper=upper)
    else: # Subtration
        generate_level_2_problem(lower=lower, upper=upper)

# generate a problem with a specified level
def generate_problem(level):
    print(f"Level {level} problem:")
    
    # determine which level problem to generate
    match level:
        case 1:
            generate_level_1_problem()
        case 2:
            generate_level_2_problem()
        case 3:
            generate_level_3_problem()
        case 4:
            generate_level_4_problem()
        case 5:
            generate_level_5_problem()
        case _:
            print("ERROR: NO LEVEL 0 PROBLEMS")

# Test start
print("Welcome to the Math Game!")
print("Mode: High Score\n")

# Generate 5 problems levels 1 - 5
for i in range(1, 6):
    generate_problem(i)
    print("")

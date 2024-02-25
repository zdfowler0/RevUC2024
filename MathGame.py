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
        print(ans)
        return output + f" + {num3}"
    else: # Subtract
        output = generate_level_5_problem()
        ans -= num3
        print(ans)
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
    print(ans)

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
    print(ans)

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
        print(ans)
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
        print(ans)
        return f"({output}) / {num3}"


'''
Run tests
'''

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
    
# Test print
print("Welcome to the Math Game!")
print("Mode: High Score\n")

# Generate 5 problems levels 1-5
for i in range(1, 13):
    print(generate_problem(i) + "\n")

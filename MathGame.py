import random
import math

num1 = random.randint(1, 9)
num2 = random.randint(1, 9)

operation = ["+", "-", "*"]

op = random.randint(0, 2)

if(operation[op] == "+"):
    result = num1 + num2
elif(operation[op] == "-"):
    result = num1 - num2
elif(operation[op] == "*"):
    result = num1 * num2

score = 0

ans = int(input(f"Please enter {num1} {operation[op]} {num2}: "))

while(ans == result):
    print("Correct!")
    score += 1

    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    op = random.randint(0, 2)

    if(operation[op] == "+"):
        result = num1 + num2
    elif(operation[op] == "-"):
        result = num1 - num2
    elif(operation[op] == "*"):
        result = num1 * num2

    ans = int(input(f"Please enter {num1} {operation[op]} {num2}: "))


print("Wrong :/")
print(f"Score: {score}")
'''
This file runs some statistics for Equation Quest.
The program will generate (num_problems) number of questions
for each question type. After that, the average value
and standard deviaion of each question type will be
found and printed to the console.
'''
import math
import Official.EquationQuest as EquationQuest

num_problems = 10000
problems = []

# open files to write to
def open_files_write():
    print("Opening files... \n")
    # open files to write data
    level_one_problems = open("level_one_problems.txt", "w")
    level_two_problems = open("level_two_problems.txt", "w")
    level_three_problems = open("level_three_problems.txt", "w")
    level_four_problems = open("level_four_problems.txt", "w")
    level_five_problems = open("level_five_problems.txt", "w")
    level_six_problems = open("level_six_problems.txt", "w")
    level_seven_problems = open("level_seven_problems.txt", "w")
    level_eight_problems = open("level_eight_problems.txt", "w")
    level_nine_problems = open("level_nine_problems.txt", "w")
    level_ten_problems = open("level_ten_problems.txt", "w")
    level_eleven_problems = open("level_eleven_problems.txt", "w")
    level_twelve_problems = open("level_twelve_problems.txt", "w")

    global problems
    problems = [
    level_one_problems,
    level_two_problems,
    level_three_problems,
    level_four_problems,
    level_five_problems,
    level_six_problems,
    level_seven_problems,
    level_eight_problems,
    level_nine_problems,
    level_ten_problems,
    level_eleven_problems,
    level_twelve_problems
    ]

# open files to read from
def open_files_read():
    print("Opening files... \n")
    # open files to read
    level_one_problems = open("level_one_problems.txt", "r")
    level_two_problems = open("level_two_problems.txt", "r")
    level_three_problems = open("level_three_problems.txt", "r")
    level_four_problems = open("level_four_problems.txt", "r")
    level_five_problems = open("level_five_problems.txt", "r")
    level_six_problems = open("level_six_problems.txt", "r")
    level_seven_problems = open("level_seven_problems.txt", "r")
    level_eight_problems = open("level_eight_problems.txt", "r")
    level_nine_problems = open("level_nine_problems.txt", "r")
    level_ten_problems = open("level_ten_problems.txt", "r")
    level_eleven_problems = open("level_eleven_problems.txt", "r")
    level_twelve_problems = open("level_twelve_problems.txt", "r")

    global problems
    problems = [
    level_one_problems,
    level_two_problems,
    level_three_problems,
    level_four_problems,
    level_five_problems,
    level_six_problems,
    level_seven_problems,
    level_eight_problems,
    level_nine_problems,
    level_ten_problems,
    level_eleven_problems,
    level_twelve_problems
    ]

# close all files
def close_files():
    print("Closing files... ")
    global problems
    for file in problems:
        file.close()

# open files to write
open_files_write()

print("Populating files... ")
# populate files
level = 1
for file in problems:
    
    for i in range(num_problems):
        EquationQuest.generate_problem(level)
        file.write(str(EquationQuest.ans) + "\n")
    
    print(f"Level {level} done")
    level += 1
print()

# close all files
close_files()

# open files for average calculation
open_files_read()

print("Getting averages... ")
averages = []
# calculate average for level
for file in problems:
    total = 0
    elements = 0
    
    # get total of file
    for line in file:
        elements += 1
        total += int(line)
    
    # print the average of the file
    averages.append(total/elements)
    print("Average of " + file.name + ": " + str(total/elements))

# close files
close_files()

# spacing
print()

# open files for std dev calculations
open_files_read()

print("Getting standard deviations... ")
level = 0
# standard deviations
for file in problems:
    total = 0
    elements = 0
    
    # get total of file
    for line in file:
        elements += 1
        total += (int(line) - averages[level])**2
    
    # print standard deviation of file
    print("Standard dev of " + file.name + ": " + str(math.sqrt(total/elements)))
    level += 1

close_files()
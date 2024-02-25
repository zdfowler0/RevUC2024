import time
import MathGame

def play_time_attack(name="Player",level=1,timer=30):
    print("Mode: Time Attack")
    print(f"Answser as may questions as you can in {timer} seconds!")

    # Introduction Sequence
    time.sleep(1)
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("GO!")

    # set the start of the timer
    start = time.time()

    total_correct = 0

    # timer
    while(timer > time.time() - start):
        # let the user know how much time is left
        print("Time left: {0}".format(int(abs((time.time() - start) - timer))))

        # get user input and generate question
        user_ans = int(input(MathGame.generate_problem(level) + " = "))
        
        # increment the user's score if they get a problem right 
        if(user_ans == MathGame.ans):
            total_correct += 1
        print()
        
    print("End!")
    print(f"{name} got {total_correct} level {level} questions correct in {timer} seconds!")
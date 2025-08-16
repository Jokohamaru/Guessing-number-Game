import random_num
import math

def playing(lifepoint, num):
    target_num = random_num.random_number(num)
    print(target_num)
    while lifepoint > 0:
        user_input = int(input("ENTER YOUR NUMBER: "))
        if check(target_num,user_input):
            print("You're right, excellent!!!\n")
            return
        else :
            lifepoint -= 1
    
    print(("Your lifepoints are over").upper())
            
       
def check(target, guess):
    if guess == target:
        print("You're correct!!")
        return 1
    else:
        if abs(target - guess) < 3:
            print("Almost there!!")
            return 0
        elif abs(target - guess) < 5:
            print("So close.")
            return 0
        elif abs(target - guess) < 20:
            print("nearly!!!")
            return 0
        else:
            print("Wrong number")
            return 0
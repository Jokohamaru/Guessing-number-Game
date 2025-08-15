import random_num
import math


def playing(lifepoint, num):
    target_num = random_num.random_number(num)
    while(lifepoint > 0 ):
        user_input = int(input("ENTER YOUR NUMBER: "))
        
"""def check(target, guess):
    if guess == target:
        print("You're correct!!")
        return 1
    else:
        if target"""
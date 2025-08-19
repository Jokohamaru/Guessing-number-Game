import random_num

def playing(lifepoint, num):
    target_num = random_num.random_number(num)
    print(target_num)
    while lifepoint > 0:
        while(True):
            user_input = int(input("ENTER YOUR NUMBER: "))
            if (user_input<=num):
                break
            else:
                print(f"You're out of range, plz enter number below or equal with {num} \n")
        if check(target_num,user_input):
            return
        else :
            lifepoint -= 1
    
    print(("Your lifepoints are over").upper())
             
def check(target, guess):
    if guess == target:
        print("You're right, excellent!!!\n")
        return 1
    else:
        isGreater(guess,target)
        if abs(target - guess) < 3:
            print("Almost there!!\n")
            return 0
        elif abs(target - guess) < 5:
            print("So close.\n")
            return 0
        elif abs(target - guess) < 20:
            print("nearly!!!\n")
            return 0
        else:
            print("Wrong number.\n")
            return 0
        
def isGreater (inp, tar):
    if inp > tar:
        print(f"Is lower than {inp}")
    else:
        print(f"Is higher than {inp}")

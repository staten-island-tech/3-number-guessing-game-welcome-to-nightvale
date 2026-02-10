import random

"""list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = random.choice(list)

user = int(input('guess the number  '))
def check(x):
    x = user
    while x != num:
        print("WRONGe")
    
    print("yayyayayayyyay you got it right !!!!")

check(user) """
#above does not work(properly)

""" list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = random.choice(list)
user = int(input("guess the number  "))
guess_history = []
def guess(x):
    while x != num:
        guess_history.append(x)
        print(guess_history)
        if x < num:
            x = int(input("WRONge!! guess again, the number is greater than your guess  "))
        else:
            x = int(input("WRONge!! guess again, the number is greater than your guess  "))
    guess_history.append(num)
    print("indeed so! you are correct")
    print("Guess history:")
    print(guess_history)

guess(user) """
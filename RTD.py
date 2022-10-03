# code by : dev patel
# www.github.com/dev22419
import random
import time

def exit(y):
    print("the dice number is", y)

def dice(x):
    y = random.randrange(1 , 6)
    if x == 1 and y > 3 :
        print("you won . your guess is correct .")
        exit(y)
    elif x == 2 and y == 3:
        print("you won . your guess is correct .")
        exit(y)
    elif x == 3 and y < 3:
        print("you won . your guess is correct .")
        exit(y)
    else:
        print("you loss the game . your guess is worng .")
        exit(y)

def main():
    r = 100
    print()
    print("choose a number greater than 3 or less then 3 . \nthen press enter to roll the dice .")
    print()
    print("1) greater than 3")
    print("2) 3")
    print("3) lower then three ")
    print()
    x = int(input("choose an option : "))
    print()
    try :
        print("press enter ctrl + c to roll the dice .")
        c = input()
    except(KeyboardInterrupt):
        dice(x)


main()
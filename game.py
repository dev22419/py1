# code by : dev patel
# www.github.com/dev22419
import random

def exit():
    print("bye , have a great time .")

def win(x):
    print()
    o = input("do you want to play one more game ? (y , n) : ")
    if o == "y":
        main()
    else :
        exit()

def lose( i ):
    print()

    print("you lose the correct answer is" , i)
    print()
    o = input("do you want to play one more game ? (y , n) : ")
    if o == "y":
        main()
    else :
        exit()

def main():
    x = random.randrange(1 , 100)
    print("you have 10 chance to guess the the number .")
    print()
    i = 1
    while i <= 10:
        try :
            print("chance :" , i)
            c = int(input("guess a number : "))
            i = i + 1
            if c == x :
                print("hurry , you guessed the correct number .")
                win(x)
            elif c < x :
                print("try guessing a higher value .")
            elif c > x:
                print("try guessing a lower number .")
            else :
                print("somethimg went wrong .")

        except(ValueError):
            print("please , type a number between 1 to 100 .")

    lose(x)

main()
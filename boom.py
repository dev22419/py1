# code by : dev patel
# https://github.com/dev22419/
# let's start

# importing modules
import pyautogui
import time
import os

# booming function
def boom( t , w , n):
    os.system("cls")
    print("waiting for" , w , "seconds ....")
    print("open whatsapps as soon  as possible .....")
    time.sleep(w)
    i = 1
    while i <= n :
        pyautogui.typewrite(t)
        #time.sleep(1)
        pyautogui.press("enter")
        i = i + 1
        

# main fuction
def main():
    os.system("cls")
    print("welcome\n")

    t = input("enter the text : ")
    
    try :
        w = int(input("waiting time : "))
    except (ValueError):
        print("please type a number not string .")
        time.sleep(2)
        main()

    try :
        n = int(input("boom number : "))
    except (ValueError):
        print("please type a number not string .")
        time.sleep(2)
        main()

    boom( t , w , n)


main()
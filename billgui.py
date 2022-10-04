# code by : dev patel
# www.github.con/dev22419/

import os
from tkinter import *

def gui(a , s):
    s = str(s)
    t = "total = "
    s = t + s
    m = Tk()
    T = Text(m)
    T.pack()
    T.insert(END , "\n################################### BILLS #####################################\n")
    T.insert( END , "name\t\t\tquantity\t\t\tprice\n")
    T.insert(END,a)
    T.insert(END , "\n")
    T.insert(END , "\n")
    T.insert(END , "##############################################################################\n")
    T.insert(END , s)
    m.mainloop()

def display(a , s):
    os.system("cls") # use "clear" insted of "cls" if you are on linux/unix
    print("\n################################### BILLS #####################################")
    print()
    print("name\t\t\tquantity\t\tprice")
    print(a)
    print()
    print("##############################################################################")
    print("total = " , s)
    c = input()
    gui(a , s)

def main():
    i = 1
    t = 0
    x = ""
    while i < 100 :
        try:
            os.system("cls") # use "clear" insted of "cls" if you are on linux/unix
            print()
            print("##############################################################################")
            print("item no . : " , i)
            print()
            n = input("name : ")
            q = int(input("quantity : "))
            p = float(input("price : "))
            t = (q*p) + t
            q = str(q)
            p = str(p)
            x = x + "\n" + n[:5] + "\t\t\t" + q + "\t\t\t" + p
            i = i + 1
        except(ValueError):
            q = 1
            p = 0
        except (KeyboardInterrupt):
            i = 101
            gui(x , t)

main()

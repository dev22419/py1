# code by : dev patel
# www.github.con/dev22419/

import os

def display(a , s):
    os.system("cls") # use "clear" insted of "cls" if you are on linux/unix
    print("\n################################### BILLS #####################################")
    print("name\t\t\tquantity\t\tprice")
    print(a)
    print()
    print("##############################################################################")
    print("total = " , s)
    c = input()

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
        except (KeyboardInterrupt):
            i = 101
            display(x , t)

main()

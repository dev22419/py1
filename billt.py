# code by : dev patel
# www.github.con/dev22419/

import os
from tkinter import *

def gui(a , s):
    os.system("cls")
    i = 0
    while i <= 2 :
        try:
            tax = int(input("enter the tax (%) : "))
            i = 4
        except(ValueError):
            print("type persentage .")
            os.system("cls")
    tax = tax/100
    tax = s * tax
    gt = s + tax
    tax = str(tax)
    gt = str(gt)
    tax = "Tax : ₹" + tax
    gt = "grand total = ₹" + gt
    s = str(s)
    t = "Total = ₹ "
    s = t + s
    m = Tk()
    m.title('BILL GUI')
    T = Text(m , font=("Arial" , 12))
    T.pack()
    T.insert(END , "\n################################### BILLS #####################################\n")
    T.insert( END , "name\t\t\tquantity\t\t\tprice\n")
    T.insert(END,a)
    T.insert(END , "\n")
    T.insert(END , "\n")
    T.insert(END , "##############################################################################\n")
    T.insert(END , s)
    T.insert(END , "\n")
    T.insert(END , tax)
    T.insert(END , "\n")
    T.insert(END , "##############################################################################\n")
    T.insert(END , "\n")
    T.insert(END , gt)
    b = Button(m , text='close' ,fg='red', width=10 , command=m.destroy)
    b.pack(side='right')
    m.mainloop()


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
            r = "₹ "
            p = r + p
            x = x + "\n" + n[:5] + "\t\t\t" + q + "\t\t\t" + p
            i = i + 1
        except(ValueError):
            q = 1
            p = 0
        except (KeyboardInterrupt):
            i = 101
            gui(x , t)

main()

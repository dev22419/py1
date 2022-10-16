# code by : dev patel
# https://www.github.com/dev22419
def main():

    print("type your full address below (with comma ) : ")
    print()
    x = input("> ")
    print()

    for n in x:
        if n == ",":
            print(n)
        else:
            print(n , end='')
    print()

main()
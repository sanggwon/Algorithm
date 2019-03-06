for tc in range(1,int(input())+1):
    string = input()

    print(".", end="")
    for i in range(len(string)):
        print(".#..", end="")

    print()
    print(".", end="")
    for i in range(len(string)):
        print("#.#.", end="")

    print()
    print("#",end="")
    for i in range(len(string)):
        print(".{}.#".format(string[i]), end="")

    print()
    print(".", end="")
    for i in range(len(string)):
        print("#.#.", end="")

    print ()
    print(".", end="")
    for i in range(len(string)):
        print(".#..", end="")
    print()


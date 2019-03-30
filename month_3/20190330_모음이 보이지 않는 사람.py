a = ['a', 'e', 'i', 'o', 'u']
for tc in range(1,int(input())+1):
    print("#{}".format(tc), end=" ")
    for i in input() :
        if not i in a :
            print(i, end="")
    print()

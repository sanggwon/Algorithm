space = int(input("거리:"))
for i in range(1,4) :
    print("*", end="")
    print(" "*space,end="") 
print()      
for i in range(1,3) :
    if space%2 == 0 :
        if i == 1 :
            print(" "*(space//2+1),end="")
            print("*",end="")
        else :
            print(" "*(space-1),end="")
            print("*",end="")
    else :
        if i == 1 :
            print(" "*((space+1)//2),end="")
            print("*",end="")
        else :
            print(" "*space,end="")
            print("*",end="")

 

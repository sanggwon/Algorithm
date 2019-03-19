def frog(croak,check) :
    for i in range(len(croak)):
        if croak[i] == "c" :
            check[0] += 1
            if check[-1] > 0 :
                for k in range(5):
                    check[k] -= 1
        elif croak[i] == "r" :
            check[1] += 1
        elif croak[i] == "o" :
            check[2] += 1
        elif croak[i] == "a" :
            check[3] += 1
        elif croak[i] == "k" :
            check[4] += 1
        else :
            return -1
        for j in range(4) :
            if check[j] < check[j+1] :
                return -1
    for m in range(1,5):
        if check[0] != check[m] :
            return -1
    return check[-1]

for tc in range(1,int(input())+1):
    croak = input()
    check = [0]*5

    print("#{} {}".format(tc,frog(croak,check)))
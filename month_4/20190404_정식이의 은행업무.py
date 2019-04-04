Trine = [0,1,2]

T = int(input().strip())+1
for tc in range(1,T):
    b = list(map(int,input().strip()))
    b_copy = b[:]
    t = list(map(int,input().strip()))
    t_copy = t[:]
    check = 0

    for i in range(len(b)) :
        if check == 0 :
            for j in range(len(t)) :
                if check == 0 :
                    if b[i] == 0 :
                        b[i] = 1
                    else:
                        b[i] = 0
                    for m in Trine :
                        if t[j] != m :
                            t[j] = m

                            if int("".join(map(str,b)),2) == int("".join(map(str,t)),3) :
                                check = 1
                                break
                            else :
                                t = t_copy[:]
                    b = b_copy[:]
    print("#{} {}".format(tc,int("".join(map(str,t)),3)))

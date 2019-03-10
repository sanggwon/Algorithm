for tc in range(1,int(input())+1):
    N = input()
    cnt = 0
    q = []
    for i in N :
        if not q :
            laser = 0 
            change = 0
        if i == "(" :
            q.append(i)
            change = 0
        elif i == ")" and change == 0 :
            q.pop()
            laser +=1
            change = 1
            cnt += len(q)
        elif q and i == ")" :
            cnt += 1
            q.pop()

    print(f"#{tc} {cnt}")

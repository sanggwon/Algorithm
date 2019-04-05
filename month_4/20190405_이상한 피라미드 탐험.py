T = int(input().strip())+1
for tc in range(1,T):
    a, b = map(int,input().strip().split())
    s = 1
    e = 3
    m = []
    t = []
    cnt = 0

    if a == 1 :
        m = [0,0]
    if b == 1 :
        t = [0,0]

    for i in range(1000) :
        if len(m) and len(t):
            break
        s = s+i
        if i != 0 :
            e = s+i
            if not len(m) :
                if s<=a<=e :
                    m = [i,a-s]
            if not len(t) :
                if s<=b<=e :
                    t = [i,b-s]


    while m[0] != t[0]:
        if m[0] < t[0] :
            if m[1] < t[1] :
                cnt += 1
                t[0] -= 1
                if t[1] != 0 :
                    t[1] -= 1
            else :
                cnt += 1
                t[0] -= 1
        elif m[0] > t[0]:
            if m[1] > t[1] :
                cnt += 1
                m[0] -= 1
                if m[1] != 0 :
                    m[1] -= 1
            else :
                cnt += 1
                m[0] -= 1


    print("#{} {}".format(tc,(cnt + abs(m[1]-t[1]))))

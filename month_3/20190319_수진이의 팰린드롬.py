
for tc in range(1,int(input())+1):
    A = sorted(list(input()))
    next = len(A)
    num = len(A)
    cnt = 0
    while num != 0 :
        for i in range(num):
            B = A[i:i+1+next-num]
            cnt += 1
            if len(B) != 1 :
                for j in range(len(B)//2) :
                    if B[j] != B[len(B)-1-j] :
                        cnt -= 1
                        break
        num -= 1

    print("#{} {}".format(tc,cnt))

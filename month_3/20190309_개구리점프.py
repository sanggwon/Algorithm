def frog(n,k):
    jump = 0
    cnt = 1
    for i in range(1,n+1) :
        if stones[i] - stones[i-1] > k :
            return -1
        else :
            if stones[i] - stones[jump] > k :
                jump = i-1
                cnt +=1
            elif stones[i] - stones[jump] == 0 :
                jump = i
                cnt +=1
    return cnt

T = int(input())
for tc in range(1,T+1):
    res = []
    N = int(input())
    stones = [0]+list(map(int,input().split()))
    K = int(input())
    print(f"Case #{tc}") 
    res.append(frog(N,K))
    for i in res :
        print(i)

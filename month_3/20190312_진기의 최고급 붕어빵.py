import sys
sys.stdin = open("text2.txt","r")
def check(N,M,K):
    global sec,cnt,next
    if customer[next] == 0:
        return "Impossible"
    for i in range(customer[-1]):
        sec += 1
        if sec % M == 0:
            cnt += K
        if customer[next] == sec :
            cnt -=1
            next +=1
        if cnt < 0 :
            return "Impossible"
    return "Possible"


for tc in range(1,int(input())+1):
    N,M,K = map(int,input().split())
    customer = sorted(list(map(int,input().split())))
    sec = 0
    cnt = 0
    next = 0
    print("#{} {}".format(tc,check(N, M, K)))


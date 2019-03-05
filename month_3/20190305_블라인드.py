import sys
sys.stdin = open("input6.txt","r")

M,N = map(int,input().split())

W = [list(input().split()) for _ in range(5*M+1)]
blind = [4,3,2,1,0]
res = [0,0,0,0,0]
check = []
for _ in range(N):
    check.append([])

for i in range(1,5*M+1):
    for j in range(N):
        check[j].append(W[i][0][(j*5)+1:(j*5)+5])
check_str = "...."
check_next = "####"
check_cnt = 0
for n in check:
    for m in n :
        if m == check_str :
            check_cnt +=1
        if m == check_next :
            res[blind.index(check_cnt)] +=1
            check_cnt = 0
print(" ".join(map(str,res)))

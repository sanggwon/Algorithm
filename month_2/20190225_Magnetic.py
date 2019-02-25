import sys
sys.stdin = open("sample_input_27.txt","r")

## 인덱스를 뽑아서 비교하는 코드.. 효율 x
for tc in range(1,11):
    T = int(input())
    M = [input().split() for _ in range(T)]
    count = 0
    for i in range(100):
        N = []
        S = []
        for j in range(T):
            if M[j][i] == "1":
                N.append(j)
            if M[j][i] == "2":
                S.append(j)
        for n in range(len(N)) :
            if S[-1] < N[n]:
                del N[n:]
                break
        for s in range(len(S)) :
            if S[s] < N[0] :
                del S[:s+1]
                break
        num = 0
        for x in S :
            num_cnt = 0
            for y in N[num+num_cnt:]:
                if x > y :
                    num_cnt +=1
                else :
                    break
                num+=1
            if num_cnt >= 1:
                count +=1
                

    print(f"#{tc} {count}")



## 세로로 for문을 돌리면서 if문을 사용
T = 10
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for x in range(100)]
    cnt = 0
    for i in range(N):
        point = 0
        for j in range(N):
            if arr[j][i] == 1:
                point = 1
            elif arr[j][i] == 2 and point == 1:
                    cnt += 1
                    point = 0
            elif arr[j][i] ==2 and point != 1:
                continue
 
 
    print(f"#{tc} {cnt}")

                
                

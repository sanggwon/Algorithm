import sys
sys.stdin = open("sample_input_10.txt","r",)


## 제가 푼 코드입니다.
T = int(input())
for tc in range(T):
    N = int(input())
    R = [list(map(int,input().split())) for _ in range(N)]

    M = [[0]*10 for _ in range(10)]
    
    for i in range(N):
        for j in range(R[i][2]-R[i][0]+1):
            for z in range(R[i][1],R[i][3]+1):
                M[R[i][0]+j][z] +=1
    count = 0
    for y in range(10):
        count+=M[y].count(2)

    print(f"#{tc+1} {count}")



## 다른 사람 코드입니다.
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    red = []
    blue = []
    for area in range(N):
        paint = list(map(int, input().split()))
        for i in range(paint[0], paint[2]+1):
            for j in range(paint[1], paint[3]+1):
                if paint[4] == 1:
                    red.append((i,j))
                else:
                    blue.append((i,j))

    result = len(set(red) & set(blue))
    print(f"#{test_case} {result}")
    

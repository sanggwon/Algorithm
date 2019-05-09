import sys
sys.stdin = open('input.txt','r')

T = int(input())+1

for tc in range(1,T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    for start_i in range(N-2):
        # 맨 아래면 제외
        for start_j in range(1,N-1):
            # 왼쪽 면, 오른쪽 면 제외
            next_i = start_i
            for next_j in range(start_j+1,N):
                next_i += 1
                if next_i == N-1:
                    break
                next_next_j = next_j
                for next_next_i in range(next_i+1,next_i+1+start_j):
                    next_next_j -= 1
                    print((start_i,start_j),(next_i,next_j),(next_next_i,next_next_j))

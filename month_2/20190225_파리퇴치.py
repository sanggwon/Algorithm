import sys
sys.stdin = open("sample_input_28.txt","r")


for tc in range(int(input())):
    T,N = map(int,input().split())
    numbers = [list(map(int,input().split())) for _ in range(T)]
    max_count = 0
    for i in range(T-N+1):
        for j in range(T-N+1):
            count = 0
            for x in range(N):
                count += sum(numbers[i+x][j:j+N])
            if max_count < count :
                max_count = count
            
    print(f"#{tc+1} {max_count}")


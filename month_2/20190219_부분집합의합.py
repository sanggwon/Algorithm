import sys
sys.stdin = open("sample_input_11.txt","r")

T = int(input())
card = list(range(1,13))


for tc in range(T):
    A = list(map(int,input().split()))
    n = len(card)
    result = []
    count = 0
    for i in range(1<<n):
        for j in range(n):
            if i & (1<<j):
                result += [card[j]]
        if len(result) == A[0] and sum(result) == A[1]:
            count += 1
        result = []
        
    print(f"#{tc+1} {count}")
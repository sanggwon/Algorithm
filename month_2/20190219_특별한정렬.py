import sys
sys.stdin = open("sample_input_13.txt","r")

T = int(input())

for tc in range(T):
    N = int(input())
    numbers = list(map(int,input().split()))
    lists = []
    for _ in range(5):
        min = 100
        max = 1
        for i in numbers :
            if i >= max :
                max = i
            if i <= min :
                min = i
        numbers.pop(numbers.index(max))
        numbers.pop(numbers.index(min))
        lists.extend([max,min])
    print(f"#{tc+1} {' '.join(map(str,lists))}")

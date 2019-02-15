import sys
sys.stdin = open("sample_input.txt","r")
for i in range(int(input())):
    T = input()
    lists = list(map(int,input().split()))

    value_max = 0

    for z in lists:
        if z > value_max:
            value_max = z
    value_min = value_max
    
    for y in lists :
        if y < value_min :
            value_min = y
    print(f"#{i+1} {value_max-value_min}")

    
        
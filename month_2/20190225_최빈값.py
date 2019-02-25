import sys
sys.stdin = open("sample_input_26.txt","r")

for _ in range(int(input())):
    tc = input()
    numbers = list(map(int,input().split()))
    result = {}
    for i in list(set(numbers)):
        result.update({i:numbers.count(i)})

    max_count = max(result.values())
    result_key = 0
    for key,value in result.items():
        if max_count == value :
            if result_key < key:
                result_key = key
    print(f"#{tc} {result_key}")
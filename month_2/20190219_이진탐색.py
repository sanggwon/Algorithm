import sys
sys.stdin = open("sample_input_12.txt","r")

T = int(input())
for tc in range(T):
    P,A,B = map(int,input().split())
    count_list = []
    for i in [A,B]:
        start = 1
        count = 0
        end = P  
        while start <= end :
            middle = (start + end)//2
            count += 1
            if middle == i :
                break
            elif middle > i :
                end = middle
            else :
                start = middle

        count_list.append(count)
        count = 0
    if count_list[0] < count_list[1]:
        result = "A"
    elif count_list[0] > count_list[1]:
        result = "B"
    else :
        result = 0
    print(f"#{tc+1} {result}")

        

import sys
sys.stdin = open("sample_input_23.txt","r")

for tc in range(int(input())):
    S1 = input()
    S2 = input()
    max_count = 0
    for i in S1 :
        count = 0
        for j in S2:
            if i == j :
                count +=1
        if max_count < count :
            max_count = count
        

    print(f"#{tc+1} {max_count}")
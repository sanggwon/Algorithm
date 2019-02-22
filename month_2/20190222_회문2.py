import sys
sys.stdin = open("sample_input_24.txt","r")


for tc in range(1,11):
    N = int(input())
    I = [input() for _ in range(100)]
    start = 3
    max_count = 0
    for i in range(98):
        for j in range(98):
            length = 3
            for x in range(start,101):
                r_count = 0
                c_count = 0
                for y in range(length//2):
                    if I[i][j+y] == I[i][j+length-y-1]:
                        r_count +=1
                    if I[j+y][i] == I[j+length-y-1][i] :
                        c_count += 1
                if max_count < r_count :
                    max_count = r_count
                if max_count < c_count :
                    max_count = c_count
                length += 1           
            start +=1
    print(max_count)
        
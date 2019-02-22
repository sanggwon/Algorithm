import sys
sys.stdin = open("sample_input_20.txt","r")

for tc in range(1,11):
    N = int(input())
    count = 0
    I = [input() for i in range(8)]
    for i in range(8):
        for j in range(9-N):
            r_count = 0
            c_count = 0
            for x in range(N//2):
                if I[i][j+x] == I[i][j+N-x-1] :
                    r_count += 1
                if I[j+x][i] == I[j+N-x-1][i] :
                    c_count += 1
            if r_count == N//2 :
                count +=1
            if c_count == N//2 :
                count +=1

    print(f"#{tc} {count}")
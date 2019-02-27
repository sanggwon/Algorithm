import sys
sys.stdin = open("sample_input_36.txt","r")

def find(sutoku,check):
    for i in range(9):
        c = []
        num_c = 0
        if check != sorted(sutoku[i]):
            return 0
        for j in range(9):
            c.append(sutoku[j][i])
        for x in check :
            if check != sorted(c):
                return 0
    for y in range(3):
        s = 3*y
        for n in range(3):
            d = []
            for m in range(s,s+3):
                d.extend(sutoku[m][3*n:3*(n+1)])
            if check != sorted(d):
                return 0
    return 1

for tc in range(1,int(input())+1):
    sutoku = [list(map(int,input().split())) for _ in range(9)]
    check = list(range(1,10))
    print(f"#{tc} {find(sutoku,check)}")

import sys
sys.stdin = open("sample_input_35.txt","r")

from itertools import permutations
T=int(input())
for _ in range(T):
    num=int(input())
    card=[list(map(int,input().split())) for i in range(num)]
    d=100
    for j in permutations(range(num)):
        c=0
        for k in range(num):
            c+=card[k][j[k]]
            if d < c :
                break
        if d>c:
            d=c
    print(f"#{_+1} {d}")
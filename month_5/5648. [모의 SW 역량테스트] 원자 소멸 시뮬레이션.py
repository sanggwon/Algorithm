import sys
sys.stdin = open('input.txt','r')

T = int(input())+1
for tc in range(1,T):
    N = int(input())
    atoms = [list(map(int,input().split())) for _ in range(N)]

    area = [[0]*2000 for _ in range(2000)]

    for atom in atoms :
        atom[0] += 1000
        atom[1] = -atom[1]
        atom[1] += 1000

    for atom in atoms :
        area[atom[1]][atom[0]] = [atom[2],atom[3]]

    sum_atom = 0
    while N :
        for i in range(2000) :
            for j in range(2000) :
                if area[i][j] :
                    if area[i][j][0] == 1 :
                        if area[i]
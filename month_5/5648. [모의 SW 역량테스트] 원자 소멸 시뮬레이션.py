import sys
sys.stdin = open('input.txt','r')

T = int(input())+1
for tc in range(1,T):
    N = int(input())
    atoms = [list(map(int,input().split())) for _ in range(N)]

    for atom in atoms :
        atom[0] *= 2
        atom[1] *= 2
    print(atoms)

    atom_sum = 0
    while N :
        atom_list = []
        for i in range(len(atoms)) :
            if atoms[i] :
                if atoms[i][2] == 0 :
                    atoms[i][1] += 1
                    if atoms[i][1] > 2000 :
                        N -= 1
                        atoms[i] = 0
                elif atoms[i][2] == 1 :
                    atoms[i][1] -= 1
                    if atoms[i][1] < -2000 :
                        N -= 1
                        atoms[i] = 0
                elif atoms[i][2] == 2 :
                    atoms[i][0] -= 1
                    if atoms[i][0] < -2000:
                        N -= 1
                        atoms[i] = 0
                else :
                    atoms[i][0] += 1
                    if atoms[i][0] > 2000 :
                        N -= 1
                        atoms[i] = 0
        print(atoms)

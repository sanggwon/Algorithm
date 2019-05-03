import sys
sys.stdin = open('input.txt','r')

T = int(input())+1
for tc in range(1,T):
    N = int(input())
    atoms = [list(map(int,input().split())) for _ in range(N)]

    for atom in atoms :
        atom[0] *= 2
        atom[1] *= 2

    atom_sum = 0
    atom_list = [i for i in range(len(atoms))]
    while atom_list :
        atom_remove = set()
        for i in atom_list :
            if atoms[i][2] == 0 :
                atoms[i][1] += 1
                if atoms[i][1] > 2000 :
                    atom_remove.add(i)
            elif atoms[i][2] == 1 :
                atoms[i][1] -= 1
                if atoms[i][1] < -2000 :
                    atom_remove.add(i)
            elif atoms[i][2] == 2 :
                atoms[i][0] -= 1
                if atoms[i][0] < -2000:
                    atom_remove.add(i)
            else :
                atoms[i][0] += 1
                if atoms[i][0] > 2000 :
                    atom_remove.add(i)

        if atom_remove :
            atom_list = set(atom_list)
            atom_list = atom_list-atom_remove
            atom_list = list(atom_list)

        atom_remove = set()

        for i in range(len(atom_list)):
            if not i in atom_remove :
                check = 0
                check_x, check_y = atoms[atom_list[i]][0], atoms[atom_list[i]][1]
                for j in range(i+1,len(atom_list)):
                    if not atom_list[j] in atom_remove:
                        if check_x == atoms[atom_list[j]][0] and check_y == atoms[atom_list[j]][1]:
                            atom_sum += atoms[atom_list[j]][3]
                            atom_remove.add(atom_list[j])
                            check += 1
                if check :
                    atom_sum += atoms[atom_list[i]][3]
                    atom_remove.add(atom_list[i])

        if atom_remove:
            atom_list = set(atom_list)
            atom_list = atom_list - atom_remove
            atom_list = list(atom_list)


    print("#{} {}".format(tc,atom_sum))

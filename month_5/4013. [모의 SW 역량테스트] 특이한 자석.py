import sys
sys.stdin = open('input.txt','r')

T = int(input())+1
for tc in range(1,T):
    K = int(input())
    gears = [list(map(int,input().split())) for _ in range(4)]
    rotation = [list(map(int,input().split())) for _ in range(K)]


    for index, direction in rotation :

        if direction == 1 :
            # 오른쪽
            right = gears[index-1][2]
            left = gears[index-1][6]
            a = gears[index-1].pop(-1)
            gears[index-1] = [a] + gears[index-1]
            # 회전

            check = 0
            for i in range(index-2,-1,-1) :
                if left != gears[i][2] :
                    left = gears[i][6]
                    if check == 0 :
                        # 왼쪽 회전
                        a = gears[i].pop(0)
                        gears[i] = gears[i] + [a]
                        check = 1
                    else :
                        # 오른쪽 회전
                        a = gears[i].pop(-1)
                        gears[i] = [a] + gears[i]
                        check = 0
                else :
                    break

            check = 0
            for i in range(index,4) :
                if right != gears[i][6] :
                    right = gears[i][2]
                    if check == 0 :
                        # 왼쪽 회전
                        a = gears[i].pop(0)
                        gears[i] = gears[i] + [a]
                        check = 1
                    else :
                        # 오른쪽 회전
                        a = gears[i].pop(-1)
                        gears[i] = [a] + gears[i]
                        check = 0
                else :
                    break

        else :
            # 왼쪽
            right = gears[index-1][2]
            left = gears[index-1][6]
            a = gears[index-1].pop(0)
            gears[index-1] = gears[index-1]+[a]
            # 회전

            check = 0
            for i in range(index-2,-1,-1) :
                if left != gears[i][2] :
                    left = gears[i][6]
                    if check == 0 :
                        # 오른쪽 회전
                        a = gears[i].pop(-1)
                        gears[i] = [a] + gears[i]
                        check = 1
                    else :
                        # 왼쪽 회전
                        a = gears[i].pop(0)
                        gears[i] = gears[i] + [a]
                        check = 0
                else :
                    break

            check = 0
            for i in range(index,4) :
                if right != gears[i][6] :
                    right = gears[i][2]
                    if check == 0 :
                        # 오른쪽 회전
                        a = gears[i].pop(-1)
                        gears[i] = [a] + gears[i]
                        check = 1
                    else :
                        # 왼쪽 회전
                        a = gears[i].pop(0)
                        gears[i] = gears[i] + [a]
                        check = 0
                else :
                    break

    print("#{} {}".format(tc, gears[0][0]*1 + gears[1][0]*2 + gears[2][0]*4 + gears[3][0]*8))

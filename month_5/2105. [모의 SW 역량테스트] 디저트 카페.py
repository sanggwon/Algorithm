import sys
sys.stdin = open('input.txt','r')

T = int(input())+1

for tc in range(1,T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_num = 0
    for start_i in range(N-2):
        # 맨 아래면 제외
        for start_j in range(1,N-1):
            # 왼쪽 면, 오른쪽 면 제외
            next_i = start_i
            for next_j in range(start_j+1,N):
                next_i += 1
                next_next_j = next_j
                for next_next_i in range(next_i+1,N):
                    next_next_j -= 1

                    if next_j-next_next_j == start_j +1:
                        break

                    last_i = start_i+(next_next_i-next_i)
                    last_j = start_j+(next_next_j-next_j)


                    list_num = []
                    check = 0


                    j = start_j
                    for start in range(start_i,next_i) :
                        if not arr[start][j] in list_num :
                            list_num.append(arr[start][j])
                            j += 1
                        else :
                            check = 1
                            break

                    if check :
                        break


                    j = next_j
                    for next in range(next_i,next_next_i):
                        if not arr[next][j] in list_num :
                            list_num.append(arr[next][j])
                            j -= 1
                        else :
                            check = 1
                            break
                    if check :
                        break


                    j = next_next_j
                    for next_next in range(next_next_i,last_i,-1):
                        if not arr[next_next][j] in list_num :
                            list_num.append(arr[next_next][j])
                            j -= 1
                        else :
                            check = 1
                            break

                    if check == 0:
                        j = last_j
                        for last in range(last_i, start_i,-1):
                            if not arr[last][j] in list_num :
                                list_num.append(arr[last][j])
                                j += 1
                            else :
                                check = 1
                                break

                    if check == 0 :
                        if max_num < len(list_num):
                            max_num = len(list_num)

    if max_num :
        print("#{} {}".format(tc,max_num))
    else :
        print("#{} {}".format(tc, -1))



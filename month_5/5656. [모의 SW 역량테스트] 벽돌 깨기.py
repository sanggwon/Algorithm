import sys
from itertools import product
import copy
sys.stdin = open('input.txt','r')

def bfs(i,j):
    global W,H,copy_arr,count
    ind_i = [0,1,0,-1]
    ind_j = [1,0,-1,0]

    q = []
    c = []
    q.append((i,j))
    c.append(copy_arr[i][j])
    count += 1
    copy_arr[i][j] = 0
    while q :
        i,j = q.pop()
        num = c.pop()
        for k in range(4):
            ni = i
            nj = j
            for _ in range(num-1) :
                ni += ind_i[k]
                nj += ind_j[k]
                if 0<=ni<W and 0<=nj<H :
                    if copy_arr[ni][nj] != 0 :
                        q.append((ni,nj))
                        c.append(copy_arr[ni][nj])
                        copy_arr[ni][nj] = 0
                        count += 1

def after(arr):
    global H,W

    for i in range(W):
        add = []
        for j in range(H):
            if copy_arr[i][j] != 0 :
                add.append(copy_arr[i][j])

        copy_arr[i] = [0]*(H-len(add))+add


T = int(input())+1
for tc in range(1,T):
    N, W, H = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]
    # input_arr
    products = list(product(list(range(W)),repeat=N))
    # product
    s_arr = [[0] * H for _ in range(W)]
    # 회전을 위한 arr

    total = 0
    for i in range(H):
        for j in range(W):
            s_arr[j][i] = arr[i][j]
            if arr[i][j] > 0 :
                total += 1
    # 회전
    max_count = 0
    for prod in products:
        copy_arr = copy.deepcopy(s_arr)
        count = 0
        # 돌릴때마다 원상복구
        check = 0
        for i in prod :
            if copy_arr[i][-1] != 0:
                for j in range(H) :
                    if copy_arr[i][j] != 0 :
                        bfs(i,j)
                        break
            after(copy_arr)
            if count == total :
                check = 1
                break
        if check :
            break
        if max_count < count :
            max_count = count
    if check :
        print("#{} {}".format(tc,0))
    else :
        print("#{} {}".format(tc,total-max_count))

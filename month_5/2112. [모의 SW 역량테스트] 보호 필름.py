import sys
import copy
sys.stdin = open('input.txt','r')


def check(box):
    for i in range(W):
        num = box[0][i]
        count = 0
        for j in range(D):
            if num == box[j][i] :
                count += 1
            else :
                num = box[j][i]
                count = 1
            if count == K :
                break
        if count != K :
            return False
    if count != K :
        return False
    else :
        return True

def f(box,k):
    global resulte
    a = copy.deepcopy(box)
    def find(n,k):
        if n == k :
            if result < box.count([0]*W) :
                return
            change(copy.deepcopy(box),0,D,box.count([0]*W))
            return

        else :
            box[n] = a[n]
            find(n+1,k)
            box[n] = [0]*W
            find(n+1,k)

    def change(arr,n,k,r) :
        global result
        if n == k :
            if check(arr):
                if result > r :
                    result = r
        else :
            if arr[n] == [0]*W :
                arr[n] = [1]*W
                change(arr,n+1,k,r)
                arr[n] = [0]*W
                change(arr,n+1,k,r)
            else :
                change(arr,n+1,k,r)

    find(0,k)



T = int(input())+1
for tc in range(1,T):
    D,W,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(D)]

    result = 9999
    if check(arr) :
        print("#{} {}".format(tc,0))
    else :
        f(copy.deepcopy(arr),D)
        print("#{} {}".format(tc, result))


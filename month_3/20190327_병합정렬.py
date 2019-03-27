def mergeSort(x):
    global cnt
    if len(x) > 1:
        mid = len(x)//2
        lx, rx = x[:mid], x[mid:] # 분할
        mergeSort(lx) # 왼쪽
        mergeSort(rx) # 오른쪽

        if lx[-1] > rx[-1]:
            cnt +=1
        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]

for tc in range(1,int(input())+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    cnt = 0
    mergeSort(numbers)
    print("#{} {} {}".format(tc,numbers[N//2], cnt))
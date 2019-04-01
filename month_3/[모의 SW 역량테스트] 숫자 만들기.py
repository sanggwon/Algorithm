def cal(num,idx,add,sub,multi,division):
    global n , maxV, minV
    if idx == n :
        maxV = max(num,maxV)
        minV = min(num,minV)
        return
    else :
        if add :
            cal(num + num_list[idx], idx+1, add-1,sub,multi,division)
        if sub :
            cal(num - num_list[idx], idx+1, add,sub-1,multi,division)
        if multi :
            cal(num * num_list[idx], idx+1, add,sub,multi-1,division)
        if division :
            cal(int(num / num_list[idx]), idx+1, add,sub,multi,division-1)

T = int(input())+1
for tc in range(1,T):
    maxV = -100000000
    minV = 100000000
    n = int(input().strip())
    a,b,c,d = map(int,input().strip().split())
    num_list = list(map(int,input().strip().split()))
    cal(num_list[0],1,a,b,c,d)
    print("#{} {}".format(tc,abs(maxV-minV)))

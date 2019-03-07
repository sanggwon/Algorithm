month = {1:31, 2:28 ,3:31 , 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for tc in range(1,int(input())+1):
    A1,A2,B1,B2 = map(int,input().split())
    res = 0
    for i in range(A1,B1):
        for mon,day in month.items():
            if i == mon :
                res += day
    res += B2 - A2 + 1

    print("#{} {}".format(tc,res))
month = list(range(1,13))
day1 = list(range(1,32))
day2 = list(range(1,31))
week = ["Mo ","Tu ","We ","Th ","Fr ","Se ","Su"]

last1 = len(day1)
last2 = len(day2)
div = 7

for i in month :
    a = str(i)+"월"
    print(a.center(20))
    print("".join(week))
    if i < 7 :
        start = 0
        if i%2 == 1 :
            for idx in range(start,last1+div,div):
                out = day1[start:start+div]
                outs =str(out)
                if out != [] :
                    print("".join(outs))
                    start += div  
        else :
            for idx in range(start,last2+div,div):
                out = day2[start:start+div]
                outs =str(out)
                if out != [] :
                    print("".join(outs))
                    start += div   
    else :
        start = 0
        if i%2 == 0 :     
            for idx in range(start,last1+div,div):
                out = day1[start:start+div]
                outs =str(out)
                if out != [] :
                    print("".join(outs))
                    start += div 
        else :
            for idx in range(start,last2+div,div):
                out = day2[start:start+div]
                outs =str(out)
                if out != [] :
                    print("".join(outs))
                    start += div     

## 두개의 차이점이 무엇일까?
out = str(list(range(0,5)))
print("".join(out))
out = ['a','s','d']
print("".join(out))
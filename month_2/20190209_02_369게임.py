count = 0
a = ""
for i in range(1,int(input())+1):
    for j in str(i) :
        if int(j) != 0 and int(j)%3 == 0:
            count+=1
    if count == 1 :
        i = "-"
    elif count ==2 :
        i = "--"
    else :
        i = i
    a += str(i)
    a +=" "
    count = 0
print(a)

        
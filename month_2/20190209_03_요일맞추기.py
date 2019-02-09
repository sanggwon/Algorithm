def week(lists):
    mon = [31,29,31,30,31,30,31,31,30,31,30,31]
    [m,d] = lists
    if (sum(mon[:m-1])+d)%7 == 1:
        num = 4
    if (sum(mon[:m-1])+d)%7 == 2:
        num = 5
    if (sum(mon[:m-1])+d)%7 == 3:
        num = 6
    if (sum(mon[:m-1])+d)%7 == 4:
        num = 0
    if (sum(mon[:m-1])+d)%7 == 5:
        num = 1
    if (sum(mon[:m-1])+d)%7 == 6:
        num = 2
    if (sum(mon[:m-1])+d)%7 == 0:
        num = 3
    return num

for i in range(int(input())):
    print(f"#{i+1} {week(list(map(int,input().split())))}")


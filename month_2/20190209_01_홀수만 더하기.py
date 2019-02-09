def num(a):
    my_sum = 0
    for i in a:
        if i%2 :
            my_sum+=i
    return my_sum

for i in range(int(input())):
    print(f"#{i+1} {num(list(map(int,input().split())))}")
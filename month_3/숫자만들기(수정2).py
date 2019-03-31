import sys
sys.stdin = open("input.txt","r")
def f(n,k,s):
    global max_num,min_num
    if n==k :
        if max_num < s:
            max_num = s
        if min_num > s :
            min_num = s
    else :
        for i in range(k):
            if u[i] == 0 :
                u[i] = 1
                if Operators[i] == "+":
                    f(n+1,k,s+numbers[n])
                elif Operators[i] == "-":
                    f(n+1,k,s-numbers[n])
                elif Operators[i] == "*":
                    f(n+1,k,s*numbers[n])
                elif Operators[i] == "/":
                    f(n+1,k,int(s/numbers[n]))
                u[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    O1,O2,O3,O4 = map(int,input().split())
    Operators = "+"*O1+"-"*O2+"*"*O3+"/"*O4
    numbers = list(map(int,input().split()))
    first = numbers[0]
    numbers = numbers[1:]
    u = [0]*(N-1)
    max_num = -100000000
    min_num = 100000000
    f(0,N-1,first)
    print("#{} {}".format(tc,abs(max_num-min_num)))
    

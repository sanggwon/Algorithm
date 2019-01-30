N = int(input("토끼의 휴식시간 : "))
M = int(input("거북이의 휴식시간 : "))
def gcd (N,M):
    mod = N%M
    while mod > 0 :
        N = M
        M = mod
        mod = N%M
    return M
def lcm (N,M):
    return N*M//gcd(N,M)

print(lcm(N,M))

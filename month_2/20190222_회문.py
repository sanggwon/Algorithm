import sys
sys.stdin = open("sample_input_22.txt","r")

def find(M,N) :
    result = ""
    for i in range(M) :
        for j in range(M-N+1):
            if S[i][j:N+j] == S[i][j:N+j][::-1] :
                return S[i][j:M]
            for x in range(N):
                result += S[j+x][i]
            if result == result[::-1]:
                return result
            else :
                result = ""


for tc in range(1,int(input())+1):
    M, N = map(int,input().split())
    S = [input() for _ in range(M)]


    print(f"#{tc} {find(M,N)}")

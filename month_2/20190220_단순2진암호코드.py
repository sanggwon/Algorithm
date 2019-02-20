import sys
sys.stdin = open("sample_input_17.txt","r")

T = int(input())

def code(N): # 암호코드가 있는 열의 위치를 찾음
    code = []
    for i in range(N-4):
        for j in range(49,53):
            if S[i][j] == "1" :
                code = S[i]
                return code

def code_s(code): # 암호코드의 행 위치를 찾아 슬라이싱
    for x in range(M-1,0,-1):
        if code[x] == "1" :
            return code[x-55:x+1]

def code_c(code_s) : # 암호코드를 7개의 숫자로 슬라이싱하여 해독 정보와 비교
    lists = []
    for n in range(8):
        for m in range(10):
            if code_s[n*7:(n+1)*7] == numbers[m] :
                lists.append(m) 
    return lists # 해독 코드

for tc in range(T):
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    numbers = ["0001101","0011001","0010011","0111101","0100011",
            "0110001","0101111","0111011","0110111","0001011"]

    print(f"#{tc+1}",end=" ")
    if not (sum(code_c(code_s(code(N)))[0:7:2])*3+sum(code_c(code_s(code(N)))[1:8:2]))%10 : # 해독코드 10배수인지 확인
        print(sum(code_c(code_s(code(N))))) # 10배수면 암호코드의 1을 모두 더함
    else : # 아니라면 0
        print(0)



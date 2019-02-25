import sys
sys.stdin = open("sample_input_30.txt","r")

for tc in range(int(input())):
    D,A,B,F = map(int,input().split())
    print(f"#{tc+1} {D/(A+B)*F}")

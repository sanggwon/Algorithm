import sys 
sys.stdin = open("sample_input_31.txt","r")
def find(routh,check, N):
    global result
    if N == check[0]:
        result.append(1)

    for i in range(len(routh)) :
        if check[1] == routh[i][1]:
            find(routh,[check[0],routh[i][0]],routh[i][0])
                

for tc in range(1,int(input())+1):
    result = []
    V,E = map(int,input().split())
    routh = [input().split() for _ in range(E)]
    check = input().split()
    find(routh,check,check[1])
    if result == []:
        print(f"#{tc}",0)
    else :
        print(f"#{tc}",1)

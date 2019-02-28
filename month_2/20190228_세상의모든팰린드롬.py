def find(S,l):
    for i in range(l//2):
        if S[i] != S[l-1-i]:
            if S[i]=="?" or S[l-1-i]=="?":
                pass
            else : 
                return "Not exist"
    return "Exist"
for tc in range(1,int(input())+1):
    S = input()
    l = len(S)
    print(f"#{tc} {find(S,l)}")
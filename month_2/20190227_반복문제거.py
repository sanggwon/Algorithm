for tc in range(1,int(input())+1):
    string = list(input())
    while 1==1:
        try :
            for i in range(len(string)) :
                if string[i] == string[i+1]:
                    del string[i:i+2]
                    break
        except :
            break
    print(f"#{tc} {len(string)}")
            
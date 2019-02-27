import sys 
sys.stdin = open("sample_input_32.txt","r")

operator = ["+","-","*","/","."]
for tc in range(1,int(input())+1):
    num = []
    num_list = input().split()
    for i in num_list :
        if not i in operator :
            num.append(i)
        else :
            try :
                if i == "+":
                    sec = num.pop()
                    fir = num.pop()
                    num.append(int(fir)+int(sec))
                if i == "-" :
                    sec = num.pop()
                    fir = num.pop()
                    num.append(int(fir)-int(sec))
                if i == "*" :
                    sec = num.pop()
                    fir = num.pop()
                    num.append(int(fir)*int(sec))
                if i == "/" :
                    sec = num.pop()
                    fir = num.pop()
                    num.append(int(int(fir)/int(sec)))
            except :
                print(f"#{tc}"+" "+"error")
                break

            if i == ".":
                if len(num) == 1 :
                    res = num.pop()
                    print(f"#{tc} {res}")
                else :
                    print(f"#{tc}"+" "+"error")
            
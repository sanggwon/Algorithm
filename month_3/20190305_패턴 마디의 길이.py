for tc in range(1,int(input())+1):
    S = input()
    for i in range(1,31):
        if S[0:i] == S[i+1:2*i+1]:
            print("#{} {}".format(tc,i+1))
            break
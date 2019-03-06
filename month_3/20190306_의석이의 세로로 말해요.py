for tc in range(1,int(input())+1):
    string = [input()for _ in range(5)]
    res = ""
    max_cnt = 0
    for n in range(5):
        if max_cnt < len(string[n]) :
            max_cnt = len(string[n])
    for i in range(max_cnt):
        for j in range(5):
            if len(string[j]) <=i :
                pass
            else :
                res += string[j][i]
    print("#{} {}".format(tc,res))
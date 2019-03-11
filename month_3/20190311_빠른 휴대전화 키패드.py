text = [[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],
        ["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]

for tc in range(1,int(input())+1):
    S,N = input().split()
    string = list(input().split())
    cnt = 0
    for i in string:
        check = []
        for j in i :
            index = 0
            for n in text :
                if j in n :
                    break
                index += 1
            check.append(index+1)
        if check == list(map(int,S)) :
            cnt +=1
    print("#{} {}".format(tc,cnt))



def talent(lists):
    [N,C] = lists
    return ((N//C)**(C-N%C))*(((N//C)+1)**(N%C))
    




for i in range(int(input())):
    print(f"#{i+1} {talent(list(map(int,input().split())))}")

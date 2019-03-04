import sys
sys.stdin = open("input2.txt","r")

for tc in range(1, int(input()) + 1):
    D, M, T, Y = map(int, input().split())
    plan = list(map(int, input().split()))

    res = Y
    for _ in range(2):
        stack = []
        my_sum = 0
        for i in plan:
            if i * D <= M:
                stack.append(i * D)
            else:
                stack.append(M)

            if len(stack) == 3:
                if sum(stack) <= T or stack[0] == 0:
                    my_sum += stack.pop(0)
                elif sum(stack) > T:
                    stack = []
                    my_sum += T
        if sum(stack) < T:
            my_sum += sum(stack)
        else:
            my_sum += T
        if res > my_sum:
            res = my_sum
        plan.reverse()




    print("#{} {}".format(tc,res))
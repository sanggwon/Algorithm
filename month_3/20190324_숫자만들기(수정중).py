# # def permutations(string): 
# #     result = set([string]) 
# #     if len(string) == 2: 
# #      result.add(string[1] + string[0]) 
# #     elif len(string) > 2: 
# #      for i, c in enumerate(string): 
# #       for s in permutations(string[:i] + string[i + 1:]): 
# #        result.add(c + s) 
# #     return list(result) 

from itertools import permutations
import operator

res = []
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    O1,O2,O3,O4 = map(int,input().split())
    Operators = "+"*O1+"-"*O2+"*"*O3+"/"*O4
    numbers = list(map(int,input().split()))
    max_num = -100000000
    min_num = 100000000
    for op in list(set(permutations(Operators))) :
        num = numbers[0]
        for i in range(N-1) :
            if op[i] == "+":
                num = operator.add(num,numbers[i+1])
            elif op[i] == "-":
                num = operator.sub(num,numbers[i+1])
            elif op[i] == "*":
                num = operator.mul(num,numbers[i+1])
            elif op[i] == "/":
                num = operator.truediv(num,numbers[i+1])
                num = int(num)
        if max_num < num :
            max_num = num
        if min_num > num :
            min_num = num
    res.append(max_num-min_num)
for r in range(len(res)) :
    print("#{} {}".format(r+1,res[r]))

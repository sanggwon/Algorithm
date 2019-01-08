def fact(n) :
    result = 1
    for i in range(1,n+1) :
        result *= i
    return result

def com(num1,num2) :
    return fact(num1)/(fact(num1-num2)*fact(num2))
    
print(com(6,4))
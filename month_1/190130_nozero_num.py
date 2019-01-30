def solution(num):
    no0_num = num +1
    strno0_num = str(no0_num)
    re_strno0_num = strno0_num.replace("0","1")
    num = int(re_strno0_num)
    return num

num = 9949999;
ret = solution(num)


print("solution 함수의 반환 값은", ret, "입니다.")
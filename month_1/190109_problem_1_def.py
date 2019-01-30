# [Problem1]
# print를 한줄에 2개 이상 써서 사용해주세요.

#  예제) 
#      print("안녕, ") print("Jupyter")

print("안녕, ") ; print("상권")

# [Problem2]
# print를 하나로 아래 문장을 써주세요.

# 예제)
    # 안녕하세요
    # 저는 파이썬을
    #     배우고 있는
    #         사람입니다.

print('''
    안녕하세요
    저는 파이썬을
        배우고 있는
            사람입니다.
''')


# [Problem3]
# 복소수 complex_data를 켤레복소수로 만드는 함수 complex_conjugate를 만들어주세요.

# 예제)
#     복소수의 표기는 본래 i이므로 i로 하도록 하겠습니다.
#     프로그래밍을 하는데에는 j로 사용하셔야 합니다.
#     complex_conjugate(5i) => -5i
#     complex_conjugate(3+7i) => (3-7i)

def complex_conjugate(com) :
    return com.real*2-com
print(complex_conjugate(3+2j))
print(complex_conjugate(5j))

# [Problem4]
# 10진수를 8진수로 변경하는 함수를 만들어주세요.

# 예제)
#     10 -> 0o12
#     7 -> 0o7
#     124 -> 0o174
def octal(value) :
    q,r = divmod(value,8)
    if q == 0 :
        return '0o' + str(r)
    else : 
        return octal(q) +str(r)
print(octal(10))

# [Problem5]
# 리스트list_data에 중간값을 리턴하는 center_value 함수를 만들어주세요.

# 예제)
#     list_data = [1,2,3,4,5]
#     center_value(list_data) => 3

list_data = [1,1,1,1,2,6,7]
list_data.sort()
def center_value(lists) :
    a = 0
    for i in range(1,len(lists)) :
        if len(lists)%2 != 0 :
            if lists[a] != lists[-i] :
                a += 1
            else :
                return lists[a]
        else :
            if lists[a] != lists[-i] :
                a += 1
                if a == len(lists)/2 :
                    return (lists[a-1],lists[a])
print(center_value(list_data))

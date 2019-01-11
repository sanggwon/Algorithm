# Problem1
# 사원 J씨가 자료를 정리하다가 모든 글자를 소문자로 만들었는데 관리자가 앞글자는 모두 대문자로 만들어 달라고 한다.
# 그리고 모든 자료들을 리스트로 만들어서 오름차순을 진행한다.
# J씨를 도와 문제를 해결해주시길 바랍니다.
# submit_list에 담아 보여주세요

str_data = "james justine martine mary unix linux java cotline tomas script moonjaein"

my_str_data = str_data.split()
a = []
for i in my_str_data :
    b = i[0].upper()+i[1:]
    a.append(b)
print(a)

# Problem2
# 관리자가 자료를 정리하다가 대소문자를 거꾸로 썼다고 한다.
# 당신에게 자료를 올바르게 고쳐달라고 한다.
# 대소문자를 바꿔서 출력하여 관리자에게 보여주면 된다.

data_err = "jAMES jUSTINE mARTINE mARY uNIX lINUX jAVA cOTLINE tOMAS sCRIPT mOONJAEIN"
lower_data = data_err.lower()
my_data_err = lower_data.split()
a=[]
for i in my_data_err :
    b = i[0].upper()+i[1:]
    a.append(b)
print(" ".join(a))



# Problem3¶
# 관리자가 아래의 자료 두개를 하나로 만들어 달라고 한다. 제출할 이름은 submit_result이다.
data_f1 = {'a':"apple", 'b':"banana", 'c':'cherry'}
data_f2 = {'o':"orange", 'p':"pineapple"}
data_result = {}
data_result.update(data_f1)
data_result.update(data_f2)
print(data_result)


# 예시)
# data_f1 = {'a':"apple", 'b':"banana", 'c':'cherry'}
# data_f2 = {'o':"orange", 'p':"pineapple"}

# 결과)
# submit_result = {'a':"apple", 'b':"banana", 'c':'cherry', 'o':"orange", 'p':"pineapple"}
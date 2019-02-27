def bracket(lists) :
    C = {"(":1,"{":1,"[":1,"<":1,
        ")":-1,"}":-1,"]":-1,">":-1}
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    for i in lists:
        if i == "(" or i == ")":
            a_count += C[i]
        if i == "{" or i == "}":
            b_count += C[i]
        if i == "[" or i == "]":
            c_count += C[i]
        if i == "<" or i == ">":
            d_count += C[i]

    if a_count == 0 and b_count == 0 and c_count == 0 and d_count == 0:
        return 1
    return 0

for tc in range(1,int(input())+1):
    print(f"#{tc} {bracket(input())}")
# [Problem1] Calc 계산기
# 클래스 Calc는 method로 두 수를 더해주는 add, 두 수를 빼주는 sub,
# 두 수를 곱해주는 mul, 두 수를 나눠주는 div를 가지고 있습니다.
# method는 값을 반환합니다.
# 기본값이 0일 때 div을 실행하면 error가 발생하므로 "0은 분모로 올수 없습니다"를 print해주세요.
# 또한, div에서 값이 반환되어지는 값이 정수(Integer)일 때는 int 타입으로 반환해주세요

# 편의상 예시는 표시하지 않고,
# 결과는 앞에 >>>표시로 하겠습니다.


class Calc :
    num = 0
    def add(self,num) :
        self.num += num
        return self.num
    def sub(self,num) :
        self.num -= num
        return self.num
    def mul(self,num) :
        self.num *= num
        return self.num
    def div(self,num) :
        try :
            self.num /= num
            result = self.num
            if result%1 == 0  :
                result = int(self.num) 
            else :
                result
        except ZeroDivisionError :
            result = "0은 분모로 올수 없습니다"
        finally:
            return result



calc = Calc()
print(calc.add(7))
print(calc.add(2))
print(calc.sub(5))
print(calc.mul(3))
print(calc.div(6))
print(calc.div(4))

calc = Calc()

print(calc.div(0))
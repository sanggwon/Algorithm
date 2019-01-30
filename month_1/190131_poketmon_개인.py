import random
class Poketmon :
     def __init__(self, name, lv):
          self.name = name
          self.lv = lv
          self.hp = lv*(random.randint(10,15))
          self.power = lv*(random.randint(4,6))
          self.speed = lv*(random.randint(1,2))
     def Bettle(self,enmey):
          print(f"이름:{self.name} 레벨:{self.lv} hp:{self.hp} power:{self.power} speed: {self.speed}")
          print(f"이름:{enmey.name} 레벨:{enmey.lv} hp:{enmey.hp} power:{enmey.power} speed: {enmey.speed}")
          
          if self.speed >= enmey.speed :
               position = 1
               print(f"이름:{self.name}이(가) 선공입니다!!")
          else : 
               position = 0
               print(f"이름:{enmey.name}이(가) 선공입니다!!")
          while self.hp > 0 and enmey.hp > 0 :
               if position == 1:
                    enmey.hp -= self.power
                    if enmey.hp < 0 :
                         enmey.hp = 0
                    print(f"{self.name}이 {self.power}만큼 공격하였습니다!!")
                    print(f"이름:{enmey.name} hp:{enmey.hp}")
                    position -= 1
               else :
                    self.hp -= enmey.power
                    if self.hp < 0 :
                         self.hp = 0
                    print(f"{enmey.name}이 {enmey.power}만큼 공격하였습니다!!")
                    print(f"이름:{self.name} hp:{self.hp}")
                    position += 1
          if self.hp == 0 :
               print(f"승자는 {enmey.name}입니다!!")
          else :
               print(f"승자는 {self.name}입니다!!")


p1 = Poketmon("피카츄",10)
p2 = Poketmon("꼬부기",10)

p1.Bettle(p2)


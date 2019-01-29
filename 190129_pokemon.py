import random

class Pokemon():
    def __init__(self,name,lv):
        self.name = name
        self.lv = lv
        self.hp = lv*random.randint(15,18)
        self.power = lv*random.randint(3,5)
        self.speed = random.randint(0,1)
    
    def info(self):
        print(f"{self.name}/{self.hp}/{self.power}/{self.speed}")

    def attack(self, enemy):
        enemy.hp -= self.power
        if enemy.hp < 0 :
            enemy.hp = 0
        print(f"{self.name}(이)가 공격했다")
        print(f"{enemy.name}/{enemy.hp}")
        if enemy.hp <= 0 :
            print(f"{enemy.name}(이)가 쓰러졌다.")

position = 0

pikachu = Pokemon("피카츄",20)
pikachu.info()
kkobugi = Pokemon("꼬부기",20)
kkobugi.info()

if pikachu.speed >= kkobugi.speed :
    position += 1
    while pikachu.hp >0 and kkobugi.hp > 0:
        if position == 1:
            pikachu.attack(kkobugi)
            position -= 1
        else :
            kkobugi.attack(pikachu)
            position += 1

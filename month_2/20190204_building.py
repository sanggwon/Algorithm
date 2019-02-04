# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

def building(T):
   building = list(map(int, input().split()))
   e = []
   for i in range(int(T)-4):
      a = building[i+2]-building[i+1]
      b = building[i+2]-building[i]
      c = building[i+2]-building[i+3]
      d = building[i+2]-building[i+4]
      if a<0 or b<0 or c<0 or d<0 :
         pass
      else:
          e.append(min([a,b,c,d])) 
   return sum(e)

for i in range(10) :
   print(f"#{i+1} {building(input())}")
from math import log
limak,bob=list(map(int,input().split()))

# while limak<=bob:
#     limak*=3
#     bob*=2
#     answer+=1

answer=int(log(bob/limak,3/2)+1) # From comparing Geometric progression

print(answer)
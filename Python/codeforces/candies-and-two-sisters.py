t=int(input())
answer=[]
for i in range(t):
    candies=int(input())
    count=0
    answer.append(str(candies//2 if candies%2!=0 else (candies-1)//2))
print('\n'.join(answer))
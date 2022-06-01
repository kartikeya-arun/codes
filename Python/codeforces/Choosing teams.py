n,k=list(map(int,input().split()))
teams=sorted(list(map(int,input().split())))
count=0
answer=0
for i in range(n):
    if teams[i]+k<=5:
        count+=1
    if(count!=0 and count%3==0):
        answer+=1
        count=0

print(answer)
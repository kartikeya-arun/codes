n=int(input())
boysSkill=sorted(list(map(int,input().split())))
m=int(input())
girlsSkill=sorted(list(map(int,input().split())))
count=0
for i in range(n):
    for j in range(m):
        if(abs(boysSkill[i]-girlsSkill[j])<=1):
            girlsSkill[j]+=1000
            count+=1
            break
print(count)
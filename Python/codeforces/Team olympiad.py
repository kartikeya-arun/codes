n=int(input())
t=list(map(int,input().split()))
count1=0
count2=0
count3=0
t1=[0]*n
t2=[0]*n
t3=[0]*n
for i in range(n):
    if t[i]==1:
        t1[count1]=i+1
        count1+=1
    elif t[i]==2:
        t2[count2]=i+1
        count2+=1
    else:
        t3[count3]=i+1
        count3+=1

num_teams=min(count1,count2,count3)


print(num_teams)
for i in range(num_teams):
    print(t1[i],t2[i],t3[i])
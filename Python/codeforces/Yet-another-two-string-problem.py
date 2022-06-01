t=int(input())
answer=[]
while t>0:
    a,b=list(map(int,input().split()))
    ans=(abs(a-b)+9)//10
    answer.append(ans)
    t-=1
for i in answer:
    print (i)
t=int(input())
answer=[]

while t>0:
    x,n,m=list(map(int,input().split()))
    while int(x/2)+10<x and n>0:
        x=int(x/2)+10
        n-=1
    x-=m*10
    if x<=0:
        answer.append('YES')
    else:
        answer.append('NO')
    t-=1

print('\n'.join(answer))
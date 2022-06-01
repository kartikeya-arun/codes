t=int(input())
answer=[]
while t>0:
    countOdd=0
    countEven=0
    n,x=list(map(int,input().split()))
    a=list(map(int,input().split()))
    for i in range(n):
        if a[i]%2!=0:
            countOdd+=1
        else:
            countEven+=1
    
    flag=False
    i=1
    while i<=countOdd and i<=x:
        have=countEven
        need=x-i
        if need<=have:
            flag=True
        i+=2
    
    if(flag):
        answer.append('Yes')
    else:
        answer.append('No')
    t-=1

print('\n'.join(answer))
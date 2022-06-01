t=int(input())
answer=[]
for i in range(t):
    a,b=list(map(int,input().split()))
    count=0
    if a==b:
        count+=2
    elif a>b and b>1:
        while a-b>b:
            a=a//b
            count+=1
        count+=2
    elif b>a:
        count+=1
    else:
        b+=1
        while a>0:
            if(a==b):
                count+=2
                break
            else:
                a=a//b
                count+=1
    

print('\n'.join(answer))
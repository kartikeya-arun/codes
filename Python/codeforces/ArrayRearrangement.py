t=int(input())
answer=''
for i in range(t):
    result=[]
    n,x=map(int,input().split())
    a1=list(map(int,input().split()))
    a2=list(map(int,input().split()))
    a1.sort()
    a2.sort(reverse=True)
    if(i!=t-1):
        input()
    for i in range(n):
        if((a1[i]+a2[i])>x):
            result.append(1)    
        else:
            result.append(0)
    if(1 in result):
        answer+='No\n'
    else:
        answer+='Yes\n'

print(answer[:len(answer)-1])

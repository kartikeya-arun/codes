n=int(input())
answer=[]
for i in range(n):
    [y,x]=list(map(int,input().split()))
    if(x>y):
        if(x%2==1):
            answer.append(str(x*x-y+1))
        else:
            x-=1
            answer.append(str(x*x+y))
    else:
        if(y%2==0):
            answer.append(str(y*y-x+1))
        else:
            y-=1
            answer.append(str(y*y+x))

print('\n'.join(answer))
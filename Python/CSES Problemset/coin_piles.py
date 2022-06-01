t=int(input())
answer=[]
for i in range(t):
    a,b=list(map(int,input().split()))
    if(2*a-b>=0 and (2*a-b)%3==0 and 2*b-a>=0 and (2*b-a)%3==0):
        answer.append("YES")
    else:
        answer.append('NO')

print('\n'.join(answer))
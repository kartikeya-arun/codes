t=int(input())

answer=[]

while t>0:
    n,a,b,c,d=list(map(int,input().split()))
    if n*(a+b)<c-d:
        answer.append('NO')
    elif n*(a-b)>c+d:
        answer.append('NO')
    else:
        answer.append('YES')
    t-=1

print('\n'.join(answer))
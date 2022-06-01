t=int(input())
answer=[]
while t>0:
    n,k=list(map(int,input().split()))
    quotient=k//(n-1)
    remainder=k%(n-1)
    if remainder==0:
        answer.append(str(n*quotient-1))
    else:
        answer.append(str(n*quotient+remainder))
    t-=1

print('\n'.join(answer))

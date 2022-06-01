answer=[]
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    parity=[0]*n
    for i in range(n):
        if a[i]%2==0:
            parity[i]=1
    if sum(parity)==0 or sum(parity)==n:
        answer.append("YES")
    else:
        answer.append("NO")
print('\n'.join(answer))